import streamlit as st
from PIL import Image

from utils import recognize_slide

st.title("Hematology Slide Analyzer")

uploaded_file = st.file_uploader("Upload hematology slide image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Slide", use_column_width=True)

    if st.button("Analyze"):
        with st.spinner("Running EmatoGPT..."):
            result = recognize_slide(image)
        st.success("Recognition Result:")
        st.write(result)
else:
    st.info("Please upload an image of a hematology slide.")
