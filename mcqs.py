import streamlit as st
import google.generativeai as genai
import os

# Set your API key
os.environ["GOOGLE_API_KEY"] = "AIzaSyDp-zYuRkOt_mZmrJ9m409__mKJ9s4G-_c"
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

# Initialize Gemini Flash model
model = genai.GenerativeModel("gemini-1.5-flash")

st.title("MCQ Generator App")

# Dropdown for subject selection
subject = st.selectbox("Select a subject:", ["Physics", "Chemistry", "Biology", "Mathematics", "Computer Science" , "Graph Theory" , "Number theory"])

if st.button("Generate MCQs"):
    prompt = f"""
    Generate 3 multiple-choice questions for {subject}.
    Each question should have 4 options (A, B, C, D).
    Mark the correct answer clearly.
    Format example:
    Q1: Question text
    A) Option 1
    B) Option 2
    C) Option 3
    D) Option 4
    Answer: C
    """

    response = model.generate_content(prompt)

    st.subheader(f"MCQs for {subject}:")
    st.write(response.text)
