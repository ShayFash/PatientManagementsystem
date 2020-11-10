import Names.Fullname as Name

#W.I.P
class Note:

    def __init__(self):
        """
        :return: Note object
        """
        self.date = []
        self.body = ''
        self.author = new Name

    def write_date(self, day, month, year):
        """
        Assigns given date values to Note object
        :params: day, month, year
        """
        self.Date[0] = Day
        self.Date[1] = Month
        self.Date[2] = Year

    def write_body(self, body_text:str):
        """
        Writes given body_text to Note object
        :param body_text: A string containing the note's body
        """
        self.body = body_text

    def write_author(self, author_name:Name):
        """
        Writes author's name to the Note object
        :param author_name: A FullName object
        """
        self.author = author_name

    def get_date(self):
        """
        :return: List[] containing Note object's date
        """
        return self.date

    def get_author(self):
        """
        :return: FullName Object containing author's name
        """
        return self.author #Consider other options as this returns a FullName Object

    def get_body(self):
        """
        :return: str containing the Note's body
        """
        return self.body

    def toString(self):
        """
        :return: String representation of the Note
        """
        #Print Date
        print('Date: ' + self.date[0] + '/' #Day
            + self.date[1] + '/'            #Month
            + self.date[2] + '/n')          #Year
        
        #Print Author's Name
        print('Author: ' + author.get_full_name_to_string() + '/n')

        #Print Note Body
        print(self.body)
   