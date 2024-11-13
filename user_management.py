import streamlit as st

def display_user_management():
    st.title("User and Permission Management")
    sub_option = st.selectbox("Choose Action", ["User Registration and Login", "Role-based Access Control", "User Activity Tracking", "Security Alerts and Warnings"])

    if sub_option == "User Registration and Login":
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        role = st.selectbox("Role", ["Manager", "Warehouse Staff", "Coordinator"])
        if st.button("Register User"):
            st.success("User registered successfully!")

    elif sub_option == "Role-based Access Control":
        user_id = st.number_input("User ID", min_value=1)
        new_role = st.selectbox("New Role", ["Manager", "Warehouse Staff", "Coordinator"])
        if st.button("Update Role"):
            st.success("User role updated!")

    elif sub_option == "User Activity Tracking":
        st.write("Tracking user activity within the system")

    elif sub_option == "Security Alerts and Warnings":
        st.write("Displaying security alerts and suspicious activity logs")
