class Medication:
    def __init__(self, unique_id, medicine_name, chemical_name, synonym, suppress):
        self.id = unique_id
        self.medicine_name = medicine_name
        self.chemical_name = chemical_name
        self.synonym = synonym
        self.suppress = suppress

    def get_scientific_name(self):
        """
        Return all scientific names of a drug
        :return: list of scientific drugs
        """
        return self.scientific_name

    @property
    def get_market_names(self):
        """
       Return all the market names of drug
       :return: list of drug market names
       """
        return self.market_names

    def set_scientific_name(self, name):
        """
        :param name: scientific name of medicine
        :return: None
        """
        self.scientific_name = name

    def set_market_names(self, market_names):
        """
        :param  market_names: Market names of medicine
        :return: None
        """
        self.market_names = market_names

    def __str__(self):
        return f"""
        Medicine Name: {self.medicine_name}
        Chemical Name: {self.chemical_name}
        Synonym: {self.synonym}
        Suppress: {self.suppress}
        """
