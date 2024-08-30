import streamlit as st
import requests

# Fetch username from the API
try:
    response = requests.get("http://localhost:8081/api/auth")
    if response.status_code == 200:
        data = response.json()
        if isinstance(data, list) and len(data) > 0:
            username = data[0].get('username', 'User')  # Extract username from the first item
        elif isinstance(data, dict):
            username = data.get('username', 'User')
        else:
            username = 'User'
    else:
        username = 'User'
        st.error(f"Failed to fetch username. Status code: {response.status_code}")
except requests.RequestException as e:
    username = 'User'
    st.error(f"Error connecting to the server: {str(e)}")

# Add logout button
logout_url = "http://localhost:8502"
st.markdown(
    f'<div style="position: absolute; top: 0.5rem; right: 1rem;"><a href="{logout_url}" target="_self"><button style="background-color: #f63366; color: white; border: none; border-radius: 4px; padding: 0.5rem 1rem; font-size: 1rem; cursor: pointer;">Logout</button></a></div>',
    unsafe_allow_html=True
)

# Add space after logout button
st.markdown("<br><br>", unsafe_allow_html=True)

# Display greeting with username
st.markdown(f"<h1 style='text-align: center; font-size: 3em;'>Hello there, {username}! 👋</h1>", unsafe_allow_html=True)

st.markdown("# Welcome to Expense Manager :dollar:")

cover_image_url = """
https://media.istockphoto.com/id/1383866726/photo/annual-budget-and-\
financial-planning-concept-with-manager-or-executive-cfo-crafting-or.jpg\
?s=2048x2048&w=is&k=20&c=iyhk1WbUWUo6921DgUs7NqVaC__qS8fgzZeJkqp6bnE=
"""

cover_image_path = "assets/expense_manager_cover.jpeg"

st.image(
    image = cover_image_path,
    caption = "Expense Manager",
)

st.markdown("***")
col11, col12, col13 = st.columns(3, gap='small')