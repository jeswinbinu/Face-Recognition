import streamlit as st
from PIL import Image
from identify2 import *
# 
st.set_page_config(page_title="Image Upload", page_icon=":image")

def get_list_of_subjects():
    return ['CD', 'AAD', 'CGIP', 'PY', 'IEFT']

subject_chosen = st.sidebar.selectbox('Select a subject:', get_list_of_subjects())

def main():
    st.title(f'{subject_chosen}')
    # sample_image_path = "./sample_image.jpg"
    # sample_image = Image.open(sample_image_path)

    # buf = BytesIO()
    # sample_image.save(buf, format="JPEG")
    # byte_im = buf.getvalue()

    # sample_image_name = "sample_image.jpg"
    # st.download_button(label="Download Sample Image", data=byte_im, file_name=sample_image_name, key="download_button")


    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image_placeholder = st.empty()
        recognizing_message = st.empty()

        image_placeholder.image(uploaded_file, caption="Uploaded Image.", use_column_width=True)
        recognizing_message.write("Recognizing...")
       
        total_faces = faceDetection(uploaded_file)
        names = faceRecognition(uploaded_file, subject_chosen)
        
        # Face Detection Results Section
        recognizing_message.empty()  
        st.header("Face Detection Results:")
        st.write(f"Total Faces Detected: {total_faces}")
        st.write(f"Total Recognized Faces: {getKnownFaces()}")
        st.write(f"Total Unrecognized Faces: {getUnknownFaces()}")
        
        
        # Absentees section
        st.header("Absentees: ")
        today_date = datetime.today().strftime('%d/%m/%Y')
        # current_directory = os.path.dirname(os.path.abspath(__file__))
        # # fr_directory = os.path.dir
        # csv_file_path = os.path.join(current_directory, 'attendance', f'{subject_chosen}.csv')
        attendance_directory = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'attendance')
        csv_file_path = os.path.join(attendance_directory, f'{subject_chosen}.csv')

        # Read the CSV file into a list of dictionaries
        with open(csv_file_path, 'r', newline='') as file:
            reader = csv.DictReader(file)
            rows = list(reader)
        absentees = [(row['Name'], row['Sl.No']) for row in rows if row[today_date] == 'A']

        # Display absentees
        for name, slno in absentees:
            st.write(f"Name: {name}, Roll Number: {slno}")

        # Names Section
        # if names:
        #     st.header("Names:")
        #     for name in names:
        #         st.write(f"- {name}")

        # Known Faces Section
        # known_names = getKnownName()
        # if known_names:
        #     st.header("Known Faces:")
        #     for name in known_names:
        #         known_image_path = f"./known/{name}.jpg"
        #         known_image = Image.open(known_image_path)
        #         st.image(known_image, caption=name, width=200)

        # Unknown Faces Section
        # st.header("Unknown Faces:")
        # if getUnknownFaces() == 0:
        #     st.write("None")
        # else:
        #     for i in range(getUnknownFaces()):
        #         unknown_image_path = f"./unknown/{i}.jpg"
        #         unknown_image = Image.open(unknown_image_path)
        #         st.image(unknown_image, caption=f"Unknown Face #{i + 1}", width=200)

        # Reset the known names and face counts
        setKnownName()
        setFacesToZero()


if __name__ == "__main__":
    main()

