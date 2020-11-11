import pytest
from Note import *
from Names import *

class Test_Note(object):
    
    def test_note_author():  
        test_note = Note()
        fn = FullName()
        fn.set_given_name("David")
        fn.set_middle_names(["Lee", "Roy", "Jenkins"])
        fn.set_surname("Baesmintdwaellor")
        fn.set_preferred_name("Dave")
        test_note.write_author(fn)
        assert test_note.get_author() == 'David Lee Roy Jenkins Baesmintdwaellor'

    def test_note_date():
        test_note = Note()
        test_note.write_date(7, 8, 2020)
        assert test_note.get_date() == '7/8/2020'
    
    def test_note_body():
        test_note = Note()
        test_note.write_body("This is the body of the note.")
        assert test_note.get_body() == "This is the body of the note."

    test_note_author()
    test_note_date()
    test_note_body()




