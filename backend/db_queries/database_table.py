class DatabaseTable:

    def __init__(self, name):
        self.name = name

    def find_all(db):
      return db[self.name].find({})

    def find_count(db):
        return db[self.name].find({}).count()
