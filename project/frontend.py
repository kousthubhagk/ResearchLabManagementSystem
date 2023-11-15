import streamlit as st
import mysql.connector

# Connect to MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
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
def authenticate_user():
    if user_type == "Student":
        query = f"SELECT * FROM Student WHERE StudentID = '{username}' AND Password = '{password}'"
    elif user_type == "Teacher":
        query = f"SELECT * FROM Teacher WHERE TeacherID = '{username}' AND Password = '{password}'"
    elif user_type == "Lab Personnel":
        query = f"SELECT * FROM LabPersonnel WHERE PersonnelID = '{username}' AND Password = '{password}'"

    cursor.execute(query)
    result = cursor.fetchone()
    return result is not None

# Authentication check
if st.button("Login"):
    if authenticate_user():
        st.success(f"Login successful! Welcome, {user_type}!")
        # Continue with the rest of the application
        # Include other functionalities and functions here
    else:
        st.error("Invalid username or password. Please try again.")



user_type = st.radio("Select User Type", ["Student", "Teacher", "Lab Personnel"])
username = st.text_input("Enter Username:")
password = st.text_input("Enter Password", type="password")

# project approvals
# Button to trigger the approval status update
def authenticate_user():
    query = f"SELECT * FROM Teacher WHERE TeacherID = '{username}' AND Password = '{password}'"
    cursor.execute(query)
    result = cursor.fetchone()

    if result:
        teacher_role = result[2]  # Assuming TeacherRole is the third column in the Teacher table
        return teacher_role == 'Teacher' or teacher_role == 'Director'
    else:
        return False
    
def get_teacher_role(teacher_id):
    # Assuming 'TeacherRole' is the third column in the Teacher table
    query = f"SELECT TeacherRole FROM Teacher WHERE TeacherID = '{teacher_id}'"
    cursor.execute(query)
    result = cursor.fetchone()

    if result:
        return result[0]  # Return the TeacherRole
    else:
        return None  # Return None if the teacher is not found


# Authentication check
if st.button("Login"):
    if authenticate_user():
        st.success(f"Login successful! Welcome, {username}!")
        
        # Fetch pending project proposals for the teacher
        pending_proposals_query = f"SELECT * FROM ProjectProposal WHERE (TeacherApprovedStatus = 'not approved' OR DirectorApprovedStatus = 'not approved') AND ApprovedID = '{username}';"
        cursor.execute(pending_proposals_query)
        pending_proposals = cursor.fetchall()

        # Display pending project proposals
        if pending_proposals:
            st.write("Pending Project Proposals:")
            for proposal in pending_proposals:
                st.write(f"Proposal ID: {proposal[0]}, Title: {proposal[1]}, Description: {proposal[2]}")
                # Add buttons for approval and rejection (modify as needed)

                if user_type == "Teacher":
                    teacher_role = get_teacher_role(username)
                    if teacher_role == 'Teacher' and st.button(f"Approve Proposal ID {proposal[0]}"):
                        # Call the stored procedure for teacher approval
                        cursor.callproc("UpdateApprovalStatus", [proposal[0], 'approved', 'not approved', username])
                    elif teacher_role == 'Director':
                        st.warning("Directors cannot approve proposals.")

                if st.button(f"Approve Proposal ID {proposal[0]}"):
                    # Call the stored procedure or update query for approval
                    approver_id = proposal[7]  # Assuming the ApprovedID is in the 7th column
                    cursor.callproc("UpdateApprovalStatus", [proposal[0], 'approved', approver_id])
                if st.button(f"Reject Proposal ID {proposal[0]}"):
                    # Call the stored procedure or update query for rejection
                    approver_id = proposal[7]  # Assuming the ApprovedID is in the 7th column
                    cursor.callproc("UpdateApprovalStatus", [proposal[0], 'not approved', approver_id])
        else:
            st.write("No pending project proposals.")
    else:
        st.error("Invalid username or password. Please try again.")


# Close the database connection
conn.close()
