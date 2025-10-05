# services/gemini_service.py

import os
import streamlit as st
from PIL import Image
from dotenv import load_dotenv
import google.generativeai as genai

# ✅ Load environment variables
load_dotenv()

# ✅ Configure Gemini API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# ✅ Load Gemini Vision Model
model = genai.GenerativeModel("gemini-2.5-pro")

def extract_invoice_data(prompt, uploaded_file):
    """
    Extract structured data from an uploaded invoice image using Gemini Vision API.
    """
    try:
        # ✅ Ensure uploaded_file is read as an image
        image = Image.open(uploaded_file)

        # ✅ Send both prompt + image to Gemini
        response = model.generate_content([prompt, image])

        # ✅ Handle valid response
        if response and hasattr(response, "text"):
            return response.text
        else:
            st.error("❌ No response from Gemini")
            return None

    except Exception as e:
        st.error(f"❌ Gemini error: {e}")
        return None
