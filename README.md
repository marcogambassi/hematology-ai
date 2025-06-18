diff --git a/README.md b/README.md
index a9f42b4e1991c2a67d373d0616b0ff14ddc62fe2..4ffbde5d3bf1b51dcf37e8fa83f6c4b3a6410b3e 100644
--- a/README.md
+++ b/README.md
@@ -1 +1,27 @@
-# Placeholder for README.md
+# Hematology AI Demo
+
+This repository contains a simple Streamlit application that allows users to
+upload hematology slide images for analysis.
+
+The recognition step relies on **EmatoGPT**, a GPT-based model for hematology
+image interpretation. The application sends uploaded slide images to EmatoGPT
+through the OpenAI API.
+
+## Setup
+
+Install dependencies with:
+
+```bash
+pip install -r requirements.txt
+```
+
+## Running the App
+
+Start the Streamlit app using:
+
+```bash
+streamlit run app.py
+```
+
+Set the ``OPENAI_API_KEY`` environment variable before running the app. Upload a
+slide image in JPEG or PNG format and click **Analyze** to send it to EmatoGPT.

