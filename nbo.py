import pandas as pd

def process_data():
    # Load the CSV file into a DataFrame
    df = pd.read_csv('unit 2.csv')

    # Create a boolean mask to identify rows containing 'RY*' or 'CR' in any column
    mask = df.apply(lambda row: any(['RY*' in str(cell) or 'CR' in str(cell) for cell in row]), axis=1)

    # Invert the mask to keep rows without 'RY*' or 'CR'
    df_filtered = df[~mask]

    # Check if 'kcal/mol' column exists
    if 'kcal/mol' in df_filtered.columns:
        # Sort the DataFrame by 'kcal/mol' in descending order
        df_sorted = df_filtered.sort_values(by='kcal/mol', ascending=False)

        # Take the top 5 rows based on the specified number
        top_5_rows = df_sorted.head(5)

        # Save the top 5 rows to a new CSV file
        top_5_rows.to_csv('top_sorted_result.csv', index=False)

        print("Data processing complete. Top 5 rows saved to 'top_sorted_result.csv'")
    else:
        print("Column 'kcal/mol' not found in the filtered DataFrame.")

if __name__ == '__main__':
    process_data()
