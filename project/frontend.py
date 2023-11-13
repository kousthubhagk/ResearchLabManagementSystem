import streamlit as st
import mysql.connector

# Connect to MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Keerthu@123",
    database="ResearchLabManagementSystem"
)

# Create a cursor object
cursor = conn.cursor()

# Streamlit code
st.title("Research Labs Management System")

# Example query to retrieve student names
cursor.execute("SELECT StudentName FROM Student;")
student = cursor.fetchall()

# Display student names in Streamlit
st.write("Student Names:")
for studen in student:
    st.write(studen[0])

# Close the database connection
conn.close()
