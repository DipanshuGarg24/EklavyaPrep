#  is page se transfer hoke quiz wale page pr jana hai right 

import streamlit as st 
from google import genai
import json
import os

st.title("Eklavya Prep")



def genrate_Quiz(subject,num_questions,difficulty):
    prompt = f"""
You are a quiz generation AI. Generate a quiz based on the provided subject/exam, number of questions, and difficulty level.
Subject: {subject}
Number of Questions: {num_questions}
Difficulty Level: {difficulty}
Type: MCQ (Multiple Choice Questions)
Generate a list of questions with options and the correct answer.
Format (as a Python dict in JSON string form):

{{
    "subject": "{subject}",
    "num_questions": {num_questions},
    "difficulty": "{difficulty}",
    "questions": [
        ["Question 1", "Option A", "Option B", "Option C", "Option D", "Correct Answer"],
        ["Question 2", "Option A", "Option B", "Option C", "Option D", "Correct Answer"]
        // ... more questions
    ]
}}
Only output the JSON string, nothing else.
"""
    client = genai.Client(api_key="AIzaSyCuuJKwu8krjaoaJ5jjExBYIQj2tDRgNjs")

    response = client.models.generate_content(
        model="gemini-2.0-flash", contents=prompt
    )
    # json_response = json.loads(response.text)
    str_response = response.text.removeprefix('```json\n').removesuffix('\n```')
    data = json.loads(str_response)
    return data
    # use the gemini api or open ai to get the data 


#  here the quiz genration will happen 
#  lets create a form to get the data like get the subject / exam name and the number of question / difficulty level 
with st.form("quiz_form"):
    subject = st.text_input("Enter the subject or exam name:")
    num_questions = st.number_input("Number of questions:", min_value=1, max_value=100, value=10)
    difficulty = st.selectbox("Select difficulty level:", ["Easy", "Medium", "Hard"])
    
    submit_button = st.form_submit_button("Generate Quiz")

if submit_button:
    # here we will genrate the quiz but will show the loading widget 
    with st.spinner("Generating quiz..."):
        # Simulate quiz generation

        #  here get the data from the LLM we can use the llm in the backend

        # Display the generated quiz
        quiz = genrate_Quiz(subject, num_questions, difficulty)
        st.success("Quiz generated successfully!")
        st.session_state.quiz = quiz  # Store the quiz in session state
        st.switch_page("pages/quiz.py")  # Set the page to quiz
