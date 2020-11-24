import pytest
from src.Allergies import *

def test_allergy_name():
    allergy = Allergy("Peanut", "Anaphylactic shock")
    assert allergy.getItem() == "Peanut"

def test_allergy_severity():
    allergy = Allergy("Peanut", "Anaphylactic shock")
    assert allergy.getSeverityDescription() == "Anaphylactic shock"

def test_allergy_equivalence():
    allergy = Allergy("Peanut", "Anaphylactic shock")
    allergy2 = Allergy("Peanut", "BAD")
    assert allergy == allergy2

def test_medical_allergy_scientific_name():
    medical_allergy = Allergy("Something", "Bad Effect", "Medical Something")
    assert medical_allergy.getScientificName() == "Medical Something"

def test_allergy_list_to_string():
    allergyList = AllergyList()
    allergy = Allergy("Peanut", "Anaphylactic shock")
    medical_allergy = Allergy("Something", "Bad Effect", "Medical Something")
    allergyList.addAllergy(allergy)
    allergyList.addAllergy(medical_allergy)
    assert allergyList.getAllergiesToString() == "Peanut, Something"

def test_add_uniqe_allergy():
    allergyList = AllergyList()
    allergy = Allergy("Peanut", "Anaphylactic shock")
    allergyList.addAllergy(allergy)
    assert allergyList.getAllergiesToString() == "Peanut"

def test_add_duplicate_allergies():
    allergyList = AllergyList()
    allergy = Allergy("Peanut", "Anaphylactic shock")
    allergy2 = Allergy("Peanut", "Something bad happens")
    allergy3 = Allergy("Cat", "Cat fur makes eyes puff up")
    allergyList.addAllergy(allergy)
    allergyList.addAllergy(allergy2)
    allergyList.addAllergy(allergy3)
    assert allergyList.getAllergiesToString() == "Peanut, Cat"

def test_remove_unique_allergy():
    allergyList = AllergyList()
    allergy = Allergy("Peanut", "Anaphylactic shock")
    medical_allergy = Allergy("Something", "Bad Effect", "Medical Something")
    allergyList.addAllergy(allergy)
    allergyList.addAllergy(medical_allergy)
    allergyList.removeAllergy(allergy)
    assert allergyList.getAllergiesToString() == "Something"

def test_get_unset_medical_name():
    allergy = Allergy("Peanut", "Anaphylactic shock")
    # uses a pytest method to test if an assert is being called properly
    with pytest.raises(Exception):
        allergy.getScientificName()
