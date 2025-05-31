import streamlit as st

#  now this page will get the data quiz data 
# and then render it to the page basically making a whole quiz on the Go


# okay so i will display the optin in the select box type of thing  

#  this data can be fetched through the steamlit session state 
# # Quiz = {
#     "subject": "GATE CSE",
#     "num_questions": 2,
#     "difficulty": "Hard",
#     "questions": [["what is the capital of India?", "Delhi", "Mumbai", "Kolkata", "Chennai", "Delhi"],["What is the capital of USA?", "New York", "Washington D.C.", "Los Angeles", "Chicago", "Washington D.C."]],
# }
Quiz = st.session_state.get("quiz", None)
if Quiz is None:
    st.error("No quiz data found. Please generate a quiz first.")
    st.stop()  # Stop further execution if no quiz data is found
#  lets display the quiz data 
st.title("Quiz Data")
st.write("Subject/Exam:", Quiz["subject"])
st.write("Number of Questions:", Quiz["num_questions"])
st.write("Difficulty Level:", Quiz["difficulty"])
# Display the questions
choosen = [None]*Quiz["num_questions"]
for i, question in enumerate(Quiz["questions"]):
    st.write(f"Question {i + 1}: {question[0]}")
    options = question[1:-1]  # Exclude the correct answer from options
    correct_answer = question[-1]
    # Display options as radio buttons
    choosen[i] = st.radio(f"Select an option for Question {i + 1}:", options, key=f"q{i}")


# st.write("Please select the correct answer for each question.")
if st.button("Submit",type="primary",use_container_width=True):
    score = 0
    for i, question in enumerate(Quiz["questions"]):
        if choosen[i] == question[-1]:
            score += 1
    st.success(f"Your score is: {score}/{Quiz['num_questions']}")
    
    # Display correct answers
    st.write("Correct Answers:")
    for i, question in enumerate(Quiz["questions"]):
        st.write(f"Question {i + 1}: {question[-1]}")
