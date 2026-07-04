from backend.database.connection import create_connection

connection = create_connection()

if connection:
    print("CareerAI is ready to use!")

from backend.database.operations import get_all_students

students = get_all_students()

print("\n===== STUDENTS DATA =====\n")

for student in students:
    print(student)