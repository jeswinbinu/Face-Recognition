# Face-Recognition 

This is a Streamlit web application for face recognition using a pre-trained YOLO (You Only Look Once) model and the DeepFace library. The app allows users to upload an image, detects faces, and performs face recognition to identify known faces.



## Quick Overview of Working

- **Face Detection**: The app uses the YOLO model to detect faces in uploaded images.
 
- **Face Extraction**: Crop and save the detected faces.

- **Face Recognition**: The DeepFace library is employed for face recognition. Known faces are saved in the 'known' folder, and unknown faces are saved in the 'unknown' folder.

- **User-friendly Interface**: The Streamlit app provides a user-friendly interface for easy interaction.


## Usage

1. Clone the repository:

   ```
   git clone https://github.com/jeswinbinu/Face-Recognition.git
   ```
2. Navigate to the directory:
    ```
    cd Face-Recognition
    ```

3. Install the required dependencies(in a virtual Environment):
    ```
    pip install -r requirements.txt
    ```

4. Run the Streamlit app:
    ``` 
    streamlit run streamlit_app.py
    ```

###### Acknowledgement: This repository is the deployed and simplified version of [this](https://github.com/sOR-o/Face-Recognition).


## License

This project is licensed under the [MIT License](LICENSE).




   
