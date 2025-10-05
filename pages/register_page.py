import streamlit as st
from services.auth_service import create_user

def render():
    st.header("🧾 Register New Account")

    with st.form("register_form"):
        username = st.text_input("Username")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        submit = st.form_submit_button("Register")

        if submit:
            if username and email and password:
                success, msg = create_user(username, password, email)
                if success:
                    st.success(msg)
                else:
                    st.error(msg)
            else:
                st.warning("⚠️ Please fill all fields")
