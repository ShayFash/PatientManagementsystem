from PatientProfile import *
import DatabaseController, Demographics, Labwork, Medication, MedicationsList, Names, Note, Allergy, AllergyList

data_controller = DatabaseController.DatabaseController()
demo = Demographics.Demographics()
demo.set_address('main st')
demo.set_date_of_birth('Aug 7 1997')
demo.set_family_history('Type 1')
data_controller.set_demographics(123, demo)

fn = FullName()
fn.set_given_name("David")
fn.set_middle_names(["Lee"])
fn.set_surname("Baesmintdwaellor")
data_controller.set_name(123, fn)

test_note = Note.Note()
test_note.write_date(26, 'November', 2020)
test_note.write_author(fn)
test_note.write_body('My test note')
data_controller.insert_note(123, test_note)

test_note1 = Note.Note()
test_note1.write_date(25, 'November', 2019)
test_note1.write_author(fn)
test_note1.write_body('My SECOND test note')
data_controller.insert_note(123, test_note1)

new_med = Medication.Medication()
new_med.set_scientific_name('acetaminophen')
new_med_list = MedicationsList.MedicationsList()
new_med_list.add_medication(new_med)
data_controller.set_medications(123, new_med_list)

allergy_list = AllergyList.AllergyList()
allergy = Allergy.Allergy('peanut', 'High')
allergy1 = Allergy.Allergy('fish', 'High')
allergy_list.add_allergy(allergy)
allergy_list.add_allergy(allergy1)
data_controller.set_allergies(123, allergy_list)

data_controller.set_billing(123, 'samplebillingcode')

new_patient = data_controller.get_patient(123)

def test_database_controller_get_name():
    assert new_patient.get_name().get_full_name_to_string() == 'David Lee Baesmintdwaellor'
    
def test_database_controller_get_demographics():
    assert new_patient.get_demographics().get_family_history() == 'Type 1'

def test_database_controller_get_billing():
    assert new_patient.get_billing() == 'samplebillingcode'

def test_database_controller_get_medications():
    assert new_patient.get_drugs().get_list()[0].get_scientific_name() == 'acetaminophen'
    
def test_database_controller_get_allergies():
    assert new_patient.profile['allergies'].get_allergies_to_string() == 'peanut, fish'

def print_patient_notes():
    #If you've made prior inserts into your db file a simple assert may fail, so instead this:
    for note in new_patient.get_notes():
        print(note.toString())
    
