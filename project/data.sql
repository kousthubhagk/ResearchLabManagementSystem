-- ResearchLab table
INSERT INTO ResearchLab (LabID, LabName, LabComponents, LabComponentsDetails)
VALUES
    (1, 'Computer Science Lab', 'Computers, Projectors', 'High-end computers with graphic cards, HD projectors'),
    (2, 'Chemistry Lab', 'Microscopes, Bunsen burners', 'Advanced chemistry equipment for experiments'),
    (3, 'Physics Lab', 'Telescopes, Laser apparatus', 'Equipment for physics experiments and demonstrations'),
    (4, 'Biology Lab', 'Microscopes, Dissection kits', 'Tools for biological studies and experiments'),
    (5, 'Engineering Lab', '3D Printers, Prototyping tools', 'Facilities for engineering projects and prototyping'),
    (6, 'Robotics Lab', 'Robot kits, Sensors', 'Resources for robotics and automation projects'),
    (7, 'Data Science Lab', 'Servers, Data sets', 'Infrastructure for data analysis and machine learning'),
    (8, 'Electronics Lab', 'Oscilloscopes, Circuit boards', 'Tools for electronics design and experimentation'),
    (9, 'Psychology Lab', 'Psychometric tests, EEG machines', 'Equipment for psychological experiments'),
    (10, 'Environmental Science Lab', 'Weather station, Soil testing kits', 'Tools for environmental studies');

-- LabPersonnel table
INSERT INTO LabPersonnel (PersonnelID, PersonnelName, LabID)
VALUES
    (1, 'John Doe', 1),
    (2, 'Jane Smith', 2),
    (3, 'Robert Johnson', 3),
    (4, 'Emily Davis', 4),
    (5, 'Michael Wilson', 5),
    (6, 'Amanda White', 6),
    (7, 'Daniel Miller', 7),
    (8, 'Olivia Taylor', 8),
    (9, 'Ethan Anderson', 9),
    (10, 'Sophia Brown', 10);

-- Teacher table
INSERT INTO Teacher (TeacherID, TeacherName)
VALUES
    (1, 'Dr. Smith'),
    (2, 'Prof. Johnson'),
    (3, 'Dr. Williams'),
    (4, 'Prof. Davis'),
    (5, 'Dr. Taylor'),
    (6, 'Prof. White'),
    (7, 'Dr. Miller'),
    (8, 'Prof. Anderson'),
    (9, 'Dr. Wilson'),
    (10, 'Prof. Brown');

-- Student table
INSERT INTO Student (StudentID, StudentName, LabID)
VALUES
    (1, 'Alice Johnson', 1),
    (2, 'Bob Smith', 2),
    (3, 'Charlie Wilson', 3),
    (4, 'David Davis', 4),
    (5, 'Eva Taylor', 5),
    (6, 'Frank White', 6),
    (7, 'Grace Brown', 7),
    (8, 'Henry Miller', 8),
    (9, 'Isabel Anderson', 9),
    (10, 'Jack Wilson', 10);

-- ProjectProposal table
INSERT INTO ProjectProposal (ProposalID, ProposalTitle, ProposalDesc, ProposalSubmissionDate, LabID)
VALUES
    (1, 'Machine Learning Project', 'Develop an ML model for image recognition', '2023-01-15', 1),
    (2, 'Chemical Reaction Study', 'Investigate the kinetics of a specific chemical reaction', '2023-02-10', 2),
    (3, 'Physics Experiment on Optics', 'Study the behavior of light in different mediums', '2023-03-05', 3),
    (4, 'Genetic Engineering Project', 'Modify the DNA of a bacterial strain for a specific trait', '2023-04-20', 4),
    (5, 'Civil Engineering Research', 'Analyze the structural stability of a building design', '2023-05-15', 5),
    (6, 'Robotics Automation Project', 'Develop a robot for automated warehouse operations', '2023-06-12', 6),
    (7, 'Data Analysis of Financial Data', 'Explore patterns and trends in financial market data', '2023-07-01', 7),
    (8, 'Electronic Circuit Design', 'Create a circuit for a specific electronic device', '2023-08-18', 8),
    (9, 'Psychological Study on Memory', 'Investigate factors affecting human memory retention', '2023-09-10', 9),
    (10, 'Environmental Impact Assessment', 'Evaluate the environmental impact of a local construction project', '2023-10-05', 10);

