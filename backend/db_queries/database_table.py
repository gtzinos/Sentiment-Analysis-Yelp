class DatabaseTable:

    def __init__(self, name):
        self.name = name

    def find_all(self, db):
        return db[self.name].find({})

    def find_count(self, db):
        return db[self.name].find({}).count()
