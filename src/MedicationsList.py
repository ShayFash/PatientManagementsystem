from Medication import *


class MedicationsList:

    def __init__(self):
        self.medications = []

    def get_list(self):
        return self.medications

    def add_medication(self, medication: Medication):
        self.medications.append(medication)

    def remove_medication(self, medication: Medication):
        """
        This method search the medication to be removed from the list and then remove
        :param medication:
        :return: Returns True if medication found and removed successfully otherwise returns False
        """
        if len(self.medications) > 0:
            for med in self.medications[:]:
                if med.scientific_name == medication.scientific_name:
                    self.medications.remove(med)
                    return True
            return False

    def clear(self):
        """
        This method clears or removes all the medication from the list
        :return: None
        """
        self.medications.clear()
