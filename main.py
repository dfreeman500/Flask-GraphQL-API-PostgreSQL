from flask import Flask
from flask_graphql import GraphQLView
from schemas import schema

app = Flask(__name__)


# url rule that takes in graphQL endpoint
# only need one endpoint


app.add_url_rule(
    "/graphql",
    view_func=GraphQLView.as_view(
        "graphql",
        schema=schema,
        graphiql=True
    )
)
