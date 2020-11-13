class AllergyList(object):
    """
    List of allergies of a patient.
    """

    def __init__(self):
        """

        """
        self.allergylist = {
            'allergies': []
        }

    def getAllergies(self):
        """
        :return: the list of allergies.
        """
        return self.allergylist['allergies']

    def getAllergiesToString(self):
        """
        :return: the list of allergies as a string.
        """
        return ", ".join([str(allergy) for allergy in self.allergylist['allergies']])

    def addAllergy(self, newAllergy):
        """
        Adds a new allergy to the list of allergies
        :param newAllergy: must be of type Allergy.
        """
        if newAllergy not in self.allergylist['allergies']:
            self.allergylist['allergies'].append(newAllergy)

    def removeAllergy(self, allergy):
        """
        Removes an allergy from the list of allergies.
        :param allergy: must be of type Allergy.
        """
        if allergy in self.allergylist['allergies']:
            self.allergylist['allergies'].remove(allergy)


class Allergy(object):
    """
    Class representation of a patient allergy.
    """

    def __init__(self, name, severity):
        """
        :param name: string name of the item/allergy.
        :param severity: string description of the severity of the allergy.
        """
        self.allergy = {
            'item': name,
            'severityDescription': severity
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
        return self.allergy['severityDescription']

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


class MedicineAllergy(Allergy):
    """
    Child class of Allergy.
    Allergy originating from a medicine
    """

    def __init__(self, name, severity, medicalName):
        """

        """
        super().__init__(name, severity)
        self.allergy['scientificName'] = medicalName

    def getScientificName(self):
        """
        :return: scientific string name of the medicine allergy.
        """
        return self.allergy['scientificName']
