Goal: Create a GraphQL API using graphene and flask. Graphene allows for a code first appoach. (Ariadne would use a schema first approach). SQLalchemy is an ORM.









Some References:
https://www.youtube.com/watch?v=sUw2omk61Gg #Uses sqlite not PostgreSQL

PostgreSQL
https://www.w3resource.com/PostgreSQL/postgresql-python-connection.php
https://www.postgresqltutorial.com/postgresql-python/connect/

SQLAlchemy
https://docs.sqlalchemy.org/en/14/dialects/postgresql.html
https://www.compose.com/articles/using-postgresql-through-sqlalchemy/


Graphene
https://graphene-python.org/

Flask
https://flask.palletsprojects.com/en/2.1.x/quickstart/

Process:

create virtual environment in gitbash: 

    * python -m venv env
    * source env/Scripts/activate
    * pip install graphene graphene-sqlalchemy flask sqlalchemy Flask-GraphQL (note: there was initial difficulty as the dependencies are specific ex: requires >1.1 <2)
    * pip freeze > requirements.txt


    * create table in db/\_\_init__.py  with classes and use SQLalchemy
    * run create_db.py to create db
    * add objects into db: scripts.py
    * define schema (schemas/\_\_init__.py) based off of data via graphene
    * create Query (schemas/\_\_init__.py)
    * create Mutations (schemas/\_\_init__.py)

Terminal/GitBash:

    * export FLASK_APP=main.py
    * export FLASK_DEBUG=1
    * flask run



#Todo: hook up postgres dB instead of sqlIte