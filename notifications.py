import streamlit as st

def display_notifications():
    st.title("Notifications and Alerts")
    sub_option = st.selectbox("Choose Notification Type", ["In-app Notifications", "Email/SMS Notifications"])

    if sub_option == "In-app Notifications":
        st.write("Notifying users about order status, inventory levels, etc.")

    elif sub_option == "Email/SMS Notifications":
        contact_method = st.selectbox("Contact Method", ["Email", "SMS"])
        recipient = st.text_input("Recipient")
        message = st.text_area("Message")
        if st.button("Send Notification"):
            st.success(f"{contact_method} notification sent to {recipient}")
