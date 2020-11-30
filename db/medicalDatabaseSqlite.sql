--
-- File generated with SQLiteStudio v3.2.1 on Sun Nov 29 23:30:53 2020
--
-- Text encoding used: UTF-8
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: Allergies
DROP TABLE IF EXISTS Allergies;
CREATE TABLE Allergies (allergyEntryID INT PRIMARY KEY, patientID INT NOT NULL, item TEXT, severity_description TEXT, medical_name TEXT);

-- Table: Billing
DROP TABLE IF EXISTS Billing;
CREATE TABLE Billing (patientID INTEGER NOT NULL PRIMARY KEY, billingID INTEGER, medicalSecretaryID INTEGER, datetime dateOfEntry, billingCode TEXT NOT NULL, FOREIGN KEY (medicalSecretaryID) REFERENCES MedicalSecretary (medicalSecretaryID), FOREIGN KEY (patientID) REFERENCES Patient (patientID));

-- Table: Credentials
DROP TABLE IF EXISTS Credentials;
CREATE TABLE Credentials (
    credentialsID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    userLevelID INTEGER NOT NULL,
    
    FOREIGN KEY (userLevelID) REFERENCES UserLevel(userLevelID)
);

-- Table: Doctor
DROP TABLE IF EXISTS Doctor;
CREATE TABLE Doctor (
    doctorID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    medProID INTEGER NOT NULL,
    crendentialsID INTEGER NOT NULL,
    name TEXT NOT NULL,
    specialist INTEGER NOT NULL,
    specialityID INTEGER,
    
    FOREIGN KEY (medProID) REFERENCES MedicalProfessional(medProID),
    FOREIGN KEY (specialityID) REFERENCES Speciality(specialityID),
    FOREIGN KEY (crendentialsID) REFERENCES Credentials(crendentialsID),
    CHECK (specialist >= 0 AND specialist <= 1)
);

-- Table: Gender
DROP TABLE IF EXISTS Gender;
CREATE TABLE Gender (
    genderID INTEGER PRIMARY KEY NOT NULL,
    gender TEXT NOT NULL
);

-- Table: GovernmentBody
DROP TABLE IF EXISTS GovernmentBody;
CREATE TABLE GovernmentBody (
    governmentBodyID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    credentialsID INTEGER NOT NULL,
    name TEXT NOT NULL,
    
    FOREIGN KEY (credentialsID) REFERENCES Credentials(crendentialsID)
);

-- Table: HospitalAdministrator
DROP TABLE IF EXISTS HospitalAdministrator;
CREATE TABLE HospitalAdministrator (
    hospitalAdministratorID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    credentialsID INTEGER NOT NULL,
    name TEXT NOT NULL,
    
    FOREIGN KEY (credentialsID) REFERENCES Credentials(crendentialsID)
);

-- Table: LabRequest
DROP TABLE IF EXISTS LabRequest;
CREATE TABLE LabRequest (
    labRequestID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    labTestID INTEGER NOT NULL,
    requestDate DATETIME NOT NULL,
    
    FOREIGN KEY (labTestID) REFERENCES LabTest(labTestID)
);

-- Table: LabResult
DROP TABLE IF EXISTS LabResult;
CREATE TABLE LabResult (
    labResultID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    labTestID INTEGER NOT NULL,
    finishDate DATETIME NOT NULL,
    results TEXT NOT NULL,
    image TEXT,
    
    FOREIGN KEY (labTestID) REFERENCES LabTest(labTestID)
);

-- Table: LabTest
DROP TABLE IF EXISTS LabTest;
CREATE TABLE LabTest (
    labTestID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    requesterID INTEGER NOT NULL,
    technicianID INTEGER NOT NULL,
    testTypeID INTEGER NOT NULL,
    
    FOREIGN KEY (requesterID) REFERENCES MedicalProfessional(medProID),
    FOREIGN KEY (technicianID) REFERENCES Technician(technicianID),
    FOREIGN KEY (testTypeID) REFERENCES TestType(testTypeID)
);

-- Table: MedicalProfessional
DROP TABLE IF EXISTS MedicalProfessional;
CREATE TABLE MedicalProfessional (
    medProID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL
);

-- Table: MedicalSecretary
DROP TABLE IF EXISTS MedicalSecretary;
CREATE TABLE MedicalSecretary (
    medicalSecretaryID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    credentialsID INTEGER NOT NULL,
    name TEXT NOT NULL,
    
    FOREIGN KEY (credentialsID) REFERENCES Credentials(crendentialsID)
);

-- Table: MedicationEntry
DROP TABLE IF EXISTS MedicationEntry;
CREATE TABLE MedicationEntry (medicationEntryID INTEGER PRIMARY KEY, patientID INTEGER NOT NULL, icd10 TEXT, scientific_name TEXT NOT NULL, FOREIGN KEY (patientID) REFERENCES Patient (patientID));

