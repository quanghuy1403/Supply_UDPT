import streamlit as st

def display_logistics_management():
    st.title("Logistics Management")
    sub_option = st.selectbox("Choose Action", ["Track Transport Vehicles", "Dispatch Coordination", "Real-time Shipping Tracking", "Delay Notifications"])

    if sub_option == "Track Transport Vehicles":
        vehicle_id = st.text_input("Vehicle ID")
        schedule = st.date_input("Schedule Date")
        driver_info = st.text_input("Driver Information")
        if st.button("Add Vehicle"):
            st.success("Vehicle added and tracked successfully!")

    elif sub_option == "Dispatch Coordination":
        delivery_schedule = st.date_input("Delivery Schedule")
        location = st.text_input("Delivery Location")
        if st.button("Schedule Delivery"):
            st.success("Delivery scheduled successfully!")

    elif sub_option == "Real-time Shipping Tracking":
        order_id = st.number_input("Order ID", min_value=1)
        st.write(f"Tracking order {order_id} via GPS...")

    elif sub_option == "Delay Notifications":
        order_id = st.number_input("Order ID for Delay Notification", min_value=1)
        delay_reason = st.text_area("Reason for Delay")
        if st.button("Notify Delay"):
            st.warning("Delay notification sent!")
