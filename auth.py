import streamlit as st
from supabase_client import get_supabase_client

def login():
    st.subheader("Login to BrandBasket")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        supabase = get_supabase_client()
        res = supabase.auth.sign_in_with_password({"email": email, "password": password})
        if res and res.user:
            st.session_state.user = res.user
            st.success(f"Welcome back, {email}!")
        else:
            st.error("Login failed. Check your credentials.")

def signup():
    st.subheader("Sign up for BrandBasket")
    email = st.text_input("Email", key="signup_email")
    password = st.text_input("Password", type="password", key="signup_password")
    if st.button("Sign Up"):
        supabase = get_supabase_client()
        res = supabase.auth.sign_up({"email": email, "password": password})
        if res and res.user:
            st.session_state.user = res.user
            st.success("Signup successful. Please check your email to verify.")
        else:
            st.error("Signup failed. Try again later.")

def logout():
    st.session_state.user = None
    st.success("Logged out successfully.")
