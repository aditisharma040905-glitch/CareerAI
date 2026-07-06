from backend.database.operations import get_students_dataframe
from ml.visualization import (
    plot_branch_distribution,
    plot_cgpa_distribution
)
from ml.preprocessing import (
    check_missing_values,
    check_duplicates,
    check_data_types
)
def main():
    # Fetch data from MySQL
    df = get_students_dataframe()

    print("\n===== STUDENTS DATAFRAME =====\n")
    print(df)

    # Create visualization
    plot_branch_distribution(df)
    plot_cgpa_distribution(df)

    check_missing_values(df)
    check_duplicates(df)
    check_data_types(df)
if __name__ == "__main__":
    main()