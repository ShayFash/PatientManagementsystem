from Names import FullName as Name

class Note():

    def __init__(self):
        """
        Properties:
            date: a list[]
            author: Names.FullName object
            body: str
        :return: Note object
        """
        self.note ={
            'date': [],
            'author': Name(),
            'body': ''
        }

    def write_date(self, day, month, year):
        """
        Assigns given date values to Note object
        :params: day, month, year
        """
        self.note['date'].append(day)
        self.note['date'].append(month)
        self.note['date'].append(year)


    def write_body(self, body_text:str):
        """
        Writes given body_text to Note object
        :param body_text: A string containing the note's body
        """
        self.note['body'] = body_text

    def write_author(self, author_name):
        """
        Writes author's name to the Note object
        :param author_name: A FullName object
        """
        self.note['author'] = author_name

    def get_date(self):
        """
        :return: String representation of the Note's date
        Day/Month/Year
        """
        try:
            date = (str(self.note['date'][0]) + '/'         #Day
                    + str(self.note['date'][1]) + '/'       #Month
                    + str(self.note['date'][2]))            #Year
        except:
            print("Error in displaying Date. Does date exist?")
        return date

    def get_author(self):
        """
        :return: FullName Object containing author's name
        """
        return self.note['author'].get_full_name_to_string() 

    def get_body(self):
        """
        :return: str containing the Note's body
        """
        return self.note['body']

    def toString(self):
        """
        :return: String representation of the Note
        """
        #Print Date
        date = self.get_date() + '\n'

        #Print Author's Name
        authors_name = 'Author: ' + self.get_author() + '\n'

        #Print Note Body
        body = self.get_body()

        return date + authors_name + body
