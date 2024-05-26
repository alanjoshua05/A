import gspread
from oauth2client.service_account import ServiceAccountCredentials
import streamlit as st
from datetime import datetime, time
import json
from streamlit_option_menu import option_menu
import webbrowser
import sys
from io import StringIO

st.sidebar.title("Daily Quiz")
a = st.sidebar.selectbox("Week 1",['Day 1','Day 2','Day 3','Day 4','Day 5'])

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
    blocked_start_time = time(19,30)  # e.g., 12:00 AM 18:30
    blocked_end_time = time(23,00)    # e.g., 4:30 AM 23:00
    now = datetime.now().time()
    return blocked_start_time < now < blocked_end_time

current_date = datetime.now().date()

    
if a == 'Day 1':
    
    st.title('Daily quiz')
    st.subheader(f"Date : {data['Day_1']['Date']}")
# Get input from the user
    name = st.text_input('Enter Name')
    email = st.text_input('Enter your college mail id (ex: 23cb000@drngpit.ac.in)')
    email = email.strip()

    st.subheader("Questions")

    q1 = st.text_area(f"1){data['Day_1']['Question']}")


    if st.button("Submit",type='primary'):
        if "@drngpit.ac.in" not in email or len(email) != 21:
            st.error("Enter your college mail id correctly")
        elif is_blocked_time():
            st.error("Sorry, the quiz has been timed out.")
        else:
    
            # Update the sheet with the entered data
            sheet.append_row(["2024-05-17", name, email, q1])
            st.success("Added successfully")
            st.balloons()

if a == 'Day 2':
    
    st.title('Daily quiz')
    st.subheader(f"Date : {data['Day_2']['Date']}")
# Get input from the user
    name = st.text_input('Enter Name')
    email = st.text_input('Enter your college mail id (ex: 23cb000@drngpit.ac.in)')
    email = email.strip()

    st.subheader("Questions")

    q1 = st.text_area(f"1){data['Day_2']['Question']}")


    if st.button("Submit",type='primary'):
        if "@drngpit.ac.in" not in email or len(email) != 21:
            st.error("Enter your college mail id correctly")
        elif is_blocked_time():
            st.error("Sorry, the quiz has been timed out.")
        else:
    
            # Update the sheet with the entered data
            sheet.append_row(["2024-05-17", name, email, q1])
            st.success("Added successfully")
            st.balloons()

if a == 'Day 3':
    
    st.title('Daily quiz')
    st.subheader(f"Date : {data['Day_3']['Date']}")
# Get input from the user
    name = st.text_input('Enter Name')
    email = st.text_input('Enter your college mail id (ex: 23cb000@drngpit.ac.in)')
    email = email.strip()

    st.subheader("Questions")

    q1 = st.text_area(f"1){data['Day_3']['Question']}")


    if st.button("Submit",type='primary'):
        if "@drngpit.ac.in" not in email or len(email) != 21:
            st.error("Enter your college mail id correctly")
        elif is_blocked_time():
            st.error("Sorry, the quiz has been timed out.")
        else:
    
            # Update the sheet with the entered data
            sheet.append_row([data['Day_3']['Date'], name, email, q1])
            st.success("Added successfully")
            st.balloons()
