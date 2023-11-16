import streamlit as st
import mysql.connector

# Connect to MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="March@142003",
    database="ResearchLabManagementSystem"
)

# Create a cursor object
cursor = conn.cursor()

# Streamlit code
st.title("Research Labs Management System")

# User authentication
user_type = st.radio("Select User Type", ["Student", "Teacher", "Lab Personnel"])

# Personalized greeting based on user type
if user_type == "Student":
    st.write("Hello Student! Please enter your login credentials:")
elif user_type == "Teacher":
    st.write("Hello Teacher! Please enter your login credentials:")
elif user_type == "Lab Personnel":
    st.write("Hello Lab Personnel! Please enter your login credentials:")

username = st.text_input("Enter Username:")
password = st.text_input("Enter Password", type="password")

# Function to authenticate user
# Function to authenticate user
# Function to authenticate user
# Function to authenticate user
def authenticate_user():
    if user_type == "Student":
        query = f"SELECT * FROM Student WHERE StudentName = '{username}' AND StudentID = '{password}'"
    elif user_type == "Teacher":
        query = f"SELECT * FROM Teacher WHERE TeacherName = '{username}' AND TeacherID = '{password}'"
    elif user_type == "Lab Personnel":
        query = f"SELECT * FROM LabPersonnel WHERE PersonnelName = '{username}' AND PersonnelID = '{password}'"

    cursor.execute(query)
    result = cursor.fetchone()
    return result is not None

# Authentication check
if st.button("Login"):
    if authenticate_user():
        st.success(f"Login successful! Welcome, {user_type}!")
        # Continue with the rest of the application
        # Include other functionalities and functions here
        if user_type == "Student":
            # Student view
            # View project proposals
            st.write("Your Project Proposals:")
            student_id = username  # Assuming student ID is the username
            student_proposals_query = f"SELECT * FROM ProjectProposal WHERE StudentID = '{student_id}';"
            cursor.execute(student_proposals_query)
            student_proposals = cursor.fetchall()
            for proposal in student_proposals:
                st.write(f"Proposal ID: {proposal[0]}, Title: {proposal[1]}, Description: {proposal[2]}")
            
        elif user_type == "Teacher":
            # Teacher view
            # Mark attendance
            st.write("Mark Attendance:")
            st.write("(Assuming 'AttendanceRecord' table structure)")
            teacher_id = username  # Assuming teacher ID is the username
            attendance_query = f"SELECT * FROM AttendanceRecord WHERE TeacherID = '{teacher_id}';"
            cursor.execute(attendance_query)
            attendance_records = cursor.fetchall()
            for record in attendance_records:
                st.write(f"Record ID: {record[0]}, Student ID: {record[7]}, Attendance Status: {record[-1]}")
            
            # Add or delete student
            st.write("Add or Delete Student:")
            st.write("(Assuming 'Student' table structure)")
            if st.button("Add Student"):
                # Add student functionality
                new_student_id = st.text_input("Enter New Student ID:")
                new_student_name = st.text_input("Enter New Student Name:")
                new_student_password = st.text_input("Enter New Student Password:", type="password")
                new_student_query = f"INSERT INTO Student (StudentID, StudentName, Password) VALUES ('{new_student_id}', '{new_student_name}', '{new_student_password}');"
                cursor.execute(new_student_query)
                conn.commit()
                st.success(f"Student with ID {new_student_id} added successfully!")

            if st.button("Delete Student"):
                # Delete student functionality
                delete_student_id = st.text_input("Enter Student ID to Delete:")
                delete_student_query = f"DELETE FROM Student WHERE StudentID = '{delete_student_id}';"
                cursor.execute(delete_student_query)
                conn.commit()
                st.success(f"Student with ID {delete_student_id} deleted successfully!")
            
            # Add stipend after marking completed status
            st.write("Add Stipend:")
            st.write("(Assuming 'stipend' and 'ProjectProposal' table structure)")
            if st.button("Add Stipend"):
                project_id_for_stipend = st.text_input("Enter Project ID:")
                stipend_amount = st.text_input("Enter Stipend Amount:")
                stipend_date = st.text_input("Enter Stipend Date:")
                add_stipend_query = f"INSERT INTO stipend (StipendAmount, StipendDate, StudentID, LabID) SELECT '{stipend_amount}', '{stipend_date}', StudentID, LabID FROM ProjectProposal WHERE ProposalID = '{project_id_for_stipend}';"
                cursor.execute(add_stipend_query)
                conn.commit()
                st.success(f"Stipend added successfully!")

    else:
        st.error("Invalid username or password. Please try again.")

# Close the database connection
conn.close()
