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
            'severity_description': severity,
            'medical_name': medical_name
        }

    def get_item(self):
        """
        :return: the item/allergy string name.
        """
        return self.allergy['item']

    def get_severity_description(self):
        """
        :return: the allergy severity description string.
        """
        return self.allergy['severity_description']

    def get_medical_name(self):
        """
        :pre-conditions: allergy must have a medical name.
        :return: scientific string name of the medicine allergy.
        """
        assert(self.allergy['medical_name'] is not None)
        return self.allergy['medical_name']

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
