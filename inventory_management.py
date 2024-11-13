import streamlit as st

def display_inventory_management():
    st.title("Inventory Management")
    sub_option = st.selectbox("Choose Action", ["Stock In", "Stock Out", "Update Stock Quantity", "Track Products in Inventory", "Inventory Reports"])

    if sub_option == "Stock In":
        product_name = st.text_input("Product Name")
        quantity = st.number_input("Quantity", min_value=1)
        if st.button("Add to Stock"):
            # Logic to add stock
            st.success(f"Added {quantity} units of {product_name} to inventory!")

    elif sub_option == "Stock Out":
        product_name = st.text_input("Product Name")
        quantity = st.number_input("Quantity", min_value=1)
        if st.button("Release from Stock"):
            # Logic to release stock
            st.warning(f"Released {quantity} units of {product_name} from inventory.")

    elif sub_option == "Update Stock Quantity":
        product_name = st.text_input("Product Name")
        new_quantity = st.number_input("New Quantity", min_value=0)
        if st.button("Update Quantity"):
            # Logic to update stock quantity
            st.info(f"Updated stock quantity of {product_name} to {new_quantity}.")

    elif sub_option == "Track Products in Inventory":
        st.write("Tracking products by batch, expiration date, etc.")

    elif sub_option == "Inventory Reports":
        st.write("Generate periodic inventory reports")
