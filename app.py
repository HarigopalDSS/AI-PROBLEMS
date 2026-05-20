import streamlit as st

st.set_page_config(page_title="Media Platform Auth", page_icon="🎬", layout="centered")

st.title("Media Platform")
st.caption("Simple login and signup forms in Streamlit")

# In-memory user store for demo purposes.
if "users" not in st.session_state:
    st.session_state.users = {
        "demo@media.com": {
            "name": "Demo User",
            "password": "demo1234",
        }
    }

login_tab, signup_tab = st.tabs(["Login", "Sign Up"])

with login_tab:
    st.subheader("Login")
    with st.form("login_form"):
        login_email = st.text_input("Email", placeholder="you@example.com")
        login_password = st.text_input("Password", type="password")
        login_submit = st.form_submit_button("Login")

    if login_submit:
        if not login_email or not login_password:
            st.warning("Please enter both email and password.")
        else:
            user = st.session_state.users.get(login_email)
            if user and user["password"] == login_password:
                st.success(f"Welcome back, {user['name']}!")
            else:
                st.error("Invalid email or password.")

with signup_tab:
    st.subheader("Create an Account")
    with st.form("signup_form"):
        signup_name = st.text_input("Full Name", placeholder="Your full name")
        signup_email = st.text_input("Email", placeholder="you@example.com")
        signup_password = st.text_input("Password", type="password")
        confirm_password = st.text_input("Confirm Password", type="password")
        signup_submit = st.form_submit_button("Sign Up")

    if signup_submit:
        if not signup_name or not signup_email or not signup_password or not confirm_password:
            st.warning("Please fill all fields.")
        elif signup_email in st.session_state.users:
            st.error("An account with this email already exists.")
        elif len(signup_password) < 6:
            st.error("Password must be at least 6 characters.")
        elif signup_password != confirm_password:
            st.error("Passwords do not match.")
        else:
            st.session_state.users[signup_email] = {
                "name": signup_name,
                "password": signup_password,
            }
            st.success("Signup successful. You can now login from the Login tab.")
