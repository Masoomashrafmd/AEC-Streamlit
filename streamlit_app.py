import streamlit as st
from PIL import Image


#adding header and animation to it too
st.markdown("""
    <style>
    @keyframes color-change {
        0% {color: red;}
        25% {color: green;}
        50% {color: blue;}
        75% {color: purple;}
        100% {color: red;}
    }
    
    .animated-header {
        font-size: 3em;
        font-weight: bold;
        animation: color-change 4s infinite;
    }
    </style>
 
    <h1 class="animated-header">ForgeX</h1>
    """, unsafe_allow_html=True)

# It is like basket to collect image
uploaded_images = []

#adding title and 
st.markdown("""
    <style>
    .animated-title {
        font-size: 2.5em;
        font-weight: bold;
        animation: slideInLeft 2s ease-in-out;
    }

    @keyframes slideInLeft {
        0% {transform: translateX(-100%);}
        100% {transform: translateX(0);}
    }
    </style>
    
    <h5 class="animated-title">An auto LoRa Trainer Tool for Efficient and Easily Accessible Model Trainer</h5>
    """, unsafe_allow_html=True)

# Image uploader section
uploaded_files = st.file_uploader("Choose images", accept_multiple_files=True, type=["png", "jpg", "jpeg"])

if uploaded_files:
    for uploaded_file in uploaded_files:
        # Open the image using PIL
        img = Image.open(uploaded_file)
        uploaded_images.append(img)

    # Display all uploaded images
    st.subheader("Preview of Uploaded Images:")
    for img in uploaded_images:
        st.image(img, caption="Uploaded Image", use_column_width=True)

# Button to upload images to the backend (simulated)
if st.button("Upload Images"):
    # Simulating the upload process to backend
    # In a real application, you would upload the images to a server or cloud storage here
    # For example, using an API request to upload images

    # Display success message after "upload"
    st.success("Images successfully uploaded!")
