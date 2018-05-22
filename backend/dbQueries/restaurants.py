import pymongo
from .databaseTable import DatabaseTable

class Restaurants(DatabaseTable):

    def __init__(self, name):
        DatabaseTable.__init__(self, name)


    def find_top_restaurants(self, db, num):
        return db[self.name].find({}, {'_id': False}).sort([('review_count', pymongo.DESCENDING)]).limit(num)


