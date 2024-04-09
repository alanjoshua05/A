import gspread
from oauth2client.service_account import ServiceAccountCredentials
import streamlit as st
from datetime import datetime, time
import json
from streamlit_option_menu import option_menu
import webbrowser
import sys
from io import StringIO

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

def python():
    st.title('Python IDE')

# Define initial code

    initial_code = '''print("Hello World")'''

# Display the code editor
    code = st.text_area(f"1){data['Code question']}", value=initial_code, height=300)

# Button to execute the code
    if st.button('Run'):
    # Redirect stdout to capture output
        output_area = st.empty()
        stdout = sys.stdout
        sys.stdout = StringIO()
    
    # Execute the code
        try:
            exec(code)
            output_value = sys.stdout.getvalue()
            output_area.write(output_value)
        except Exception as e:
            st.error(f"An error occurred: {e}")
    
    # Restore stdout
        sys.stdout = stdout


def is_blocked_time():
    blocked_start_time = time(19,30)  # e.g., 12:00 AM 18:30
    blocked_end_time = time(23,00)    # e.g., 4:30 AM 23:00
    now = datetime.now().time()
    return blocked_start_time < now < blocked_end_time

current_date = datetime.now().date()
# Streamlit app
with st.sidebar:
     selected = option_menu(
          menu_title="1st Year CSBS",
          options=["Daily quiz","Coding practice","PYQs"]
     )
if selected == "Daily quiz":
    
    st.title('Daily quiz')
    st.write(current_date.strftime('%d/%m/%y'))

# Get input from the user
    name = st.text_input('Enter Name')
    email = st.text_input('Enter your college mail id (ex: 23cb000@drngpit.ac.in)')
    email = email.strip()

    st.subheader("Questions")

    q1 = st.text_area(f"1){data['Question 1']}")


    if st.button("Submit",type='primary'):
        if "@drngpit.ac.in" not in email or len(email) > 21:
            st.error("Enter your college mail id correctly")
        elif is_blocked_time():
            st.error("Sorry, the quiz has been timed out.")
        else:
    
            # Update the sheet with the entered data
            sheet.append_row([current_date.strftime('%Y-%m-%d'), name, email, q1])
            st.success("Added successfully")
            st.balloons()

if selected == "PYQs":
    st.title("Previous questions")
    st.subheader("Internal 1")
    if st.button('Engineering Economics with Applications'):
        webbrowser.open("https://drive.google.com/file/d/1J8ZWpcczv39NRvD1T-SY7K1LubqymIBl/view")
    # if st.button('Python Programming'):
    #     webbrowser.open("#")
    if st.button('Technical English'):
        webbrowser.open("https://drive.google.com/file/d/1JT4JYF2w0gFV5DgUGyQJzGqC3j4rVZfs/view?usp=sharing")
    # if st.button('Linear Algebra'):
    #     webbrowser.open("#")
    # if st.button('Physics for Information Science'):
    #     webbrowser.open("#")
    if st.button('Digital Principles and System Design'):
        webbrowser.open("https://drive.google.com/file/d/1JJoTvviMBcwVmb2IZt1tPbQpSMYOlkCw/view?usp=sharing")

if selected=="Coding practice":
    python()
