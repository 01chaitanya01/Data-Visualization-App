import streamlit as st
import pandas as pd
from io import StringIO

def convert_to_excel(csv_file):
    # Convert file object to string buffer
    csv_string = StringIO(csv_file.getvalue().decode("utf-8"))

    # Read the CSV string into a DataFrame
    dataset = pd.read_csv(csv_string)
    dataframe = pd.DataFrame(dataset)

    # Convert DataFrame to Excel and save it
    excel_filename = "converted_excel_file_1.xlsx"
    dataframe.to_excel(excel_filename, index=False)

    return excel_filename

# Streamlit app
def main():
    st.markdown("# Convert to Excel 📄")
    # File uploader for CSV
    csv_file = st.file_uploader("Upload CSV file", type=['csv'])

    if csv_file:
        st.success("CSV file uploaded successfully!")
        st.write("Preview of the CSV data:")
        st.write(pd.read_csv(csv_file))

        # Convert to Excel on button click
        if st.button("Convert to Excel"):
            st.success("Conversion completed! Excel file is ready for download.")
            excel_filename = convert_to_excel(csv_file)
            st.download_button(
                label="Download Excel file",
                data=open(excel_filename, 'rb').read(),
                file_name= "converted_excel_file.xlsx",
                mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
            )

if __name__ == "__main__":
    main()
