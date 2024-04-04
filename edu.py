import gspread
from oauth2client.service_account import ServiceAccountCredentials
import streamlit as st

scopes = ['https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive"]

credentials = ServiceAccountCredentials.from_json_keyfile_name('data-419313-295934c65ef4.json', scopes)
client = gspread.authorize(credentials)

# Open the desired sheet
sheet = client.open("FirstSheet").sheet1

# Streamlit app
st.title("hi")
a = st.text_input("Enter your name")
b = st.number_input("Your age")

if st.button("Submit"):
    # Update the sheet with the entered name
    sheet.append_row([a,b])
    st.success("Added")