-- Table: Names
DROP TABLE IF EXISTS Names;
CREATE TABLE Names (patientID INT PRIMARY KEY NOT NULL, givenName TEXT, middleNames TEXT, surname TEXT);

-- Table: Note
DROP TABLE IF EXISTS Note;
CREATE TABLE Note (
    noteEntryID INT  PRIMARY KEY,
    patientID   INT  NOT NULL,
    date        TEXT,
    author      TEXT,
    body        TEXT
);

-- Table: Nurse
DROP TABLE IF EXISTS Nurse;
CREATE TABLE Nurse (
    nurseID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    medProID INTEGER NOT NULL,
    credentialsID INTEGER NOT NULL,
    name TEXT NOT NULL,

    FOREIGN KEY (medProID) REFERENCES MedicalProfessional(medProID),
    FOREIGN KEY (credentialsID) REFERENCES Credentials(crendentialsID)
);

-- Table: Patient
DROP TABLE IF EXISTS Patient;
CREATE TABLE Patient (patientID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, federalHealthID INTEGER UNIQUE, provinceID INTEGER, credentialsID INTEGER, name TEXT, genderID INTEGER, dateOfBirth DATE, age INTEGER, "temp" INTEGER, address TEXT, familyHistory TEXT, medicalConditions TEXT, FOREIGN KEY (provinceID) REFERENCES Province (provinceID), FOREIGN KEY (credentialsID) REFERENCES Credentials (crendentialsID), FOREIGN KEY (genderID) REFERENCES Gender (genderID), CHECK ("temp" >= 0 AND "temp" <= 1));

-- Table: PatientNotes
DROP TABLE IF EXISTS PatientNotes;
CREATE TABLE PatientNotes (
    notesID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    patientID INTEGER NOT NULL,
    authorID INTEGER NOT NULL,
    dateOfEntry DATETIME NOT NULL,
    textbody TEXT NOT NULL,
    image TEXT,
    
    FOREIGN KEY (patientID) REFERENCES Credentials(credentialsID),
    FOREIGN KEY (authorID) REFERENCES MedicalProfessional(medProID)
);

-- Table: Payroll
DROP TABLE IF EXISTS Payroll;
CREATE TABLE Payroll (
    payrollID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    userID INTEGER NOT NULL,
    statusID INTEGER NOT NULL,
    payDate DATETIME NOT NULL,
    runBy TEXT,
    paycycleStart DATETIME NOT NULL,
    paycycleEnd DATETIME NOT NULL,
    total REAL NOT NULL,
    
    FOREIGN KEY (userID) REFERENCES Credentials(crendentialsID),
    FOREIGN KEY (statusID) REFERENCES PayrollStatus(statusID)
);

-- Table: PayrollStatus
DROP TABLE IF EXISTS PayrollStatus;
CREATE TABLE PayrollStatus (
    statusID INTEGER PRIMARY KEY NOT NULL,
    status TEXT NOT NULL
);

-- Table: Pharmacist
DROP TABLE IF EXISTS Pharmacist;
CREATE TABLE Pharmacist (
    pharmacistID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    medProID INTEGER NOT NULL,
    credentialsID INTEGER NOT NULL,
    name TEXT NOT NULL,

    FOREIGN KEY (medProID) REFERENCES MedicalProfessional(medProID),
    FOREIGN KEY (credentialsID) REFERENCES Credentials(crendentialsID)
);

-- Table: ProfileLog
DROP TABLE IF EXISTS ProfileLog;
CREATE TABLE ProfileLog (
    profileLogID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    patientID INTEGER NOT NULL,
    viewerID INTEGER NOT NULL,
    dateOfView DATETIME NOT NULL,
        
    FOREIGN KEY (patientID) REFERENCES Patient(patientID),
    FOREIGN KEY (viewerID) REFERENCES Credentials(credentialsID)
);

-- Table: Province
DROP TABLE IF EXISTS Province;
CREATE TABLE Province (
    provinceID INTEGER PRIMARY KEY NOT NULL,
    province TEXT NOT NULL
);

-- Table: Speciality
DROP TABLE IF EXISTS Speciality;
CREATE TABLE Speciality (
    specialityID INTEGER PRIMARY KEY NOT NULL,
    speciality TEXT NOT NULL
);

-- Table: Technician
DROP TABLE IF EXISTS Technician;
CREATE TABLE Technician (
    technicianID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    credentialsID INTEGER NOT NULL,
    name TEXT NOT NULL,
    
    FOREIGN KEY (credentialsID) REFERENCES Credentials(crendentialsID)
);

-- Table: TestType
DROP TABLE IF EXISTS TestType;
CREATE TABLE TestType (
    testTypeID INTEGER PRIMARY KEY NOT NULL,
    name TEXT NOT NULL
);

-- Table: UserLevel
DROP TABLE IF EXISTS UserLevel;
CREATE TABLE UserLevel (
    userLevelID INTEGER PRIMARY KEY NOT NULL,
    userLevelName TEXT NOT NULL
);

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
