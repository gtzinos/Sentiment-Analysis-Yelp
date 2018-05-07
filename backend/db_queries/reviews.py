
from database_table import DatabaseTable

class Reviews(DatabaseTable):
    def __init__(self, name):
        DatabaseTable.__init__(name)

    def find_random_reviews(db, num):
        random_reviews = db['reviews'].aggregate([{'$sample': {'size': num}}])
        random_reviews = list(random_reviews)

        for review in random_reviews:
            review['restaurant_name'] = db['restaurants'].find_one({'business_id': review['business_id']})['name']
            review['user_name'] = db['users'].find_one({'user_id': review['user_id']})['name']
        return random_reviews
