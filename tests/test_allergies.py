import pytest
from src.AllergyList import *

def test_allergy_name():
    allergy = Allergy("Peanut", "Anaphylactic shock")
    assert allergy.get_item() == "Peanut"

def test_allergy_severity():
    allergy = Allergy("Peanut", "Anaphylactic shock")
    assert allergy.get_severity_description() == "Anaphylactic shock"

def test_allergy_equivalence():
    allergy = Allergy("Peanut", "Anaphylactic shock")
    allergy2 = Allergy("Peanut", "BAD")
    assert allergy == allergy2

def test_medical_allergy_scientific_name():
    medical_allergy = Allergy("Something", "Bad Effect", "Medical Something")
    assert medical_allergy.get_medical_name() == "Medical Something"

def test_allergy_list_to_string():
    allergy_list = AllergyList()
    allergy = Allergy("Peanut", "Anaphylactic shock")
    medical_allergy = Allergy("Something", "Bad Effect", "Medical Something")
    allergy_list.add_allergy(allergy)
    allergy_list.add_allergy(medical_allergy)
    assert allergy_list.get_allergies_to_string() == "Peanut, Something"

def test_add_uniqe_allergy():
    allergy_list = AllergyList()
    allergy = Allergy("Peanut", "Anaphylactic shock")
    allergy_list.add_allergy(allergy)
    assert allergy_list.get_allergies_to_string() == "Peanut"

def test_add_duplicate_allergies():
    allergy_list = AllergyList()
    allergy = Allergy("Peanut", "Anaphylactic shock")
    allergy2 = Allergy("Peanut", "Something bad happens")
    allergy3 = Allergy("Cat", "Cat fur makes eyes puff up")
    allergy_list.add_allergy(allergy)
    allergy_list.add_allergy(allergy2)
    allergy_list.add_allergy(allergy3)
    assert allergy_list.get_allergies_to_string() == "Peanut, Cat"

def test_remove_unique_allergy():
    allergy_list = AllergyList()
    allergy = Allergy("Peanut", "Anaphylactic shock")
    medical_allergy = Allergy("Something", "Bad Effect", "Medical Something")
    allergy_list.add_allergy(allergy)
    allergy_list.add_allergy(medical_allergy)
    allergy_list.remove_allergy(allergy)
    assert allergy_list.get_allergies_to_string() == "Something"

def test_get_unset_medical_name():
    allergy = Allergy("Peanut", "Anaphylactic shock")
    # uses a pytest method to test if an assert is being called properly
    with pytest.raises(Exception):
        allergy.get_medical_name()
