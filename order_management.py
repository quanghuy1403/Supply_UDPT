import streamlit as st

def display_order_management():
    st.title("Order Management")
    sub_option = st.selectbox("Choose Action", ["Create New Order", "Update Order", "Track Order Status", "Order History"])

    if sub_option == "Create New Order":
        order_details = st.text_area("Order Details")
        quantity = st.number_input("Quantity", min_value=1)
        supplier_info = st.text_input("Supplier Information")
        if st.button("Create Order"):
            # Logic to create order
            st.success("Order created successfully!")

    elif sub_option == "Update Order":
        order_id = st.number_input("Enter Order ID", min_value=1)
        # Logic to update order
        st.info("Order updated!")

    elif sub_option == "Track Order Status":
        order_id = st.number_input("Enter Order ID", min_value=1)
        # Logic to display order status
        st.write(f"Order status for ID {order_id}")

    elif sub_option == "Order History":
        st.write("List of past orders")
