import os
import psycopg2
from flask import g

def get_connection():
    return psycopg2.connect(
        host=os.environ["DB_HOST"],
        database=os.environ["DB_NAME"],
        user=os.environ["DB_USER"],
        password=os.environ["DB_PASSWORD"],
        port=os.environ.get("DB_PORT")
    )

def get_db():
    if "db" not in g:
        g.db = get_connection()
    return g.db

def close_db(e=None):
    db = g.pop("db", None)
    if db is not None:
        db.close()
