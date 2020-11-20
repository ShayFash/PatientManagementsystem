import pytest

from Labwork import *

# dictionary input for a lab request in LabTest.
request_input = {
    'sender': 'Dr. Pipper',
    'recipient': 'Dr. Robert',
    'patient_ID': '6060842',
    'details': 'We applied the cortical electrodes but '
               'were unable to get a neural response.'
}


# LabResult tests
def test_lab_get_empty_result():
    # default constructor should have empty string for result
    lr = LabResult()
    assert "" == lr.get_result()


def test_lab_get_result():
    lr = LabResult("Results are pretty good", [])
    assert "Results are pretty good" == lr.get_result()


def test_lab_set_result():
    # set result manually after default constructor
    lr = LabResult()
    lr.set_result("Results are inconclusive")
    assert "Results are inconclusive" == lr.get_result()


# LabTest tests
def test_lab_test_make_request():
    lt = LabTest()
    expected = "sent by: Dr. Pipper, sent to: Dr. Robert, " \
               "patient ID: 6060842, details: We applied the cortical " \
               "electrodes but were unable to get a neural response."
    lt.make_request(request_input)
    assert expected == lt.get_request()


