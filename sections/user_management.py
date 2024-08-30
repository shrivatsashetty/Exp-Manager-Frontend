import streamlit as st
import requests

st.markdown("# User Management :bust_in_silhouette:")

# Initialize session state
if 'show_form' not in st.session_state:
    st.session_state.show_form = True

if 'user_added' not in st.session_state:
    st.session_state.user_added = False

def reset_form():
    st.session_state.show_form = True
    st.session_state.user_added = False

def submit_form(username, email, role, age, gender):
    user = {
        "username": username,
        "email": email,
        "role": role,
        "age": age,
        "gender": gender
    }
    try:
        response = requests.post("http://localhost:8083/api/users", json=user)
        if response.status_code == 200:
            st.session_state.show_form = False
            st.session_state.user_added = True
            st.session_state.new_user = user
            st.rerun()
        else:
            st.error(f'Error adding user: {response.text}', icon="❌")
    except requests.RequestException as e:
        st.error(f'Error connecting to server: {str(e)}', icon="❌")

if st.session_state.show_form:
    with st.form(key="_user_form", clear_on_submit=True):
        username = st.text_input(label="Enter Username", placeholder="ex: user123")
        email = st.text_input(label="Enter Email", placeholder="ex: user@example.com")
        role = st.text_input(label="Enter Occupation", placeholder="ex: admin")
        age = st.number_input(label="Enter Age", min_value=0, max_value=120, step=1)
        gender = st.selectbox(label="Select Gender", options=["Male", "Female"])

        if st.form_submit_button("Submit", type='primary'):
            if username and email and role and age and gender:
                submit_form(username, email, role, age, gender)
            else:
                st.warning("Please fill in all fields", icon="⚠️")

if st.session_state.user_added:
    st.success('User Added Successfully', icon="✅")
    
    st.markdown("""
    <style>
    .user-card {
        background-color: #f0f2f6;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .user-card h3 {
        color: #0e1117;
        margin-bottom: 10px;
    }
    .user-card p {
        margin: 5px 0;
    }
    .user-icon {
        font-size: 100px;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown('<div class="user-icon">👤</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="user-card">
            <h3>User Details</h3>
            <p><strong>Username:</strong> {st.session_state.new_user.get('username')}</p>
            <p><strong>Email:</strong> {st.session_state.new_user.get('email')}</p>
            <p><strong>Role:</strong> {st.session_state.new_user.get('role')}</p>
            <p><strong>Age:</strong> {st.session_state.new_user.get('age')}</p>
            <p><strong>Gender:</strong> {st.session_state.new_user.get('gender')}</p>
        </div>
        """, unsafe_allow_html=True)
    
    if st.button("Change  User"):
        reset_form()