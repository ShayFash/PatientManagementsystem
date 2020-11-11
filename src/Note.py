from Names import FullName as Name

class Note():

    def __init__(self):
        """
        Properties:
            date: a list[]
            body: str
            author: Names.FullName object
        :return: Note object
        """
        self.date = []
        self.body = ''
        self.author = Name()

    def write_date(self, day, month, year):
        """
        Assigns given date values to Note object
        :params: day, month, year
        """
        self.date.append(day)
        self.date.append(month)
        self.date.append(year)


    def write_body(self, body_text:str):
        """
        Writes given body_text to Note object
        :param body_text: A string containing the note's body
        """
        self.body = body_text

    def write_author(self, author_name):
        """
        Writes author's name to the Note object
        :param author_name: A FullName object
        """
        self.author = author_name

    def get_date(self):
        """
        :return: String representation of the Note's date
        Day/Month/Year
        """
        date = (str(self.date[0]) + '/'         #Day
                + str(self.date[1]) + '/'       #Month
                + str(self.date[2]))            #Year
        return date

    def get_author(self):
        """
        :return: String representation of author's fullname
        """
        return self.author.get_full_name_to_string() #Is a String representation of FullName more appropriate?

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
        try:
            date = ('Date: ' + str(self.date[0]) + '/'  #Day
                + str(self.date[1]) + '/'               #Month
                + str(self.date[2]) + '\n')             #Year
        except: 
            print("Error in displaying Date. Does date exist?")
        
        #Print Author's Name
        try:
            authors_name = 'Author: ' + self.author.get_full_name_to_string() + '\n'
        except: 
            print("Error in displaying Author's name. Does the author's name exist?")

        #Print Note Body
        body = self.body

        return date + authors_name + body

  