import requests
import xml.etree.ElementTree as ET
import Medication

"""
Note - this needs to be an API Handler
"""

"""
XML is an inherently hierarchical data format, and the most natural way to represent it is with a tree. 
ET has two classes for this purpose - ElementTree represents the whole XML document as a tree, and Element represents a 
single node in this tree. Interactions with the whole document (reading and writing to/from files) are usually done on 
the ElementTree level.  Interactions with a single XML element and its sub-elements are done on the Element level.
"""

SEARCH_BY_MEDICINE_NAME_URL = 'https://rxnav.nlm.nih.gov/REST/drugs'

def get_remote_medicine_data(endpoint, parameter):
    response = requests.get(endpoint, params=parameter)
    if response.status_code == 200:
        tree = ET.fromstring(response.text)
        try:
            concept_Group = tree.find('drugGroup').find('conceptGroup').tag
            for drug_info in tree.findall('drugGroup'):
                medicine_name = drug_info.find('name').text
                chemical_name = drug_info.findall('conceptGroup')[0].find('conceptProperties')[1].text
                synonym = drug_info.findall('conceptGroup')[0].find('conceptProperties')[2].text
                unique_id = drug_info.findall('conceptGroup')[0].find('conceptProperties')[6].text
                suppress = drug_info.findall('conceptGroup')[0].find('conceptProperties')[5].text
                return Medication(unique_id, medicine_name, chemical_name, synonym, suppress)

        except Exception as e:
            print("This drug does not exist in our database")
            return "This drug does not exist in our database"

    else:
        print("Something went wrong with remote API server")
        return "Something went wrong with remote API server"

