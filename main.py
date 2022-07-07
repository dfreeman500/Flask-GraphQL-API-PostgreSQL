from flask import Flask
from flask_graphql import GraphQLView
from schemas import schema, UserDBModel, PostDBModel
from db import session
import json

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


@app.route("/")
def hello():
    return "<h1>Hello, World!</h1>"


@app.route("/users", methods=["GET"])
def get_users():
    a = session.query(UserDBModel).all()
    b = session.query(PostDBModel).all()
    print(a)
    return str(a), 200


@app.route("/posts", methods=["GET"])
def get_posts():
    b = session.query(PostDBModel).all()
    print(b)
    return str(b), 200    