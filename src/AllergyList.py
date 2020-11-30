from Allergy import *

class AllergyList(object):
    """
    List of allergies of a patient.
    """

    def __init__(self):
        """

        """
        self.allergy_list = {
            'allergies': []
        }

    def get_allergies(self):
        """
        :return: the list of allergies.
        """
        return self.allergy_list['allergies']

    def get_allergies_to_string(self):
        """
        :return: the list of allergies as a string.
        """
        return ", ".join([str(allergy) for allergy in self.allergy_list['allergies']])

    def add_allergy(self, new_allergy: Allergy):
        """
        Adds a new allergy to the list of allergies
        :param new_allergy: must be of type Allergy.
        """
        if new_allergy not in self.allergy_list['allergies']:
            self.allergy_list['allergies'].append(new_allergy)

    def remove_allergy(self, allergy: Allergy):
        """
        Removes an allergy from the list of allergies.
        :param allergy: must be of type Allergy.
        """
        if allergy in self.allergy_list['allergies']:
            self.allergy_list['allergies'].remove(allergy)
