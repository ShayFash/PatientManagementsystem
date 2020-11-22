import src.PatientProfile as PatientProfile
import sqlite3

class DatabaseController():

    def create_connection(db_file):
        """ 
        creates a database connection to the SQLite database
        :param db_file: database file
        :return: Connection object or None
        """
        db = None
        try:
            db = sqlite3.connect(db_file)
        except Error as e:
            print(e)
        return db

    def get_patient(health_num):
        """
        Queries all the patient data from the database and compiles it into
        a patient object which is returned to the caller
        :param health_num: a 9-digit integer health number corresponding to patient
        :return PatientProfile: A PatientProfile object
        """
        patient_dict = {}
        patient_dict['name']            #select queries given id health_num
        patient_dict['demographics']    #
        patient_dict['notes']           #
        patient_dict['billing_code']    #
        patient_dict['drugs']           #
        patient_dict['allergies']       #
        patient_dict['lab_work']        #
        #Construct PatientProfile w/ dictionary
        patient_profile = PatientProfile(**patient_dict)
        return patient_profile

    def overwrite_patient(health_num, patient: PatientProfile):
        """
        Overwrites all the fields of a patient profile in the database or 
        creates one if it doesn't exist
        :param health_num: a 9-digit integer health number corresponding to patient 
        :param PatientProfile: A PatientProfile object containing the new patient information
        """
        set_name(health_num, patient.profile['name'])
        if patient.profile['demographics'] != None:
            set_demographics(health_num, patient.profile['demographics'])
        for note in patient.profile['notes']:
            insert_note(health_num)
        if patient.profile['billing_code'] != None:
            set_billing(health_num, patient.profile['billing_code'])
        if patient.profile['drugs'] != None:
            set_medications(health_num, patient.profile['drugs'])
        if patient.profile['allergies'] != None:
            set_allergies(health_num, patient.profile['allergies'])
        if patient.profile['lab_work'] != None:
            set_lab_work(health_num, patient.profile['lab_work'])
        pass

    def set_name(health_num, fullname: FullName):
        """
        Writes the provided FullName objects information into the database for the
        given health_num
        :param health_num: a 9-digit integer health number corresponding to patient 
        :param FullName: a FullName object containing the patient's name
        """
        #insert fullname.given, .middle, .surname, .preferred if they exist w/ id:health_num
        pass

    def set_demographics(health_num, demographics: Demographics):
        """
        Writes the information from the provided Demographics object into the database
        for the given health_num
        :param health_num: a 9-digit integer health number corresponding to patient 
        :param demographics: a Demographics object containing patient information
        """
        for key, item in demographics.demographics.items():
            #insert/replace items into demo's table w/ id:health_num
            pass
        pass

    def insert_note(health_num, note: Note):
        """
        Inserts a note into the database for the specified patient
        :param health_num: a 9-digit integer health number corresponding to patient 
        :param note: a Note object containing note information
        """
        for key, item in note.note.items():
            #insert items into notes table alongside id:health_num
            pass
        pass

    def set_billing(health_num, billing_code):
        """
        Writes the billing information into the database for the given patient
        :param health_num: a 9-digit integer health number corresponding to patient 
        :param billing_code: a str representing patient billing code
        """
        #SQL query to billing_code table with health_num key
        pass

    def set_medications(health_num, medication_list: MedicationList):
        """
        Writes the provided medication list into the database for the patient.
        :param health_num: a 9-digit integer health number corresponding to patient 
        param medication_list: a MedicationList object
        """
        #Medication contains two fields, scientfic_name : str, and market_names[]
        #can this be packaged into a stringified json, stored and later be reconstructed?
        #that, or extra columns in MedicationEntry could be made and be iterated into

        #An implementation: Table per patient?
        for drug in medication_list:
            #insert health_num drug table value drug.scientific_name into column scientific_name
            for name in drug.market_names:
                #insert str(name + ', ') into market names
                pass
    
    def set_allergies(health_num, allergies: Allergies):
        """
        Writes the allergies object into the database for the specified patient
        :param health_num: a 9-digit integer health number corresponding to patient
        :param allergies: an Allergies object already containing allergy information
        """
        pass

    def set_lab_work(health_num, lab_work: Labwork):
        """
        Writes the provided Lab work data into the database for the patient
        :param health_num: a 9-digit integer health number corresponding to patient 
        :param lab_work: a LabWork object containing the lab work data in question
        """
        pass
        


