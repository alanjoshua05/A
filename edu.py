import gspread
from oauth2client.service_account import ServiceAccountCredentials
import streamlit as st
from datetime import datetime, time
import json
import time

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

def display_clock():
    while True:
        # Get current time
        current_time = datetime.datetime.now()
        
        # Format the time as HH:MM:SS
        formatted_time = current_time.strftime("%H:%M:%S")
        
        # Print the time
        st.write("Current time:", formatted_time)
        
        # Wait for 1 second before updating the time
        time.sleep(1)

def is_blocked_time():
    blocked_start_time = time(17, 0)  # e.g., 5:00 PM
    blocked_end_time = time(5, 0)    # e.g., 9:00 PM
    now = datetime.now().time()
    return blocked_start_time < now < blocked_end_time


# Streamlit app
current_date = datetime.now().date()
st.title('Daily quiz')
st.write(current_date.strftime('%d/%m/%y'))
display_clock()
# Get input from the user
name = st.text_input('Enter Name')
email = st.text_input('Enter your college mail id (ex: 23cb000@drngpit.ac.in)')
email = email.strip()

st.subheader("Questions")

q1 = st.text_area(f"1){data['Question 1']}")



if "@drngpit.ac.in" not in email or len(email) > 21:
    st.error("Enter your college id correctly to open 'Submit' button")
elif is_blocked_time():
        st.error("Sorry, the quiz has been timed out.")

else:
    if st.button("Submit"):
            # Update the sheet with the entered data
            sheet.append_row([current_date.strftime('%Y-%m-%d'), name, email, q1])
            st.success("Added successfully")
            st.balloons()
