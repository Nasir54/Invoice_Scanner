import streamlit as st
from pages import (
    login_page,
    register_page,
    extract_invoice_page,
    invoice_history_page,
    profile_page
)
from services.auth_service import authenticate_user

st.set_page_config(
    page_title="📄 Invoice Extractor using Gemini AI",
    page_icon=":money_with_wings:",
    layout="wide"
)

# Initialize session
if "user_id" not in st.session_state:
    st.session_state.user_id = None


def main():
    st.sidebar.title("🧭 Navigation")

    # ✅ If logged in
    if st.session_state.user_id:
        page = st.sidebar.radio("Go to", ["Extract Invoice", "Invoice History", "Profile"])
        st.sidebar.markdown("---")

        if st.sidebar.button("🚪 Logout"):
            st.session_state.user_id = None
            st.rerun()  # ✅ Updated

        if page == "Extract Invoice":
            extract_invoice_page.render()
        elif page == "Invoice History":
            invoice_history_page.render()
        elif page == "Profile":
            profile_page.render()

    # ✅ If NOT logged in
    else:
        page = st.sidebar.radio("Go to", ["Login", "Register"])
        st.sidebar.markdown("---")

        if page == "Login":
            login_page.render()
        elif page == "Register":
            register_page.render()


if __name__ == "__main__":
    main()
