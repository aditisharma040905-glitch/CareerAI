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

# ==========================================
# Get Prediction History
# ==========================================

def get_prediction_history():
    """
    Fetch prediction history from MySQL.
    """

    connection = create_connection()

    query = """
    SELECT
        student_name,
        job_role,
        prediction,
        confidence,
        created_at
    FROM prediction_history
    ORDER BY created_at DESC
    """

    df = pd.read_sql(query, connection)

    connection.close()

    return df

# ==========================================
# Dashboard Statistics
# ==========================================

def get_dashboard_stats():
    """
    Return dashboard statistics.
    """

    connection = create_connection()

    cursor = connection.cursor()

    # Total Predictions
    cursor.execute("SELECT COUNT(*) FROM prediction_history")
    total_predictions = cursor.fetchone()[0]

    # Placed Students
    cursor.execute(
        "SELECT COUNT(*) FROM prediction_history WHERE prediction='Placed'"
    )
    placed_students = cursor.fetchone()[0]

    # Not Placed Students
    cursor.execute(
        "SELECT COUNT(*) FROM prediction_history WHERE prediction='Not Placed'"
    )
    not_placed_students = cursor.fetchone()[0]

    cursor.close()
    connection.close()

    return (
        total_predictions,
        placed_students,
        not_placed_students
    )