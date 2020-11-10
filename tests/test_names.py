import pytest
from Names import *


# GivenName tests
def test_given_name_getter_setter():
    gn = GivenName()
    gn.set_name(["Kenny"])
    assert ["Kenny"] == gn.get_name()


# MiddleNames tests
def test_middle_names_set_names():
    mn = MiddleNames()
    mn.set_name(["Gary", "Kaye"])
    assert ["Gary", "Kaye"] == mn.get_names_list()


def test_middle_names_get_name():
    mn = MiddleNames()
    mn.set_name(["William", "Thomas"])
    assert "William" == mn.get_name()


def test_middle_names_get_names_list():
    mn = MiddleNames()
    mn.set_name(["William", "Thomas"])
    assert ["William", "Thomas"] == mn.get_names_list()


def test_middle_names_get_names_to_string():
    mn = MiddleNames()
    mn.set_name(["William", "Thomas"])
    assert "William Thomas" == mn.get_names_to_string()


# Surname Tests
def test_surname_get_name():
    sn = Surname()
    sn.set_name("Riker")
    assert "Riker" == sn.get_name()


# FullName tests
def test_full_name_get_preferred_name():
    fn = FullName()
    fn.set_preferred_name("Dave")
    assert "Dave" == fn.get_preferred_name()


def test_full_name_get_middle_name_list():
    fn = FullName()
    fn.set_middle_names(["Lee", "Roy", "Jenkins"])
    assert ["Lee", "Roy", "Jenkins"] == fn.get_middle_name_list()


def test_full_name_get_middle_names_to_string():
    fn = FullName()
    fn.set_middle_names(["Lee", "Roy", "Jenkins"])
    assert "Lee Roy Jenkins" == fn.get_middle_names_to_string()


def test_full_name_get_surname():
    fn = FullName()
    fn.set_surname("Baesmintdwaellor")
    assert "Baesmintdwaellor" == fn.get_surname()


def test_full_name_get_full_name_to_string():
    fn = FullName()
    fn.set_given_name("David")
    fn.set_middle_names(["Lee", "Roy", "Jenkins"])
    fn.set_surname("Baesmintdwaellor")
    fn.set_preferred_name("Dave")
    assert "David Lee Roy Jenkins Baesmintdwaellor" == fn.get_full_name_to_string()