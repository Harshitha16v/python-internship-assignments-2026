import pandas as pd


def load_dataset(file_path):
    """Load dataset safely"""
    try:
        df = pd.read_csv(file_path)
        print("Dataset loaded successfully!\n")
        return df
    except Exception as e:
        print("Error loading dataset:", e)
        return None


def dataset_overview(df):
    print("----- Top 5 Rows -----")
    print(df.head(), "\n")


def highest_value_column(df):
    numeric_cols = df.select_dtypes(include='number')

    if numeric_cols.empty:
        print("No numeric columns found.\n")
        return

    max_values = numeric_cols.max()
    highest_col = max_values.idxmax()

    print("----- Highest Value Column -----")
    print(f"Column: {highest_col}")
    print(f"Highest Value: {max_values[highest_col]}\n")


def missing_values_report(df):
    print("----- Missing Values -----")
    print(df.isnull().sum(), "\n")


def generate_insights(df):
    print("----- Insights -----")

    print("1. Dataset contains", df.shape[0], "rows and", df.shape[1], "columns.")
    print("2. Numeric columns:", list(df.select_dtypes(include='number').columns))
    print("3. Columns with missing values:",
          list(df.columns[df.isnull().sum() > 0]))
    print("4. Column with most missing values:",
          df.isnull().sum().idxmax())
    print("5. Data types summary:\n", df.dtypes)


def main():
    file_path = "students_data.csv"  

    df = load_dataset(file_path)

    if df is not None:
        dataset_overview(df)
        highest_value_column(df)
        missing_values_report(df)
        generate_insights(df)


if __name__ == "__main__":
    main()