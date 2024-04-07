import gspread
from oauth2client.service_account import ServiceAccountCredentials
import streamlit as st
from datetime import datetime, time
import json

scopes = ['https://www.googleapis.com/auth/spreadsheets',
          "https://www.googleapis.com/auth/drive"]

credentials = ServiceAccountCredentials.from_json_keyfile_name('data-419313-295934c65ef4.json', scopes)
client = gspread.authorize(credentials)

# Open the desired sheet
sheet = client.open("FirstSheet").sheet1

with open('question.json','r') as file:
    json_data = file.read()

    # Parse the JSON data
    data = json.loads(json_data)


def is_blocked_time():
    blocked_start_time = time(21, 0)  # e.g., 5:00 PM
    blocked_end_time = time(21, 0)    # e.g., 9:00 PM
    now = datetime.now().time()
    return blocked_start_time < now < blocked_end_time


# Streamlit app
st.title('Daily quiz')

# Get input from the user
name = st.text_input('Enter Name')
email = st.text_input('Enter your college id')

st.subheader("Questions")
q2 = st.radio(f"1){data['Question 1']}", ["hello", "hey"], index=None)
q1 = st.text_area(f"2){data['Question 2']}")
current_date = datetime.now().date()


if "@drngpit.ac.in" not in email or len(email) > 21:
    st.error("Enter your college id or ensure the id doesn't have empty space at the end")
elif is_blocked_time():
        st.error("Sorry, the quiz has been timed out.")

else:
    if st.button("Submit"):
            # Update the sheet with the entered data
            sheet.append_row([current_date.strftime('%Y-%m-%d'), name, email, q2, q1])
            st.success("Added successfully")
            st.balloons()