-- Project table
INSERT INTO Project (ProjectID, ProjectName, ProjectStatus, ProjectStartDate, ProjectEndDate, MentorID, LabID, ProposalID, ProjectType)
VALUES
    (1, 'Image Recognition Project', 'ongoing', '2023-02-01', NULL, 1, 1, 1, 'internship'),
    (2, 'Reaction Kinetics Analysis', 'finished', '2023-02-20', '2023-04-15', 2, 2, 2, 'full time'),
    (3, 'Optics Experiment', 'ongoing', '2023-03-15', NULL, 3, 3, 3, 'internship'),
    (4, 'Genetic Engineering Study', 'finished', '2023-05-01', '2023-07-10', 4, 4, 4, 'part-time'),
    (5, 'Structural Stability Analysis', 'ongoing', '2023-06-01', NULL, 5, 5, 5, 'internship'),
    (6, 'Warehouse Robotics Project', 'ongoing', '2023-07-01', NULL, 6, 6, 6, 'full time'),
    (7, 'Financial Data Analysis', 'finished', '2023-08-01', '2023-09-30', 7, 7, 7, 'part-time'),
    (8, 'Electronic Circuit Design Project', 'ongoing', '2023-09-15', NULL, 8, 8, 8, 'full time'),
    (9, 'Memory Study', 'finished', '2023-10-01', '2023-11-10', 9, 9, 9, 'internship'),
    (10, 'Environmental Impact Assessment', 'ongoing', '2023-11-15', NULL, 10, 10, 10, 'part-time');

-- Eventss table
INSERT INTO Eventss (EventID, EventName, EventDate, LabID, ManagerID, CashPrize, Winner, WinnerID)
VALUES
    (1, 'Tech Expo', '2023-03-10', 1, 1, 1000, 'Best Project', 1),
    (2, 'Chemistry Fair', '2023-04-05', 2, 2, 800, 'Top Experiment', 2),
    (3, 'Physics Symposium', '2023-05-20', 3, 3, 1200, 'Outstanding Presentation', 3),
    (4, 'Biology Exhibition', '2023-06-15', 4, 4, 900, 'Best Display', 4),
    (5, 'Engineering Showcase', '2023-07-10', 5, 5, 1500, 'Innovative Design', 5),
    (6, 'Robotics Competition', '2023-08-25', 6, 6, 1000, 'Top Performing Robot', 6),
    (7, 'Data Science Expo', '2023-09-15', 7, 7, 1300, 'Best Data Analysis', 7),
    (8, 'Electronics Fair', '2023-10-20', 8, 8, 1100, 'Outstanding Circuit Design', 8),
    (9, 'Psychology Conference', '2023-11-05', 9, 9, 1000, 'Best Research Paper', 9),
    (10, 'Environmental Impact Forum', '2023-12-01', 10, 10, 1400, 'Top Presentation', 10);

-- stipend table
INSERT INTO stipend (StipendID, StipendAmount, StipendDate, StudentID, LabID)
VALUES
    (1, 500, '2023-03-15', 1, 1),
    (2, 600, '2023-04-15', 2, 2),
    (3, 550, '2023-05-15', 3, 3),
    (4, 700, '2023-06-15', 4, 4),
    (5, 800, '2023-07-15', 5, 5),
    (6, 750, '2023-08-15', 6, 6),
    (7, 900, '2023-09-15', 7, 7),
    (8, 650, '2023-10-15', 8, 8),
    (9, 750, '2023-11-15', 9, 9),
    (10, 700, '2023-12-15', 10, 10);

-- AttendanceRecord table
INSERT INTO AttendanceRecord (RecordID, RecordType, DateOfEntry, EntryTime, ExitTime, Signature, StudentID, TeacherID, LabID)
VALUES
    (1, 'Biometric', '2023-03-01', '08:00:00', '16:00:00', 123456, 1, 1, 1),
    (2, 'Manual Entry', '2023-03-02', '08:30:00', '16:30:00', 654321, 2, 2, 2),
    (3, 'Biometric', '2023-03-03', '09:00:00', '17:00:00', 987654, 3, 3, 3),
    (4, 'Manual Entry', '2023-03-04', '09:30:00', '17:30:00', 456789, 4, 4, 4),
    (5, 'Biometric', '2023-03-05', '10:00:00', '18:00:00', 789012, 5, 5, 5),
    (6, 'Manual Entry', '2023-03-06', '10:30:00', '18:30:00', 567890, 6, 6, 6),
    (7, 'Biometric', '2023-03-07', '11:00:00', '19:00:00', 234567, 7, 7, 7),
    (8, 'Manual Entry', '2023-03-08', '11:30:00', '19:30:00', 890123, 8, 8, 8),
    (9, 'Biometric', '2023-03-09', '12:00:00', '20:00:00', 345678, 9, 9, 9),
    (10, 'Manual Entry', '2023-03-10', '12:30:00', '20:30:00', 012345, 10, 10, 10);
