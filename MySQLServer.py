"""
Write a simple python script that creates the database alx_book_store in your MySQL server.

Name of python script should be MySQLServer.py
If the database alx_book_store already exists, your script should not fail
You are not allowed to use the SELECT or SHOW statements
NOTE :

Required to print message such as Database 'alx_book_store' created successfully! when database is successfully created.

Print error message to handle errors when failing to connect to the DB.

handle open and close of the DB in your script.

Repo:

GitHub repository: Intro_to_DB
File: MySQLServer.py
"""

import mysql.connector
from mysql.connector import Error

try:
    # Connect to MySQL server (without specifying database)
    connection = mysql.connector.connect(
        host="localhost",
        user="george",
        password="NeverEn0ugh001"
    )

    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store;")
        print("Database 'alx_book_store' created successfully!")
except Error as e:
    print(f"Error while connecting to MySQL: {e}")
finally:
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()