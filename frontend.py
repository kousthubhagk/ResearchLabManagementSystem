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

# Display events before user authentication
st.header("Upcoming Events in our University:")
events_query = "SELECT e.EventName, e.EventDate, l.LabName FROM Eventss e JOIN ResearchLab l ON e.LabID = l.LabID;"
cursor.execute(events_query)
events = cursor.fetchall()

if events:
    for event in events:
        st.write(f"Event: {event[0]}, Date: {event[1]}, Lab: {event[2]}")

# Display login heading
st.header("Login")

# User authentication
user_type = st.selectbox("Select User Type", ["Student", "Teacher", "Lab Personnel"])

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
            sidebar_option = st.sidebar.selectbox("Select Action", ["None", "Add Student", "Delete Student", "Update Student"])
            if sidebar_option == "Add Student":
                # Add student form
                st.sidebar.header("Add Student")
                new_student_id = st.sidebar.text_input("Enter Student ID:")
                new_student_name = st.sidebar.text_input("Enter Student Name:")
                new_student_lab_id = st.sidebar.text_input("Enter Lab ID:")
                
                if st.sidebar.button("Add"):
                    # Add student functionality
                    new_student_password = new_student_id  # Setting the password as the student ID
                    new_student_query = f"INSERT INTO Student (StudentID, StudentName, Password, LabID) VALUES ('{new_student_id}', '{new_student_name}', '{new_student_password}', '{new_student_lab_id}');"
                    cursor.execute(new_student_query)
                    conn.commit()
                    st.sidebar.success(f"Student with ID {new_student_id} added successfully!")

            elif sidebar_option == "Delete Student":
                # Delete student form
                st.sidebar.header("Delete Student")
                delete_student_id = st.sidebar.text_input("Enter Student ID to Delete:")
                
                if st.sidebar.button("Delete"):
                    # Delete student functionality
                    delete_student_query = f"DELETE FROM Student WHERE StudentID = '{delete_student_id}';"
                    cursor.execute(delete_student_query)
                    conn.commit()
                    st.sidebar.success(f"Student with ID {delete_student_id} deleted successfully!")

            elif sidebar_option == "Update Student":
                # Update student form
                st.sidebar.header("Update Student")
                update_student_id = st.sidebar.text_input("Enter Student ID to Update:")
                updated_name = st.sidebar.text_input("Enter Updated Student Name:")
                updated_lab_id = st.sidebar.text_input("Enter Updated Lab ID:")
                
                if st.sidebar.button("Update"):
                    # Update student functionality
                    update_student_query = f"UPDATE Student SET StudentName = '{updated_name}', LabID = '{updated_lab_id}' WHERE StudentID = '{update_student_id}';"
                    cursor.execute(update_student_query)
                    conn.commit()
                    st.sidebar.success(f"Student with ID {update_student_id} updated successfully!")

    else:
        st.error("Invalid username or password. Please try again.")

# Close the database connection
conn.close()
