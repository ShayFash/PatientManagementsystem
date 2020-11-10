import Names.FullName as Name

//W.I.P
class Note:

    def __init__(self):
        self.date = []
        self.body = ''
        self.author = new Name

    def write_date(self, day, month, year):
        self.Date[0] = Day
        self.Date[1] = Month
        self.Date[2] = Year

    def write_body(self, body_text:str):
        self.body = body_text

    def write_author(self, author_name:Name):
        self.author = author_name

    def get_date(self):
        return self.date

    def get_author(self):
        return self.author //Consider other options as this returns a FullName Object

    def get_body(self):
        return self.body

    def toString(self):
        /* Print Date */
        print('Date: ' + self.date[0] + '/' //Day
            + self.date[1] + '/'            //Month
            + self.date[2] + /n)            //Year
        
        /* Print Author's Name */
        print('Author: ' + author.get_full_name_to_string + /n)

        /* Print Note Body */
        print(self.body)
   