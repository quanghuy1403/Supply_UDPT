import streamlit as st

def display_supplier_management():
    st.title("Supplier Management")
    sub_option = st.selectbox("Choose Action", ["Add New Supplier", "Update Supplier Information", "Delete Supplier", "Search and Filter Suppliers"])

    if sub_option == "Add New Supplier":
        supplier_name = st.text_input("Supplier Name")
        address = st.text_input("Address")
        contact_details = st.text_input("Contact Details")
        products = st.text_input("Supplied Products")
        if st.button("Add Supplier"):
            # Logic to add supplier
            st.success("Supplier added successfully!")

    elif sub_option == "Update Supplier Information":
        supplier_id = st.number_input("Enter Supplier ID", min_value=1)
        # Logic to update supplier information
        st.info("Supplier information updated!")

    elif sub_option == "Delete Supplier":
        supplier_id = st.number_input("Enter Supplier ID", min_value=1)
        if st.button("Delete Supplier"):
            # Logic to delete supplier
            st.warning("Supplier deleted successfully!")

    elif sub_option == "Search and Filter Suppliers":
        search_term = st.text_input("Search by Name, Product, or Location")
        # Logic to filter and display suppliers
        st.write("Search results for suppliers")
