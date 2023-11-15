CREATE DATABASE ResearchLabManagementSystem;
USE ResearchLabManagementSystem;

CREATE TABLE ResearchLab (
    LabID INT,
    LabName varchar(20),
    LabComponents varchar(50),
    LabComponentsDetails varchar(200),
    PRIMARY KEY (LabID)
);

CREATE TABLE LabPersonnel (
	PersonnelID INT,
    PersonnelName varchar(20),
    LabID INT,
    PRIMARY KEY (PersonnelID),
    foreign key (LabID) references ResearchLab(LabID)
);

CREATE TABLE Teacher (
	TeacherID INT,
    TeacherName varchar(20),
    TeacherRole varcahr(20), -- this is to indicate hierarchy
    PRIMARY KEY (TeacherID)
);

CREATE TABLE Student (
	StudentID INT,
    StudentName varchar(20),
    LabID INT,
    PRIMARY KEY (StudentID),
    foreign key (LabID) references ResearchLab(LabID)
);

CREATE TABLE ProjectProposal (
	ProposalID INT,
    ProposalTitle varchar(50),
    ProposalDesc varchar(200),
    ProposalSubmissionDate datetime,
    LabID INT,
    TeacherApprovedStatus enum('approved','not approved') default 'not approved',
    DirectorApprovedStatus enum('approved','not approved') default 'not approved',
    ApprovedID INT, -- the id of the teacher who approves
    StudentID INT,
    PRIMARY KEY (ProposalID),
    foreign key (LabID) references ResearchLab(LabID),
    foreign key (ApprovedID) references Teacher(TeacherID),
    foreign key (StudentID) references Student(StudentID)
);

CREATE TABLE Project (
	ProjectID INT,
    ProjectName varchar(50),
    ProjectStatus enum('ongoing','finished'),
    ProjectStartDate datetime,
    ProjectEndDate datetime,
    MentorID INT,
    StudentID INT,
    LabID INT,
    ProposalID INT,
    ProjectType varchar(20),
    -- internship or full time or something else
    PRIMARY KEY (ProjectID),
    foreign key (LabID) references ResearchLab(LabID),
    foreign key (MentorID) references Teacher(TeacherID),
    foreign key (ProposalID) references ProjectProposal(ProposalID),
    foreign key (StudentID) references Student(StudentID)
);

CREATE TABLE Eventss (
	EventID INT,
    EventName varchar(20),
    EventDate datetime,
    LabID INT,
    ManagerID INT,
    CashPrize INT,
    Winner varchar(20),
    WinnerID INT,
    PRIMARY KEY (EventID),
    foreign key (LabID) references ResearchLab(LabID),
    foreign key (ManagerID) references Teacher(TeacherID),
    foreign key (WinnerID) references Student(StudentID)
);

CREATE TABLE stipend (
	StipendID INT,
    StipendAmount INT,
    StipendDate datetime,
    StudentID INT,
    LabID INT,
    PRIMARY KEY (StipendID),
    foreign key (StudentID) references Student(StudentID),
    foreign key (LabID) references ResearchLab(LabID)
);

CREATE TABLE AttendanceRecord (
	RecordID int,
    RecordType varchar(20),
    -- Could be biometric or manual entry
    DateOfEntry date,
    EntryTime time,
    ExitTime time,
    Signature INT,
    -- could be some kind of password
    StudentID INT,
    TeacherID INT,
    LabID INT,
    PRIMARY KEY (RecordID),
    foreign key (StudentID) references Student(StudentID),
    foreign key (TeacherID) references Teacher(TeacherID),
    foreign key (LabID) references ResearchLab(LabID)
);

-- for project approval
DELIMITER //
CREATE PROCEDURE UpdateApprovalStatus(
    IN proposal_id INT,
    IN teacher_approval_status ENUM('approved', 'not approved'),
    IN director_approval_status ENUM('approved', 'not approved'),
    IN approver_id INT
)
BEGIN
    UPDATE ProjectProposal
    SET 
        TeacherApprovedStatus = teacher_approval_status,
        DirectorApprovedStatus = director_approval_status,
        ApprovedID = approver_id
    WHERE ProposalID = proposal_id;

    -- If both teacher and director have approved, update the corresponding student's project table
    IF teacher_approval_status = 'approved' AND director_approval_status = 'approved' THEN
        -- You can perform further actions here
        -- For example, you can insert data into the Project table
        INSERT INTO Project (ProjectName, ProjectStatus, ProjectStartDate, ProjectEndDate, MentorID, StudentID, LabID, ProposalID, ProjectType)
        VALUES ('ProjectName', 'ongoing', NOW(), NOW(), 1, (SELECT StudentID FROM ProjectProposal WHERE ProposalID = proposal_id), (SELECT LabID FROM ProjectProposal WHERE ProposalID = proposal_id), proposal_id, 'internship');
    END IF;
END //
DELIMITER ;

