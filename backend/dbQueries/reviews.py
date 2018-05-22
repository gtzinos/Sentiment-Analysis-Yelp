
from .databaseTable import DatabaseTable

class Reviews(DatabaseTable):
    def __init__(self, name):
        DatabaseTable.__init__(self, name)

    def find_random_reviews(self, db, num):
        random_reviews = db[self.name].aggregate([{'$sample': {'size': num}}])
        random_reviews = list(random_reviews)

        for review in random_reviews:
            review['restaurant_name'] = db['restaurants'].find_one({'business_id': review['business_id']})['name']
            review['user_name'] = db['users'].find_one({'user_id': review['user_id']})['name']
        return random_reviews

    #stars != 3
    def get_filtered_reviews(self, db, useful = 1, limit = None):

        filtered = db[self.name].find({"stars" : {"$ne": 3}, "useful": {"$gte": useful}})

        if limit != None:
            filtered.limit(limit)

        filtered = list(filtered)

        for review in filtered:
            review['restaurant_name'] = db['restaurants'].find_one({'business_id': review['business_id']})['name']
            review['user_name'] = db['users'].find_one({'user_id': review['user_id']})['name']

        return filtered


