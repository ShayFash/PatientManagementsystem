import pytest
from Names import *
from PatientProfile import *

patient_name = FullName()
patient_name.set_surname("Alan")
patient_name.set_given_name("Gerald")
patient_name.set_preferred_name("Jerry")
patient_name.set_middle_names(["Mark", "Bob"])


def test_patient_profile_constructor():
    pass


def test_patient_profile_get_name():
    pp = PatientProfile(patient_name, [], [], "300", [], [], [])
    assert "Gerald Mark Bob Alan" == pp.get_name().get_full_name_to_string()


def test_patient_profile_get_demographics():
    pass


def test_patient_profile_get_billing():
    pp = PatientProfile(patient_name, [], [], "300", [], [], [])
    assert "300" == pp.get_billing()


def test_patient_profile_get_notes():
    pass


def test_patient_profile_get_drugs():
    pass


def test_patient_profile_get_lab_work():
    pass
