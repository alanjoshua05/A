import gspread
from oauth2client.service_account import ServiceAccountCredentials
import streamlit as st
from datetime import datetime, time

scopes = ['https://www.googleapis.com/auth/spreadsheets',
          "https://www.googleapis.com/auth/drive"]

credentials = ServiceAccountCredentials.from_json_keyfile_name('data-419313-295934c65ef4.json', scopes)
client = gspread.authorize(credentials)

# Open the desired sheet
sheet = client.open("FirstSheet").sheet1

def is_blocked_time():
    blocked_start_time = time(21, 0)  # e.g., 5:00 PM
    blocked_end_time = time(21, 0)    # e.g., 9:00 PM
    now = datetime.now().time()
    return blocked_start_time < now < blocked_end_time


# Streamlit app
st.title('Daily quiz')

# Get input from the user
name = st.text_input('Enter Name')
email = st.text_input('Enter your college Mail id (ex 23cb000@drngpit.ac.in)')

st.subheader("Questions")
q2 = st.radio("1)hi", ["hello", "hey"], index=None)
q1 = st.text_area("2)how are you?")
current_date = datetime.now().date()


if email[7:] != "@drngpit.ac.in" or len(email) > 21:
    st.error("Enter your college id or ensure the id doesn't have empty space at the end")
elif is_blocked_time():
        st.error("Sorry, the quiz has been timed out.")

else:
    if st.button("Submit"):
            # Update the sheet with the entered data
            sheet.append_row([current_date.strftime('%Y-%m-%d'), name, email, q2, q1])
            st.success("Added successfully")
            st.balloons()
