import pytest
from Medication import *
from MedicationsList import *


def test_adding_and_removing():
    medications_list = MedicationsList()

    adderall = Medication()
    adderall.set_scientific_name("Dextroamphetamine-Amphetamine")
    adderall_names = ["Adderall", "Mydayis"]
    adderall.set_market_names(adderall_names)

    assert len(medications_list.get_list()) == 0
    medications_list.add_medication(adderall)
    assert len(medications_list.get_list()) == 1
    medications_list.remove_medication(adderall)
    assert len(medications_list.get_list()) == 0

    medications_list.add_medication(adderall)
    assert len(medications_list.get_list()) == 1
    medications_list.clear()
    assert len(medications_list.get_list()) == 0


