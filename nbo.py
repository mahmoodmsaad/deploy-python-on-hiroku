import pandas as pd
import streamlit as st

def process_data(file_contents):
    try:
        # Load the CSV file into a DataFrame
        df = pd.read_csv(file_contents)

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

            # Display the top 5 rows in a Streamlit table
            st.table(top_5_rows)

            st.success("Data processing complete.")
        else:
            st.warning("Column 'kcal/mol' not found in the filtered DataFrame.")
    
    except Exception as e:
        st.error(f"An error occurred: {e}")

# Streamlit UI
def main():
    st.title("NBO Orbital Processor")

    # File uploader widget
    uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

    if uploaded_file is not None:
        # Display some details about the uploaded file
        st.write("Uploaded file details:")
        st.write({"filename": uploaded_file.name, "filetype": uploaded_file.type, "size (bytes)": uploaded_file.size})

        # Process the data when the user clicks the "Process" button
        if st.button("Process"):
            # Convert the uploaded file to a DataFrame
            file_contents = uploaded_file.read()
            process_data(file_contents)

# Run the Streamlit app
if __name__ == '__main__':
    main()
