import pytest

from Labwork import *


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