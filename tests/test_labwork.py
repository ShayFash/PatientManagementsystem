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


# LabRequest Tests
def test_lab_request_set_request():
    lr = LabRequest(request_input['sender'],
                    request_input['recipient'],
                    request_input['patient_ID'],
                    request_input['details'])
    # setting request changes the details field.
    lr.set_request("What has science done?")
    expected = "sent by: Dr. Pipper, sent to: Dr. Robert, " \
               "patient ID: 6060842, details: What has science done?"
    assert expected == lr.get_request()


# LabTest tests
def test_lab_test_make_request():
    lt = LabTest()
    lt.make_request(request_input)
    expected = "sent by: Dr. Pipper, sent to: Dr. Robert, " \
               "patient ID: 6060842, details: We applied the cortical " \
               "electrodes but were unable to get a neural response."
    assert expected == lt.get_request()


def test_lab_test_enter_results():
    lt = LabTest()
    lt.make_request(request_input)
    lt.enter_results("Survey says: not great", [])
    expected_string = "Survey says: not great"
    expected_list = []
    (result_string, result_list) = lt.get_results()
    assert expected_string == result_string
    assert expected_list == result_list


