import streamlit as st

def display_partner_management():
    st.title("Partner Management")
    sub_option = st.selectbox("Choose Action", ["Add New Partner", "Contract Management", "Track Partner Performance"])

    if sub_option == "Add New Partner":
        partner_name = st.text_input("Partner Name")
        partner_type = st.selectbox("Type", ["Transport Company", "Insurance Provider", "Bank"])
        if st.button("Add Partner"):
            st.success("Partner added successfully!")

    elif sub_option == "Contract Management":
        partner_id = st.number_input("Enter Partner ID", min_value=1)
        contract_terms = st.text_area("Contract Terms")
        if st.button("Update Contract"):
            st.info("Contract terms updated!")

    elif sub_option == "Track Partner Performance":
        partner_id = st.number_input("Enter Partner ID", min_value=1)
        performance_rating = st.slider("Performance Rating", 1, 5)
        if st.button("Rate Partner"):
            st.success("Partner performance rated successfully!")
