#3_add_new_student.py

import os
import streamlit as st
import csv

def save_student_pics(name, pics):
    
    current_directory = os.path.dirname(os.path.abspath(__file__))
    fr_directory = os.path.dirname(current_directory)

    database_path = os.path.join(fr_directory, "database", name)
    os.makedirs(database_path, exist_ok=True)
    for i, pic in enumerate(pics):
        pic_path = os.path.join(database_path, f"{name}{i+1}.png")
        with open(pic_path, "wb") as f:
            f.write(pic.getvalue())

def get_existing_dates(csv_file_path):
    with open(csv_file_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader)
        existing_dates = headers[4:] if len(headers) > 4 else []  # Assuming first four columns are fixed
    return existing_dates

import os
import csv

def add_student_to_csv(name, ktu, rollno):
    current_directory = os.path.dirname(os.path.abspath(__file__))
    fr_directory = os.path.dirname(current_directory)

    subjects = ['CD', 'AAD', 'CGIP', 'PY', 'IEFT']
    student_added = False
    
    for subject in subjects:
        csv_file_path = os.path.join(fr_directory, 'attendance', f'{subject}.csv')
        existing_dates = get_existing_dates(csv_file_path)

        # Check if the CSV file exists, if not, create it with headers
        if not os.path.exists(csv_file_path):
            with open(csv_file_path, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                # Get the headers from the existing CSV file or define them
                headers = ['Sl.No', 'RollNo', 'KTU_ID', 'Name']
                headers += existing_dates
                writer.writerow(headers)
        
        # Get the next available slno
        slno = get_next_slno(csv_file_path)
        
        # Append student details to the CSV file
        with open(csv_file_path, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            row = [slno, rollno, ktu, name]
            existing_dates_count = len(existing_dates)
            row += ['A'] * existing_dates_count
            writer.writerow(row)
            student_added = True
    return student_added

def get_existing_dates(csv_file_path):
    with open(csv_file_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader)
        existing_dates = headers[4:] if len(headers) > 4 else []  # Assuming first four columns are fixed
    return existing_dates

def get_next_slno(csv_file_path):
    slno = 1
    if os.path.exists(csv_file_path):
        with open(csv_file_path, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # Skip the header row
            for row in reader:
                slno += 1
    return slno


# def add_student_to_csv(name, ktu, rollno):
    
#     current_directory = os.path.dirname(os.path.abspath(__file__))
#     fr_directory = os.path.dirname(current_directory)

#     subjects = ['CD', 'AAD', 'CGIP', 'PY', 'IEFT']
#     for subject in subjects:
#         csv_file_path = os.path.join(fr_directory, 'attendance', f'{subject}.csv')
#         existing_dates = get_existing_dates(csv_file_path)
#         # Check if the CSV file exists, if not, create it with headers
#         # if not os.path.exists(csv_file_path):
#         #     with open(csv_file_path, 'w', newline='') as csvfile:
#         #         writer = csv.writer(csvfile)
#         #         writer.writerow(['Sl.No', 'RollNo', 'KTU_ID', 'Name'])  # Assuming 10 pre-existing columns
#         #         headers += existing_dates
#         #         writer.writerow(headers)
                
#         # Get the next available slno
#         slno = 1
#         if os.path.exists(csv_file_path):
#             with open(csv_file_path, 'r', newline='') as csvfile:
#                 reader = csv.reader(csvfile)
#                 next(reader)  # Skip the header row
#                 for row in reader:
#                     slno += 1
        
#         # Append student details to the CSV file
#         with open(csv_file_path, 'a', newline='') as csvfile:
#             writer = csv.writer(csvfile)
#             writer.writerow([slno, rollno, ktu, name])  # Assuming 10 pre-existing columns
#             existing_dates_count = len(existing_dates)
#             row += ['A'] * existing_dates_count
#             writer.writerow(row)
            

def delete_representations():
    representations_file = os.path.join("database", "representations_facenet512.pkl")
    if os.path.exists(representations_file):
        os.remove(representations_file)

def main():
    st.title("Add New Student")

    name = st.text_input("Enter Student Name")
    ktu_rollno = st.text_input("Enter KTU Roll Number")
    class_rollno = st.text_input("Enter Class Roll Number")

    uploaded_files = st.file_uploader("Upload Student Pictures (up to 3)", accept_multiple_files=True)

    if st.button("Add Student"):
        if not name:
            st.error("Please enter the student's name.")
        else:
            if not uploaded_files:
                st.warning("No pictures uploaded. Student will be added without pictures.")

            if uploaded_files:
                save_student_pics(name, uploaded_files)
                student_added = add_student_to_csv(name, ktu_rollno, class_rollno)
                
                if student_added:
                    st.success("Student added successfully.")
                    delete_representations()

            st.success("Student added successfully.")

if __name__ == "__main__":
    main()
