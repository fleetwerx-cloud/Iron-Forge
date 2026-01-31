import streamlit as st
import google.generativeai as genai

# 1. Setup the AI using the key you will add later
# This checks if the key exists to prevent crashing
try:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    model = genai.GenerativeModel('gemini-1.5-flash')
except:
    st.warning("We are setting up the API key, please wait...")

# 2. The App Design
st.title("Project Iron Forge")
st.write("Please input your data below for the project record.")

# 3. User Inputs
user_name = st.text_input("Name / ID")
user_input = st.text_area("Input Information")

# 4. The Submit Button
if st.button("Submit Data"):
    if user_name and user_input:
        try:
            # Process with AI
            response = model.generate_content(user_input)
            
            # Show the result to the user
            st.success("Data recorded successfully.")
            st.write("### AI Analysis:")
            st.write(response.text)
            
            # LOG THE DATA (This is how you get their input later)
            print(f"LOG_ENTRY::{user_name}::{user_input}")
            
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please fill in both fields.")
