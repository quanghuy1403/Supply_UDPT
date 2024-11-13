import streamlit as st
from supplier_management import display_supplier_management
from order_management import display_order_management
from inventory_management import display_inventory_management
from logistics_management import display_logistics_management
from partner_management import display_partner_management
from product_management import display_product_management
from user_management import display_user_management
from reporting import display_reporting
from notifications import display_notifications

# Main App Navigation
st.sidebar.title("Main Navigation")
page = st.sidebar.selectbox("Select a page", [
    "Supplier Management",
    "Order Management",
    "Inventory Management",
    "Logistics Management",
    "Partner Management",
    "Product Management",
    "User and Permission Management",
    "Reporting and Analytics",
    "Notifications"
])

# Display the selected page
if page == "Supplier Management":
    display_supplier_management()
elif page == "Order Management":
    display_order_management()
elif page == "Inventory Management":
    display_inventory_management()
elif page == "Logistics Management":
    display_logistics_management()
elif page == "Partner Management":
    display_partner_management()
elif page == "Product Management":
    display_product_management()
elif page == "User and Permission Management":
    display_user_management()
elif page == "Reporting and Analytics":
    display_reporting()
elif page == "Notifications":
    display_notifications()
