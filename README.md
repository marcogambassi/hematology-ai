# Hematology AI Demo

This repository contains a simple Streamlit application that allows users to
upload hematology slide images for analysis.

The recognition step relies on **EmatoGPT**, a GPT-based model for hematology
image interpretation. The application sends uploaded slide images to EmatoGPT
through the OpenAI API.

## Setup

Install dependencies with:

```bash
pip install -r requirements.txt
```

## Running the App

Start the Streamlit app using:

```bash
streamlit run app.py
```

Set the ``OPENAI_API_KEY`` environment variable before running the app. Upload a
slide image in JPEG or PNG format and click **Analyze** to send it to EmatoGPT.
