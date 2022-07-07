from graphene import ObjectType, Schema, String


class Query(ObjectType):
    hello = String(name=String(default_value="Stranger"),
                   age=String(default_value="72"))
    goodbye = String()

    def resolve_hello(root, info, name, age):
        return f"Hello {name} your age is {age}"

    def resolve_goodbye(root, info):
        return "Good bye"


schema = Schema(query=Query)

"""
type Query{
    hello(name:String="Stranger")
    goodbye:String
}
"""

query_str = "{hello}"

result = schema.execute(query_str)

print(result)

query_with_args = '{hello(name:"Dan",age:"71")}'

result2 = schema.execute(query_with_args)

print(result2)
