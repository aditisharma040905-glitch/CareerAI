"""
Database Operations
"""

import pandas as pd
from backend.database.connection import create_connection


def get_students_dataframe():
    """
    Fetch all students and return a Pandas DataFrame.
    """

    connection = create_connection()

    query = "SELECT * FROM students"

    df = pd.read_sql(query, connection)

    connection.close()

    return df

# ==========================================
# Save Prediction History
# ==========================================

def save_prediction(student_name, job_role, prediction, confidence):
    """
    Save prediction history into MySQL database.
    """

    connection = create_connection()

    cursor = connection.cursor()

    query = """
    INSERT INTO prediction_history
    (student_name, job_role, prediction, confidence)
    VALUES (%s, %s, %s, %s)
    """

    values = (
        student_name,
        job_role,
        prediction,
        confidence
    )

    cursor.execute(query, values)

    connection.commit()

    cursor.close()
    connection.close()