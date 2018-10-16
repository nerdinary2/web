import psycopg2
import sys
from .db_settings import *
from sqlalchemy import create_engine

def init():
    

    if sys.platform == "win32":
        conn = psycopg2.connect(database=DB, user=USER, password=PASSWORD, host='localhost', port=PORT)
        cur = conn.cursor()
    else:
        print("The OS of this machine is " + sys.platform + ". Connecting to remote server...")
        host = '143.248.109.99'
        conn = psycopg2.connect(database=DB, user=USER, password=PASSWORD, host=HOST, port=PORT)
        cur = conn.cursor()
    return conn, cur

engine = create_engine('postgresql+psycopg2://{}:{}@{}/{}'.format(USER, PASSWORD, HOST,DB))
