import pymongo
from .databaseTable import DatabaseTable


class Reviews(DatabaseTable):
    def __init__(self, name):
        DatabaseTable.__init__(self, name)

    def find_random_reviews(self, db, num):
        random_reviews = db[self.name].aggregate([{'$sample': {'size': num}}])
        random_reviews = list(random_reviews)

        for review in random_reviews:
            review['restaurant_name'] = db['restaurants'].find_one(
                {'business_id': review['business_id']})['name']
            review['user_name'] = db['users'].find_one(
                {'user_id': review['user_id']})['name']
        return random_reviews

    # stars != 3
    def get_filtered_reviews(self, db, useful=1, limit=None):

        filtered = db[self.name].find(
            {"stars": {"$ne": 3}, "useful": {"$gte": useful}})

        if limit != None:
            filtered.limit(limit)

        filtered = list(filtered)

        for review in filtered:
            review['restaurant_name'] = db['restaurants'].find_one(
                {'business_id': review['business_id']})['name']
            review['user_name'] = db['users'].find_one(
                {'user_id': review['user_id']})['name']

        return filtered

    def find_top_reviews(self, db, num):
        reviews = db[self.name].aggregate([{
            "$group":
            {
                "_id": "$_id",
                "totalUseful": {"$sum": "$useful"}
            },
        }, {"$sort": {"totalUseful": -1}}, {"$limit": num}
        ])

        reviews = list(reviews)

        for review in reviews:
            review['text'] = db[self.name].find_one(
                {'_id': review['_id']})['text']

        return reviews

    def get_reviews_per_year(self, db, num):
        reviews = db[self.name].aggregate([
            {
                "$group":
                {
                    "_id": {"$year": {"$dateFromString": {"dateString": "$date"}}},
                    "count": {"$sum": 1},
                    "useful": {"$sum": "$useful"},
                    "avg_useful": {"$avg": "$useful"},
                    "stars": {"$sum": "$stars"},
                    "avg_stars": {"$avg": "$stars"}
                },
            }, {"$sort": {"_id": 1}}, {"$limit": num}
        ])

        reviews = list(reviews)
        output = []
        for review in reviews:
            if '_id' in review:
                output.append(
                    {
                        "id": str(review['_id']),
                        "count": review['count'],
                        "useful": review['useful'],
                        "avg_useful": review['avg_useful'],
                        "stars": review['stars'],
                        "avg_stars": review['avg_stars']
                    }
                )

        return output

    @staticmethod
    def get_goodUser_reviews(db, reviewTableName, goodReviewersList, restaurantList):

        filteredReviews = db[reviewTableName].find(
          {
            "user_id": {"$in": goodReviewersList},
            "business_id": {"$in": restaurantList},
            "useful": {"$gte": 1}
          })

        return filteredReviews

    def get_top_words(self, db, num):
        reviews = db[self.name].find({"useful": {"$gt": 100}})

        reviews = list(reviews)
        output = []
        for review in reviews:
            if '_id' in review:
                output.append(
                    {
                        "text": str(review['text'])
                    }
                )

        return output
