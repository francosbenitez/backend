# load the neccesary libraries
import mysql.connector
from mysql.connector import Error
import pandas as pd

# set the neccesary functions
def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection

def read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f"Error: '{err}'")
        
# connect to database
connection = create_db_connection("localhost", "root", "1234", "world")
        
# queries and transform table to dataframe 
q1 = """
SELECT *
FROM COUNTRY;
"""

results = read_query(connection, q1)
from_db = []
for result in results:
  result = list(result)
  from_db.append(result)

df = pd.DataFrame(from_db)  



