"""
Database Operations
"""

from backend.database.connection import create_connection


def get_all_students():
    """
    Fetch all students from database
    """

    connection = create_connection()

    if connection is None:
        return []

    cursor = connection.cursor()

    query = "SELECT * FROM students"

    cursor.execute(query)

    students = cursor.fetchall()

    cursor.close()
    connection.close()

    return students