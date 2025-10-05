import streamlit as st
import json
import pandas as pd
from services.gemini_service import extract_invoice_data
from services.pdf_service import create_pdf, create_download_link

def render():
    st.header("📸 Extract Invoice Details using Gemini AI")

    uploaded_file = st.file_uploader(
        "Upload an Invoice (Image or PDF)",
        type=["png", "jpg", "jpeg", "pdf"]
    )

    if uploaded_file:
        st.image(uploaded_file, caption="🧾 Uploaded Invoice", use_container_width=True)

        if st.button("🔍 Extract Details"):
            with st.spinner("Analyzing invoice..."):
                prompt = (
                    "Extract key invoice details like vendor name, invoice number, "
                    "invoice date, line items, subtotal, tax, and total in clean JSON format."
                )

                result = extract_invoice_data(prompt, uploaded_file)

                if result:
                    try:
                        cleaned_result = (
                            result.replace("```json", "")
                            .replace("```", "")
                            .strip()
                        )

                        invoice_data = json.loads(cleaned_result)
                        st.success("✅ Extraction Successful!")

                        st.subheader("📄 Extracted Invoice Data")
                        st.json(invoice_data)

                        if "items" in invoice_data and isinstance(invoice_data["items"], list):
                            st.subheader("🧾 Line Items")
                            df = pd.DataFrame(invoice_data["items"])
                            st.dataframe(df, use_container_width=True)

                        pdf = create_pdf(invoice_data)
                        if pdf:
                            download_link = create_download_link(pdf, "invoice_summary.pdf")
                            st.markdown(download_link, unsafe_allow_html=True)

                    except json.JSONDecodeError:
                        st.warning("⚠️ Gemini response is not valid JSON. Here’s the raw output:")
                        st.code(result, language="json")

                    except Exception as e:
                        st.error(f"❌ Unexpected error: {str(e)}")

                else:
                    st.error("❌ No response received from Gemini. Please try again.")
