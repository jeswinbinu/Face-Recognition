#streamlit_app.py
import streamlit as st
from PIL import Image
from identify2 import *
from io import BytesIO

st.set_page_config(page_title="CS", page_icon=":camera:")

# def main():
#     st.title("MecAttendence")
#     # sample_image_path = "./sample_image.jpg"
#     # sample_image = Image.open(sample_image_path)

#     # buf = BytesIO()
#     # sample_image.save(buf, format="JPEG")
#     # byte_im = buf.getvalue()

#     # sample_image_name = "sample_image.jpg"
#     # st.download_button(label="Download Sample Image", data=byte_im, file_name=sample_image_name, key="download_button")


#     uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

#     if uploaded_file is not None:
#         image_placeholder = st.empty()
#         recognizing_message = st.empty()

#         image_placeholder.image(uploaded_file, caption="Uploaded Image.", use_column_width=True)
#         recognizing_message.write("Recognizing...")
       
#         total_faces = faceDetection(uploaded_file)
#         names = faceRecognition(uploaded_file)

#         # Face Detection Results Section
#         recognizing_message.empty()  
#         st.header("Face Detection Results:")
#         st.write(f"Total Faces Detected: {total_faces}")
#         st.write(f"Total Recognized Faces: {getKnownFaces()}")
#         st.write(f"Total Unrecognized Faces: {getUnknownFaces()}")

#         # Names Section
#         if names:
#             st.header("Names:")
#             for name in names:
#                 st.write(f"- {name}")

#         # Known Faces Section
#         known_names = getKnownName()
#         if known_names:
#             st.header("Known Faces:")
#             for name in known_names:
#                 known_image_path = f"./known/{name}.jpg"
#                 known_image = Image.open(known_image_path)
#                 st.image(known_image, caption=name, width=200)

#         # Unknown Faces Section
#         st.header("Unknown Faces:")
#         if getUnknownFaces() == 0:
#             st.write("None")
#         else:
#             for i in range(getUnknownFaces()):
#                 unknown_image_path = f"./unknown/{i}.jpg"
#                 unknown_image = Image.open(unknown_image_path)
#                 st.image(unknown_image, caption=f"Unknown Face #{i + 1}", width=200)

#         # Reset the known names and face counts
#         setKnownName()
#         setFacesToZero()

# if __name__ == "__main__":
#     main()




# import streamlit as st
# from PIL import Image
# from identify import *
# from io import BytesIO
# import pandas as pd

# st.set_page_config(page_title="Attendance Taking App", page_icon=":clipboard:")

# def update_attendance(attendance_df, present_students):
#     for student in present_students:
#         if student in attendance_df.columns:
#             attendance_df.loc["Present", student] += 1
#     return attendance_df

# def main():
#     st.title("Attendance Taking App")

#     uploaded_file = st.file_uploader("Upload the class photo...", type=["jpg", "jpeg", "png"])

#     if uploaded_file is not None:
#         image_placeholder = st.empty()
#         recognizing_message = st.empty()

#         image_placeholder.image(uploaded_file, caption="Uploaded Class Photo.", use_column_width=True)
#         recognizing_message.write("Taking Attendance...")

#         present_students = faceRecognition(uploaded_file)

#         # Attendance Results Section
#         recognizing_message.empty()  
#         st.header("Attendance Results:")
        
#         if present_students:
#             st.write("Present Students:")
#             for student in present_students:
#                 st.write(f"- {student}")
#         else:
#             st.write("No students detected.")

#         # Update attendance
#         if st.button("Update Attendance"):
#             try:
#                 attendance_df = pd.read_excel("attendance.xlsx", index_col=0, engine="openpyxl")
#             except FileNotFoundError:
#                 # If file does not exist, create a new DataFrame
#                 attendance_df = pd.DataFrame(columns=["Present"], index=["Present"])
            
#             attendance_df = update_attendance(attendance_df, present_students)
#             attendance_df.to_excel("attendance.xlsx")
#             st.success("Attendance updated successfully.")

# if __name__ == "__main__":
#     main()
