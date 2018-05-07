from database_table import DatabaseTable

class Users(DatabaseTable):

    def __init__(self, name):
        DatabaseTable.__init__(name)
