"""
Database Connection Module
"""

import mysql.connector

from backend.database.config import HOST, PORT, USER, PASSWORD, DATABASE


def create_connection():
    """
    Create and return a MySQL database connection.
    """

    try:
        connection = mysql.connector.connect(
            host=HOST,
            port=PORT,
            user=USER,
            password=PASSWORD,
            database=DATABASE
        )

        if connection.is_connected():
            print("✅ Connected to CareerAI Database")

        return connection

    except mysql.connector.Error as error:
        print("❌ Database Connection Error")
        print(error)
        return None