import streamlit as st
import google.generativeai as genai

# Load Gemini API Key from secrets or input manually
GEMINI_API_KEY = "AIzaSyDjWyM8ujJgGzVds_BEZ1s9TnN4UILTKeM"  # Replace with your actual key
genai.configure(api_key=GEMINI_API_KEY)

# Function to get response from Gemini
def get_gemini_response(prompt):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)
    return response.text

# Streamlit UI
st.title("💬 Chat with Google's Gemini AI")
st.write("Enter your prompt below and get responses from Gemini AI!")

user_input = st.text_area("Enter your query:", "")

if st.button("Generate Response"):
    if user_input:
        response = get_gemini_response(user_input)
        st.subheader("Response:")
        st.write(response)
    else:
        st.warning("Please enter a query first!")
