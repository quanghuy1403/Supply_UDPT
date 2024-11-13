import streamlit as st

def display_product_management():
    st.title("Product Management")
    sub_option = st.selectbox("Choose Action", ["Add New Product", "Update Product Information", "Track Product Lifecycle", "Product Reports"])

    if sub_option == "Add New Product":
        product_name = st.text_input("Product Name")
        unit = st.text_input("Unit")
        cost = st.number_input("Cost", min_value=0.0)
        suppliers = st.text_area("Suppliers (comma separated)")
        if st.button("Add Product"):
            st.success("Product added successfully!")

    elif sub_option == "Update Product Information":
        product_id = st.number_input("Product ID", min_value=1)
        # Logic to update product information
        st.info("Product information updated!")

    elif sub_option == "Track Product Lifecycle":
        product_id = st.number_input("Product ID to Track", min_value=1)
        st.write("Track product lifecycle details")

    elif sub_option == "Product Reports":
        st.write("Generate reports on product consumption and demand forecasting")
