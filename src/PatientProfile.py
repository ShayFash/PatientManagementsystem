from Names import *
from Note import *
from Labwork import *
from Allergies import *
from Medication import *
from MedicationsList import *
from Demographics import *


class PatientProfile:
    def __init__(self, full_name, demographics: [], notes: [],
                 billing_code: str, medications: [], allergies: [], lab_work: []):
        """
        Constructor for PatientProfile.
        :param full_name: A FullName object.
        :param demographics: A list of Demographic objects.
        :param notes: A list of Note objects.
        :param billing_code: A string of numbers and/or characters.
        :param medications: A list of Medication objects.
        :param allergies: A list of Allergy objects
        :param lab_work: A list of LabWork objects.
        """
        self.profile = {
            'name': full_name,
            'demographics': demographics,
            'notes': notes,
            'billing_code': billing_code,
            'drugs': medications,
            'allergies': allergies,
            'lab_work': lab_work
        }

    def get_name(self):
        return self.profile['name']

    def get_demographics(self):
        return self.profile['demographics']

    def get_billing(self):
        return self.profile['billing_code']

    def get_notes(self):
        return self.profile['notes']

    def get_drugs(self):
        return self.profile['drugs']

    def get_lab_work(self):
        return self.profile['lab_work']
