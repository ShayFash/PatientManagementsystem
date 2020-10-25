import pytest
from Names import *


# stub test
def test_stub():
	assert True


def test_middle_names_set_names():
	mn = MiddleNames()
	mn.set_name(["Gary", "Kaye"])
	assert ["Gary", "Kaye"] == mn.get_names_list()


def test_full_name_getters_setters():
	fn = FullName()
	fn.set_given_name("Robert")
	fn.set_middle_names(["Lee", "Roy", "Jenkins"])
	fn.set_surname("Baesmintdwaellor")
	fn.set_preferred_name("Bob")
	assert "Robert Lee Roy Jenkins Baesmintdwaellor" == fn.get_full_name_to_string()
