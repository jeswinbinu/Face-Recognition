#2_attendance_sheet

import os
import streamlit as st
import pandas as pd
from io import BytesIO
subject_chosen = ''

st.set_page_config(page_title="Attendance Sheet", page_icon="📋")

def get_list_of_subjects():
    return ['CD', 'AAD', 'CGIP', 'PY', 'IEFT']

subject_chosen = st.sidebar.selectbox('Select a subject:', get_list_of_subjects())

st.title(f'{subject_chosen} Attendance List')

# #get current directory
# current_directory = os.path.dirname(os.path.abspath(__file__))

# fr_directory = os.path.dirname(current_directory)

# #construct file path to attendance.csv
# file_path = os.path.join(fr_directory, 'attendance', 'attendance.csv')

# atten_df = pd.read_csv(file_path)
# st.write(atten_df)



current_directory = os.path.dirname(os.path.abspath(__file__))

fr_directory = os.path.dirname(current_directory)

#construct file path to f'{subject_chosen}.csv'
csv_file_path = os.path.join(fr_directory, 'attendance', f'{subject_chosen}.csv')
# Read the CSV file with the specified column names
atten_df = pd.read_csv(csv_file_path)

# Define the path where you want to save the Excel file
excel_file_path = f'{subject_chosen}.xlsx'

# Write the DataFrame to an Excel file
atten_df.to_excel(excel_file_path, index=False)  # Set index=False to avoid writing row indices

def get_excel_file(excel_df):
    with BytesIO() as output:
        writer = pd.ExcelWriter(output, engine='xlsxwriter')
        excel_df.to_excel(writer, index=False)
        writer.close()
        excel_file = output.getvalue()
    return excel_file

# Read the Excel file into a DataFrame
excel_df = pd.read_excel(excel_file_path)

# Display the DataFrame in Streamlit
st.write(excel_df)

excel_file = get_excel_file(excel_df)
st.download_button(label='Download Excel File', data=excel_file, file_name=f'{subject_chosen}.xlsx', mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')