import streamlit as st
import mysql.connector

# Connect to MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="March@142003",
    database="RLMS"
)

# Create a cursor object
cursor = conn.cursor()

# Check if session state is already set, if not, initialize it
if 'session_state' not in st.session_state:
    st.session_state.session_state_initialized = False

# State variables
@st.cache(allow_output_mutation=True, hash_funcs={"_thread.RLock": lambda _: None})
def init():
    return {
        "is_logged_in": False,
        "user_type": None,
        "username": None,
        "password": None,
        "lab_id": None  # Initialize password here
    }

state = init()

# Streamlit code
st.title("Welcome to the Research Labs at PES University")

# Display events
st.header("Stay Tuned for These Events:")
events_query = "SELECT e.EventName, e.EventDate, l.LabName FROM Eventss e JOIN ResearchLab l ON e.LabID = l.LabID;"
cursor.execute(events_query)
events = cursor.fetchall()

if events:
    for event in events:
        st.write(f"Event: {event[0]}, Date: {event[1]}, Lab: {event[2]}")

# Display projects
st.header("Projects:")
projects_query = "SELECT p.ProjectName, l.LabName FROM Project p JOIN ResearchLab l ON p.LabID = l.LabID;"
cursor.execute(projects_query)
projects = cursor.fetchall()

if projects:
    for project in projects:
        st.write(f"Project: {project[0]}, Lab: {project[1]}")

    # Display average stipend
    average_stipend_query = "SELECT AVG(StipendAmount) FROM Stipend;"
    cursor.execute(average_stipend_query)
    average_stipend = cursor.fetchone()[0]

# Display incentives heading
st.header("Incentives")

# Display average stipend
st.write(f"Average Stipend: {average_stipend:.2f}")

# Display project with max stipend
max_stipend_query = "SELECT p.ProjectName, SUM(s.StipendAmount) as TotalStipend FROM Project p JOIN Stipend s ON p.StudentID = s.StudentID AND p.LabID = s.LabID GROUP BY p.ProjectName ORDER BY TotalStipend DESC LIMIT 1;"
cursor.execute(max_stipend_query)
max_stipend = cursor.fetchone()

if max_stipend:
    st.write(f"Project with Max Stipend: {max_stipend[0]}, Total Amount: {max_stipend[1]}")

# Display login heading
st.header("Login")

# User authentication
if not state["is_logged_in"]:
    user_type = st.selectbox("Select User Type", ["Student", "Teacher", "Lab Personnel"])

    # Personalized greeting based on user type
    if user_type == "Student":
        st.write(f"Hello Student! Please enter your login credentials:")
        state["username"] = st.text_input("Enter Username:")
        state["password"] = st.text_input("Enter Password", type="password")

    elif user_type == "Teacher":
        st.write("Hello Teacher! Please enter your login credentials:")
        state["username"] = st.text_input("Enter Username:")
        state["password"] = st.text_input("Enter Password", type="password")

    elif user_type == "Lab Personnel":
        st.write("Hello Lab Personnel! Please enter your login credentials:")
        state["username"] = st.text_input("Enter Username:")
        state["password"] = st.text_input("Enter Password", type="password")

    # Function to authenticate user
    def authenticate_user():
        if user_type == "Student":
            query = f"SELECT * FROM Student WHERE StudentName = '{state['username']}' AND StudentID = '{state['password']}'"
        elif user_type == "Teacher":
            query = f"SELECT * FROM Teacher WHERE TeacherName = '{state['username']}' AND TeacherID = '{state['password']}'"
        elif user_type == "Lab Personnel":
            query = f"SELECT * FROM LabPersonnel WHERE PersonnelName = '{state['username']}' AND PersonnelID = '{state['password']}'"

        cursor.execute(query)
        result = cursor.fetchone()
        return result is not None

    # Authentication check
    if st.button("Login"):
        if authenticate_user():
            state["is_logged_in"] = True
            state["user_type"] = user_type
            st.success(f"Login successful! Welcome, {state['username']}!")

