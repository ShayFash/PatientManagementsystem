class Name:
    """
    <<interface>> Name
    """

    def get_name(self):
        """

        :return:
        """
        pass

    def set_name(self, name):
        """

        :param name:
        :return:
        """
        pass


class GivenName(Name):
    """
    The given name of a person.
    """

    def __init__(self):
        """
        Default Constructor.
        """
        self.givenName = ""

    def get_name(self):
        """
        :return: Given name as a string.
        """
        return self.givenName

    def set_name(self, name):
        """
        :param name: Set name to a string.
        :return: None.
        """
        self.givenName = name


class MiddleNames(Name):
    """
    A list of middle names in their legal order.
    """

    def __init__(self):
        """
        Default Constructor.
        List has a default empty first element to avoid getter exceptions.
        """
        self.middleNames = [""]

    def get_name(self):
        """
        :return: The first middle name in the list.
        """
        return self.middleNames[0]

    def get_names_list(self):
        """
        :return: The middle names as a list.
        """
        return self.middleNames

    def get_names_to_string(self):
        """
        :return: The middle names as a string.
        """
        return ' '.join(self.middleNames)

    def set_name(self, name_list):
        """
        :param name_list: A list of strings.
        :return: None.
        """
        self.middleNames = name_list


class Surname(Name):
    """
    The surname of a person.
    """

    def __init__(self):
        """
        Default constructor.
        """
        self.surname = ""

    def get_name(self):
        """
        :return: The name as a string.
        """
        return self.surname

    def set_name(self, name):
        """
        :param name: A string.
        :return: None.
        """
        self.surname = name


class PreferredName(GivenName):
    """
    Behaviour is like GivenName so nothing to add at the moment.
    """


class FullName:
    """
    Contains the full name of a person.
    """

    def __init__(self):
        """
        Default Constructor.
        Initializes names as empty, must set them manually.
        """
        self.given = GivenName()
        self.middle = MiddleNames()
        self.surname = Surname()
        self.preferred = PreferredName()

    def get_full_name_to_string(self):
        """
        :return: All names in their legal order as a string.
        """
        return self.given.get_name() + " " + self.middle.get_names_to_string() \
               + " " + self.surname.get_name()

    def get_preferred_name(self):
        """
        :return: Preferred name as a string.
        """
        return self.preferred.get_name()

    def get_given_name(self):
        """
        :return: Given name as a string.
        """
        return self.given.get_name()

    def get_surname(self):
        """
        :return: Surname as a string.
        """

    def get_middle_name_list(self):
        """
        :return: Middle names as a list.
        """
        return self.middle.get_names_list()

    def get_middle_names_to_string(self):
        """
        :return: Middle names as a string.
        """
        return self.middle.get_names_to_string()

    def set_middle_names(self, name_list):
        """
        Replaces middle name list with a new list.
        :param name_list: A list of strings.
        :return: None.
        """
        self.middle.set_name(name_list)

    def set_preferred_name(self, name):
        """
        :param name: Preferred name, a string.
        :return: None.
        """
        self.preferred.set_name(name)

    def set_surname(self, name):
        """
        :param name: Surname, a string.
        :return: None.
        """
        self.surname.set_name(name)

    def set_given_name(self, name):
        """
        :param name: Given name, a string.
        :return: None.
        """
        self.given.set_name(name)
