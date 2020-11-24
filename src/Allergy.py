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

    def add_allergy(self, new_allergy):
        """
        Adds a new allergy to the list of allergies
        :param new_allergy: must be of type Allergy.
        """
        if new_allergy not in self.allergy_list['allergies']:
            self.allergy_list['allergies'].append(new_allergy)

    def removeAllergy(self, allergy):
        """
        Removes an allergy from the list of allergies.
        :param allergy: must be of type Allergy.
        """
        if allergy in self.allergy_list['allergies']:
            self.allergy_list['allergies'].remove(allergy)


class Allergy(object):
    """
    Class representation of a patient allergy.
    """

    def __init__(self, name, severity, medical_name=None):
        """
        :param name: string name of the item/allergy.
        :param severity: string description of the severity of the allergy.
        :param scientific_name: a string medical name of the
        """
        self.allergy = {
            'item': name,
            'severity description': severity,
            'medical name': medical_name
        }

    def getItem(self):
        """
        :return: the item/allergy string name.
        """
        return self.allergy['item']

    def getSeverityDescription(self):
        """
        :return: the allergy severity description string.
        """
        return self.allergy['severity description']

    def getMedicalName(self):
        """
        :pre-conditions: allergy must have a medical name.
        :return: scientific string name of the medicine allergy.
        """
        assert(self.allergy['medical name'] is not None)
        return self.allergy['medical name']

    def __eq__(self, other):
        """
        Overrides the equals boolean operator.
        :param other: must be of type Allergy.
        :return: True if other is equal to self, False otherwise.
        """
        return self.allergy['item'] == other.allergy['item']

    def __str__(self):
        """
        Overrides the __str__ method of this class.
        :return: a string representation of the allergy object (i.e. the name)
        """
        return self.allergy['item']


# class MedicineAllergy(Allergy):
#     """
#     Child class of Allergy.
#     Allergy originating from a medicine
#     """

#     def __init__(self, name, severity, medicalName):
#         """

#         """
#         super().__init__(name, severity)
#         self.allergy['scientificName'] = medicalName

#     def getScientificName(self):
#         """
#         :return: scientific string name of the medicine allergy.
#         """
#         return self.allergy['scientificName']
