import mysql.connector as connector 
import os 

"""
DB_PASSWORD = os.environ["DBPASSWORD"]
DB_USER = os.environ["DBUSER"]
DB_HOST = os.environ["DBHOST"]
"""

conn = connector.connect(user="root",host="0.0.0.0",passwd="Abc123")
print(conn)