
# Datbase code for Reserve Table
import datetime
import psycopg2

DBNAME = "ReserveTable"
def get_posts():
    db = psycopg2.connect(database = DBNAME)

def add_post(content):
    db = psycopg2.connect(database = DBNAME)