# Continue with the rest of the application for logged-in users
if state["is_logged_in"]:
    # Option to propose a project idea for students
    if state["user_type"] == "Student":
        with st.form(key="project_proposal_form"):
            project_title = st.text_input("Enter Project Title:")
            project_description = st.text_area("Enter Project Description:")

            submit_button = st.form_submit_button("Submit Project Proposal")

            if submit_button:
                lab_id_query = f"SELECT LabID FROM Student WHERE StudentName = '{state['username']}';"
                cursor.execute(lab_id_query)
                lab_id_result = cursor.fetchone()

                if lab_id_result:
                    lab_id = lab_id_result[0]

                    # Insert the project proposal into the database
                    proposal_query = f"INSERT INTO ProjectProposal (ProposalTitle, ProposalDesc, ProposalSubmissionDate, LabID, TeacherApprovedStatus, DirectorApprovedStatus, StudentID) VALUES ('{project_title}', '{project_description}', NOW(), '{lab_id}', 'not approved', 'not approved', '{state['password']}');"
                    cursor.execute(proposal_query)
                    conn.commit()
                    st.success("Project proposal submitted successfully!")

                    # Output values for debugging
                    st.write(f"Project Title: {project_title}")
                    st.write(f"Project Description: {project_description}")
                    st.write(f"Lab ID: {lab_id}")
                else:
                    st.warning("Lab ID not found. Please check your StudentName.")


        # Option to join an existing project for students
        with st.form(key='join_existing_project_form'):
            if st.form_submit_button("Join an Existing Project"):
                student_id_query = f"SELECT StudentID FROM Student WHERE StudentID = '{state['password']}';"
                cursor.execute(student_id_query)
                student_id_result = cursor.fetchone()

                if student_id_result:
                    student_id = state['password']

                    existing_projects_query = f"SELECT ProposalID, ProposalTitle FROM ProjectProposal WHERE StudentID = '{student_id}' AND TeacherApprovedStatus = 'approved';"
                    cursor.execute(existing_projects_query)

                    # Fetch results as dictionaries
                    existing_projects = [dict(zip(cursor.column_names, proj)) for proj in cursor.fetchall()]

                    if existing_projects:
                        st.write("Choose a project to join:")

                        # Selectbox with project options
                        selected_project = st.selectbox(
                            "Select Project",
                            [(proj['ProposalID'], f"{proj['ProposalID']}: {proj['ProposalTitle']}") for proj in existing_projects],
                            format_func=lambda proj: f"{proj[0]}: {proj[1]}"
                        )


                        # Additional details for the selected project
                        project_id = st.text_input("Enter project id:")
                        project_end_date = st.text_input("Enter project end date dd/mm/yyyy:")
                        mentor_id = st.text_input("Enter mentor id:")
                        project_type = st.text_input("Enter project type:")

                        # Submit button for the form
                        if st.form_submit_button("Submit"):
                            selected_project_id = selected_project.split(":")[0]

                            # Update Student table with the selected project
                            # update_project_query = f"UPDATE Student SET ProjectID = '{selected_project_id}' WHERE StudentName = '{state['username']}';"
                            # cursor.execute(update_project_query)
                            # conn.commit()

                            # Insert additional details into the Project table
                            insert_project_details_query = f"INSERT INTO Project (ProjectName, ProjectStatus, ProjectStartDate, ProjectEndDate, MentorID, StudentID, LabID, ProposalID, ProjectType) " \
                                                            f"SELECT ProposalTitle, 'ongoing', NOW(), {project_end_date}, {mentor_id}, '{state['password']}', LabID, '{selected_project_id}', {project_type} " \
                                                            f"FROM ProjectProposal WHERE ProposalID = '{selected_project_id}';"
                            cursor.execute(insert_project_details_query)
                            conn.commit()

                            st.success(f"You have joined the project: {selected_project} with additional details submitted successfully.")

                    else:
                        st.warning("No existing projects available to join or projects are not approved by the teacher.")

                else:
                    st.warning("Student ID not found. Please check your StudentName.")









    # Continue with the rest of the application for other user types
    elif state["user_type"] == "Teacher":
        # Teacher view
        # Mark attendance
        st.write("Please Refer to the side bar:")

        # Sidebar for teacher actions
        st.sidebar.header("Teacher Actions")
        action = st.sidebar.radio("Select Action", ["None", "Add Student", "Delete Student", "Update Student"])

        if action == "Add Student":
            # Add student form
            st.sidebar.header("Add Student")
            new_student_id = st.sidebar.text_input("Enter Student ID:")
            new_student_name = st.sidebar.text_input("Enter Student Name:")
            new_student_lab_id = st.sidebar.text_input("Enter Lab ID:")

            if st.sidebar.button("Add"):
                # Add student functionality
                new_student_password = new_student_id  # Setting the password as the student ID
                new_student_query = f"INSERT INTO Student (StudentID, StudentName, LabID) VALUES ('{new_student_id}', '{new_student_name}', '{new_student_lab_id}');"
                cursor.execute(new_student_query)
                conn.commit()
                st.sidebar.success(f"Student with ID {new_student_id} added successfully!")

        elif action == "Delete Student":
            # Delete student form
            st.sidebar.header("Delete Student")
            delete_student_id = st.sidebar.text_input("Enter Student ID to Delete:")

            if st.sidebar.button("Delete"):
                # Delete student functionality
                delete_student_query = f"DELETE FROM Student WHERE StudentID = '{delete_student_id}';"
                cursor.execute(delete_student_query)
                conn.commit()
                st.sidebar.success(f"Student with ID {delete_student_id} deleted successfully!")

        elif action == "Update Student":
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

    elif state["user_type"] == "Lab Personnel":
        if not state['lab_id'] or not st.session_state.session_state_initialized:
            # Lab Personnel needs to enter their Lab ID
            state['lab_id'] = st.text_input("Enter Lab ID:")
            st.session_state.session_state_initialized = True

        # Fetch lab personnel details
        lab_personnel_query = f"SELECT * FROM LabPersonnel WHERE PersonnelName = '{state['username']}' AND PersonnelID = '{state['password']}' AND LabID = '{state['lab_id']}';"
        cursor.execute(lab_personnel_query)
        lab_personnel = cursor.fetchone()

        if lab_personnel:
            st.success(f"Login successful! Welcome, {state['username']}!")
            st.header("Project Approval")

            # Display pending project proposals in the lab
            pending_proposals_query = f"""
                SELECT pp.ProposalID, pp.ProposalTitle, pp.ProposalDesc, pp.ProposalSubmissionDate, pp.TeacherApprovedStatus, pp.DirectorApprovedStatus,
                       pp.StudentID, s.StudentName
                FROM ProjectProposal pp
                JOIN Student s ON pp.StudentID = s.StudentID
                WHERE pp.LabID = '{state['lab_id']}' AND pp.TeacherApprovedStatus = 'not approved';
            """
            cursor.execute(pending_proposals_query)
            pending_proposals = cursor.fetchall()

            if pending_proposals:
                st.write("Pending Project Proposals:")
                for proposal in pending_proposals:
                    st.write(f"Proposal ID: {proposal[0]}, Title: {proposal[1]}, Description: {proposal[2]}, "
                             f"Submission Date: {proposal[3]}, Teacher Approval: {proposal[4]}, Director Approval: {proposal[5]}, "
                             f"Student ID: {proposal[6]}, Student Name: {proposal[7]}")

                # Project Approval form
                selected_proposal_id = st.selectbox("Select Proposal to Approve:", [proposal[0] for proposal in pending_proposals])
                if st.button("Approve Project"):
                    # Update the project approval status in the database
                    approve_project_query = f"UPDATE ProjectProposal SET TeacherApprovedStatus = 'approved' WHERE ProposalID = '{selected_proposal_id}';"
                    cursor.execute(approve_project_query)
                    conn.commit()
                    st.success("Project approved successfully!")

            else:
                st.write("No pending project proposals for approval.")
        else:
            st.warning("Invalid Lab ID. Please check your credentials.")

# Close the database connection
conn.close()
