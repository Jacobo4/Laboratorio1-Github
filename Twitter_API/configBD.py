import psycopg2
import pandas as pd 
import numpy as np 
from configparser import ConfigParser

def create_connection():
    
    global HOST
    global DATABASE
    global USER
    global PASSWORD
    global PORT
    
    config = ConfigParser()
    config.read('Laboratorio1-Github/Twitter API/config.ini')
    HOST = config.get('PostegreSQL', 'HOST')
    DATABASE = config.get('PostegreSQL', 'DATABASE')
    USER = config.get('PostegreSQL', 'USER')
    PASSWORD = config.get('PostegreSQL', 'PASSWORD')
    PORT = config.get('PostegreSQL', 'PORT')

    connection = psycopg2.connect(
        host =  HOST,
        database = DATABASE,
        user = USER,
        password = PASSWORD,
        port = PORT,
    )


def execute_query(query):
    with psycopg2.connect(
    host = HOST,
    database = DATABASE,
    user = USER,
    password = PASSWORD,
    port = PORT
    ) as connection:

        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()

