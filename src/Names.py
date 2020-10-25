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

	"""

	def __init__(self):
		"""

		"""
		self.givenName = ""

	def get_name(self):
		"""

		:return:
		"""
		return self.givenName

	def set_name(self, name):
		"""

		:param name:
		:return:
		"""
		self.givenName = name


class MiddleNames(Name):
	"""

	"""

	def __init__(self):
		"""

		"""
		self.middleNames = []

	def get_name(self):
		"""

		:return:
		"""
		return self.middleNames

	def get_names_list(self):
		"""

		:return:
		"""
		return self.middleNames

	def get_names_to_string(self):
		"""

		:return:
		"""
		return ' '.join(self.middleNames)

	def set_name(self, name_list):
		"""

		:param name_list: a list of strings
		:return:
		"""
		self.middleNames = name_list.split(' ')


class Surname(Name):
	"""

	"""

	def __init__(self):
		"""

		"""
		self.surname = ""

	def get_name(self):
		"""

		:return:
		"""
		return self.surname

	def set_name(self, name):
		"""

		:param name:
		:return:
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

		"""
		self.given = GivenName()
		self.middle = MiddleNames()
		self.surname = Surname()
		self.preferred = PreferredName()

	def get_full_name_to_string(self):
		"""

		:return:
		"""
		return self.given.get_name() + self.middle.get_names_to_string() \
			+ self.surname.get_name()

	def get_preferred_name(self):
		"""

		:return:
		"""
		return self.preferred.get_name()

	def get_given_name(self):
		"""

		:return:
		"""
		return self.given.get_name()

	def get_middle_name_list(self):
		"""

		:return:
		"""
		return self.middle.get_names_list()

	def get_middle_names_to_string(self):
		"""

		:return:
		"""
		return self.middle.get_names_to_string()

	def set_middle_names(self, name_list):
		"""

		:param name_list:
		:return:
		"""
		self.middle.set_name(name_list)

	def set_preferred_name(self, name):
		"""

		:param name:
		:return:
		"""
		self.preferred.set_name(name)

	def set_surname(self, name):
		"""

		:param name:
		:return:
		"""
		self.surname.set_name(name)

	def set_given_name(self, name):
		"""

		:param name:
		:return:
		"""
		self.given.set_name(name)
