import pytest
from PatientProfile import *

# test parameters for re-use in different test cases
patient_name = FullName()
patient_name.set_surname("Alan")
patient_name.set_given_name("Gerald")
patient_name.set_preferred_name("Jerry")
patient_name.set_middle_names(["Mark", "Bob"])
demographics = Demographics()
notes = [Note(), Note()]
notes[0].write_body("It's just supply and demand.")
notes[1].write_body("I'm tired of this soup du jour.")
med1 = Medication()
med1.set_scientific_name("Rhonoclycerin")
med1.set_market_names("White Rhino")
medications = MedicationsList()
medications.add_medication(med1)
allergies = AllergyList()
lab_work = [LabTest(), LabTest()]


def test_patient_profile_constructor():
    pp = PatientProfile(patient_name, demographics, notes, "300BA", medications, allergies, lab_work)
    assert None is not pp


def test_patient_profile_get_name():
    pp = PatientProfile(patient_name, demographics, notes, "300BA", medications, allergies, lab_work)
    assert "Gerald Mark Bob Alan" == pp.get_name().get_full_name_to_string()


def test_patient_profile_get_demographics():
    pp = PatientProfile(patient_name, demographics, notes, "300BA", medications, allergies, lab_work)
    assert None is not pp.get_demographics()


def test_patient_profile_get_billing():
    pp = PatientProfile(patient_name, demographics, notes, "300BA", medications, allergies, lab_work)
    assert "300BA" == pp.get_billing()


def test_patient_profile_get_notes():
    pp = PatientProfile(patient_name, demographics, notes, "300BA", medications, allergies, lab_work)
    assert "It's just supply and demand." == pp.get_notes()[0].get_body()
    assert "I'm tired of this soup du jour." == pp.get_notes()[1].get_body()


def test_patient_profile_get_drugs():
    pp = PatientProfile(patient_name, demographics, notes, "300BA", medications, allergies, lab_work)
    assert 1 == len(pp.get_drugs().get_list())


def test_patient_profile_get_lab_work():
    pp = PatientProfile(patient_name, demographics, notes, "300BA", medications, allergies, lab_work)
    assert None is not pp.get_lab_work()
