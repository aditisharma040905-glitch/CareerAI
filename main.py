from backend.database.operations import get_students_dataframe

# Fetch Data
df = get_students_dataframe()

print("\n===== STUDENTS DATAFRAME =====\n")
print(df)

print("\n==============================")
print("Dataset Shape")
print("==============================")
print(df.shape)

print("\n==============================")
print("Column Names")
print("==============================")
print(df.columns)

print("\n==============================")
print("Dataset Information")
print("==============================")
df.info()

print("\n==============================")
print("Statistical Summary")
print("==============================")
print(df.describe())

print("\n==============================")
print("Average CGPA")
print("==============================")
print(df["cgpa"].mean())

print("\n==============================")
print("Highest CGPA")
print("==============================")
print(df["cgpa"].max())

print("\n==============================")
print("Lowest CGPA")
print("==============================")
print(df["cgpa"].min())

print("\n==============================")
print("Students in Each Branch")
print("==============================")
print(df["branch"].value_counts())

print("\n==============================")
print("Gender Distribution")
print("==============================")
print(df["gender"].value_counts())