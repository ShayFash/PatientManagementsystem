class Medication:
    def __init__(self):
        self.scientific_name = ''
        self.market_names = []

    def get_scientific_name(self):
        """
        Return all scientific names of a drug
        :return: list of scientifc drugs
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

    def set_market_names(self, market_name):
        """
        :param  market_name: Markets of medicine
        :return: None
        """
        self.market_names = market_name


