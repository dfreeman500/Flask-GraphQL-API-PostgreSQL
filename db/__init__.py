from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    create_engine,
    String,
    Integer,
    Column,
    ForeignKey,
    Text

)
from sqlalchemy.orm import relationship, sessionmaker, scoped_session

from connection import connection_string


# A base class stores a catlog of classes and mapped tables in the Declarative 
# system. This is called as the declarative base class. There will be usually 
# just one instance of this base in a commonly imported module. The declarative_base() 
# function is used to create base class.

Base = declarative_base()

# create_engine() function is called to set up an engine object which is 
# subsequently used to perform SQL operations. The function has two arguments, 
# one is the name of database and other is an echo parameter when set to 
# True will generate the activity log. If it doesn’t exist, the database will 
# be created.
engine = create_engine(connection_string, echo=True)

# The job of the scoped_session is simple; hold onto a Session for all who ask 
# for it. As a means of producing more transparent access to this Session, the 
# scoped_session also includes proxy behavior, meaning that the registry itself 
# can be treated just like a Session directly; when methods are called on this 
# object, they are proxied to the underlying Session being maintained by the registry

# The SQL expression object itself references an Engine or Connection known as the bind, 
# which it uses in order to provide so-called “implicit” execution services.

session = scoped_session(
    sessionmaker(bind=engine)
)

# query_property returns a class property which produces a Query object against
#  the class and the current Session when called.


Base.query = session.query_property()

"""
table users:
id - primary key
username : str
email


table posts:
id - primary key
title: str
content:text
user_id -> users.id
"""


class User(Base):
    __tablename__ = "users"
    id = Column(Integer(), primary_key=True)
    username = Column(String(45), nullable=False)
    email = Column(String(80), nullable=False)
    posts = relationship("Post", backref="author")

    def __repr__(self):
        return f"<User {self.username}>"


class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer(), primary_key=True)
    title = Column(String(), nullable=False)
    content = Column(Text(), nullable=False)
    user_id = Column(Integer(), ForeignKey("users.id"))

    def __repr__(self):
        return f"<Post {self.title}>"


#relationship()
# The above configuration establishes a collection of Post objects on User 
# called User.posts. It also establishes a .user attribute on Post which 
# will refer to the parent User object.

# In fact, the relationship.backref keyword is only a common shortcut for placing 
# a second relationship() onto the Post mapping, including the establishment of 
# an event listener on both sides which will mirror attribute operations in both 
# directions.