# ResearchLabManagementSystem
Welcome to the Research Lab Management System. Please take a moment to read through this README file for important information about the project.
**Important:** The main branch is the primary branch for this project. Please refer to and work with the code in the main branch for the latest stable release. 

### Overview
This Research Lab Management System is a database management system project developed for the DBMS course at PES. It provides functionality for managing research projects, events, and incentives within the university's research labs. This system provides a centralized solution for research lab management. Only the students that are part of the research lab can log in and only teachers can add or delete students into the lab. 

### Features
- **User Authentication:** Supports authentication for students, teachers, and lab personnel.
- **Project Proposals:** Students can submit project proposals, which require approval from teachers.
- **Project Approvals:** Approved projects are managed, including details like project status, start/end dates, mentors, and project types. Students get to choose their mentors and start their projects.
- **Project Management:** Displays ongoing projects in all labs 
- **Event Management:** Displays upcoming events within the labs.
- **Incentives:** Provides information about average stipends, projects with maximum stipends, etc.

### Technologies Used
- **Languages:** Python
- **Web Framework:** Streamlit
- **Database:** MySQL

### Project Structure
- **Database Schema:** The relational schema and ER diagram are included in the `docs` folder.
- **Source Code:** The main Python script is `frontend.py`, which utilizes the Streamlit framework for the web interface.
- **Database Setup:** Instructions for setting up the MySQL database are provided in `script.sql`.
- **Dependencies:** Ensure you have the required Python libraries by running `pip install -r requirements.txt`.

### Getting Started
1. **Database Setup:**
   - Execute the SQL script `script.sql` to set up the required tables and initial data.
   - Update the MySQL connection details in `frontend.py` if needed.

2. **Running the Application:**
   - Run the application using `streamlit run frontend.py`.
   - Access the application through the provided URL.

3. **Usage:**
   - Follow the instructions within the application for different user types (student, teacher, lab personnel). Each of them will have different previledges

**Contribution Guidelines:**

If you'd like to contribute to this project, feel free to fork the repository and submit a pull request with your changes.
