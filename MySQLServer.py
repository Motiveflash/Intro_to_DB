import mysql.connector
from mysql.connector import Error
import getpass

def create_database():
    try:
        # Get username and password securely
        user_name = input("Enter your MySQL username: ")
        password = getpass.getpass("Enter your MySQL password: ")
        
        # Establish a connection to MySQL server
        connection = mysql.connector.connect(
            host = 'localhost',
            user = user_name,
            password = password
        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            # Create the database if it does not already exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error:
        print("We got an error while connecting")
           
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        
    finally:
        # Close the connection
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

if __name__ == "__main__":
    create_database()