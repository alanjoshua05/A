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
    blocked_start_time = time(20,30)  # e.g., 2:00 AM 20:30
    blocked_end_time = time(20,00)    # e.g., 4:30 AM 23:00
    now = datetime.now().time()
    return blocked_start_time < now < blocked_end_time


# Streamlit app
current_date = datetime.now().date()
st.title('Daily quiz✍️')
st.write(current_date.strftime('%d/%m/%y'))

# Get input from the user
name = st.text_input('Enter Name')
email = st.text_input('Enter your college mail id (ex: 23cb000@drngpit.ac.in)')
email = email.strip()

st.subheader("Questions")

q1 = st.text_area(f"1){data['Question 1']}")


if st.button("Submit"):
    if "@drngpit.ac.in" not in email or len(email) > 21:
        st.error("Enter your college mail id correctly")
    elif is_blocked_time():
        st.error("Sorry, the quiz has been timed out.")
    else:
    
            # Update the sheet with the entered data
            sheet.append_row([current_date.strftime('%Y-%m-%d'), name, email, q1])
            st.success("Added successfully")
            st.balloons()
