import streamlit as st
from services.auth_service import authenticate_user

def render():
    st.header("🔐 Login to Invoice Generator")

    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submit = st.form_submit_button("Login")

        if submit:
            if username and password:
                user_id = authenticate_user(username, password)
                if user_id:
                    st.session_state.user_id = user_id
                    st.success(f"✅ Welcome back, {username}!")
                    st.rerun()  # ✅ Updated for latest Streamlit version
                else:
                    st.error("❌ Invalid username or password")
            else:
                st.warning("⚠️ Please fill all fields")
