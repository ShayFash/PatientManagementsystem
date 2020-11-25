import pytest
from Medication import *


def test_scientific_name():
    medication = Medication()
    assert medication.get_scientific_name() == ""
    medication.set_scientific_name("Dextroamphetamine-Amphetamine")
    assert medication.get_scientific_name() == "Dextroamphetamine-Amphetamine"


def test_market_name():
    medication = Medication()
    list1 = medication.get_market_names
    assert len(list1) == 0
    list2 = ["Adderall", "Mydayis"]
    medication.set_market_names(list2)
    list3 = medication.market_names
    for i in range(len(list3)):
        assert list2[i] == list3[i]
