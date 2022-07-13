import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType
from db import (
    User as UserDBModel,
    Post as PostDBModel,
    session
)

#inherits SQL alchemy 
class UserSchema(SQLAlchemyObjectType):
    class Meta:
        model = UserDBModel
        interfaces = (relay.Node,) # is tuple

        #https://stackoverflow.com/questions/50300832/what-is-the-meta-subclass-in-graphene
            #"Graphene uses a Meta inner class on ObjectType to set different options."
            #"The SQLAlchemyObjectType class adds three more options, model, registry, and 
            # connection. If you look through the code the model option is your SQLAlchemy 
            # model class. The SQLAlchemyObjectType class uses the model option to inspect 
            # your model and create your respective fields automatically."

class PostSchema(SQLAlchemyObjectType):
    class Meta:
        model = PostDBModel
        interfaces = (relay.Node,)

# We must define a query for our schema = graphene.Schema(query=Query, mutation=Mutation)
class Query(graphene.ObjectType):
    node = relay.Node.Field()

    #https://docs.graphene-python.org/en/latest/relay/nodes/
    #A Node is an Interface provided by graphene.relay that contains a 
    # single field id (which is a ID!). Any object that inherits from it 
    # has to implement a get_node method for retrieving a Node by an id.
    #As is required in the Relay specification, the server must implement 
    # a root field called node that returns a Node Interface.
    #You can use the predefined relay.Node or you can subclass it, defining 
    # custom ways of how a node id is encoded (using the to_global_id method 
    # in the class) or how we can retrieve a Node given a encoded id (with the 
    # get_node_from_global_id method).

    #For this reason, graphene provides the field relay.Node.Field, which links 
    # to any type in the Schema which implements Node. 

    all_users = SQLAlchemyConnectionField(UserSchema.connection)

    all_posts = SQLAlchemyConnectionField(PostSchema.connection)

    # https://docs.graphene-python.org/projects/sqlalchemy/en/latest/tips/
    # By default the SQLAlchemyConnectionField sorts the result elements over 
    # the primary key(s). The query has a sort argument which allows to sort 
    # over a different column(s)
    # Allows sorting over multiple columns, by default over the primary key


#A Mutation is a special ObjectType that also defines an Input.
#https://docs.graphene-python.org/en/latest/types/mutations/




class UserMutation(graphene.Mutation):
    class Arguments:
        username=graphene.String(required=True)
        email=graphene.String(required=True)
        #Arguments attributes are the arguments that the Mutation UserMutation 
        # needs for resolving, in this case name will be the only argument for the mutation.
        #InputFields are used in mutations to allow nested input data for mutations.
        #To use an InputField you define an InputObjectType that specifies the structure of your 
        # input data:

    user = graphene.Field(lambda:UserSchema)
    # user is the output field of the Mutation when it is resolved.


    #mutate is the function that will be applied once the mutation is called. 
    # This method is just a special resolver that we can change data within. It takes the 
    # same arguments as the standard query Resolver Parameters.
    def mutate(self,info,username,email):
        user=UserDBModel(
            username=username,
            email=email
        )

        session.add(user)
        session.commit()

        return UserMutation(user=user)


class PostMutation(graphene.Mutation):
    class Arguments:
        user_id=graphene.Int()
        title=graphene.String(required=True)
        content=graphene.String(required=True)



    post=graphene.Field(lambda:PostSchema)

    def mutate(self, info,user_id, title, content):
        
        author=session.query(UserDBModel).filter_by(id=user_id).first()
        
        new_post=PostDBModel(
            title=title,
            content=content,
            author=author
            )

        session.add(new_post)
        session.commit()

        return PostMutation(post=new_post)


class Mutation(graphene.ObjectType):
    mutate_user=UserMutation.Field()
    mutate_post=PostMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)

