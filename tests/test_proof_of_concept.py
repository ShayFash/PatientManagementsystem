import pytest
from Names import *


def test_middle_names_set_names():
    mn = MiddleNames()
    mn.set_name(["Gary", "Kaye"])
    assert ["Gary", "Kaye"] == mn.get_names_list()


def test_full_name_getters_setters():
    fn = FullName()
    fn.set_given_name("David")
    fn.set_middle_names(["Lee", "Roy", "Jenkins"])
    fn.set_surname("Baesmintdwaellor")
    fn.set_preferred_name("Dave")
    assert "David Lee Roy Jenkins Baesmintdwaellor" == fn.get_full_name_to_string()
