import pandas as pd

class DatabaseTable:

    def __init__(self, name = None, reviewTableName = None, userTableName = None, restaurantTableName = None):
        self.name = name
        self.reviewTableName = reviewTableName
        self.userTableName = userTableName
        self.restaurantTableName = restaurantTableName

    def find_all(self, db):
        return db[self.name].find({})

    def find_count(self, db):
        return db[self.name].find({}).count()

    def toDataFrame(self, cursor):
        return pd.DataFrame(list(cursor))
