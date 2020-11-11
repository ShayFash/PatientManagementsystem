import pytest
from Demographics import *
from Names import *

    # TODO: Allergies
def test_demo_allergies():
    test_demo = Demographics()
    test_demo.set_allergies()
    #assert test_demo.get_allergies() == Something
    pass

    # TODO: Medications
def test_demo_medications():
    test_demo = Demographics()
    test_demo.set_medications()
    #assert test_demo.get_medications() == Something
    pass

def test_demo_name():
    test_demo = Demographics()
    fn = FullName()
    fn.set_given_name("David")
    fn.set_middle_names(["Lee", "Roy", "Jenkins"])
    fn.set_surname("Baesmintdwaellor")
    fn.set_preferred_name("Dave")
    test_demo.set_name(fn)
    assert "David Lee Roy Jenkins Baesmintdwaellor" == test_demo.get_name().get_full_name_to_string()

def test_demo_address():
    test_demo = Demographics()
    test_demo.set_address("100 Lane Cresc")
    assert test_demo.get_address() == "100 Lane Cresc"

def test_demo_date_of_birth():
    test_demo = Demographics()
    test_demo.set_date_of_birth("08/07/1997")
    assert test_demo.get_date_of_birth() == "08/07/1997"

def test_demo_family_history():
    test_demo = Demographics()
    test_demo.set_family_history("John's mom has diabetes")
    assert test_demo.get_family_history() == "John's mom has diabetes"

def test_demo_medical_conditions():
    test_demo = Demographics()
    test_demo.set_medical_conditions("Asthma")
    assert test_demo.get_medical_conditions == "Asthma"


