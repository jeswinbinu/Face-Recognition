import streamlit as st
from PIL import Image
from identify import *
from io import BytesIO


st.sidebar.title("CSB Attendance")
uploaded_file = st.sidebar.file_uploader('Upload image', type=["jpg", "jpeg", "png"])
