import streamlit as st

def display_reporting():
    st.title("Reporting and Analytics")
    sub_option = st.selectbox("Choose Report", ["Order Summary Reports", "Shipping Cost Analysis", "Inventory Performance Reports"])

    if sub_option == "Order Summary Reports":
        st.write("Summary of order quantities and statuses")

    elif sub_option == "Shipping Cost Analysis":
        st.write("Analysis of shipping costs for optimization")

    elif sub_option == "Inventory Performance Reports":
        st.write("Report on inventory storage efficiency and stock turnover")
