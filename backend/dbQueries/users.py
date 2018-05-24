from .databaseTable import DatabaseTable
import pymongo

class Users(DatabaseTable):

    def __init__(self, name):
        DatabaseTable.__init__(self, name)

    def find_top_users(self, db, num):
        users = db[self.name].aggregate([ {
            "$group":
              {
                "_id": "$_id",
                "totalUseful": { "$sum": "$useful" }
              },
          }, {"$sort": {"totalUseful": -1}}, {"$limit": 10}
        ])

        users = list(users)

        for user in users:
            userDB = db[self.name].find_one({'_id': user['_id']})
            user['name'] = userDB['name']
            user['fans'] = userDB['fans']

        return users

    def get_users_per_year(self, db, num):
        users = db[self.name].aggregate([
            {
                "$group":
                {
                    "_id": {"$year": {"$dateFromString": {"dateString": "$yelping_since"}}},
                    "count": {"$sum": 1},
                    "useful": {"$sum": "$useful"},
                    "avg_useful": {"$avg": "$useful"},
                    "compliment_photos": {"$sum": "$compliment_photos"},
                    "avg_compliment_photos": {"$avg": "$compliment_photos"},
                    "compliment_list": {"$sum": "$compliment_list"},
                    "avg_compliment_list": {"$avg": "$compliment_list"},
                    "compliment_funny": {"$sum": "$compliment_funny"},
                    "avg_compliment_funny": {"$avg": "$compliment_funny"},
                    "funny": {"$sum": "$funny"},
                    "avg_funny": {"$avg": "$funny"},
                    "review_count": {"$sum": "$review_count"},
                    "avg_review_count": {"$avg": "$review_count"},
                    "fans": {"$sum": "$fans"},
                    "avg_fans": {"$avg": "$fans"},
                    "compliment_note": {"$sum": "$compliment_note"},
                    "avg_compliment_note": {"$avg": "$compliment_note"},
                    "compliment_plain": {"$sum": "$compliment_plain"},
                    "avg_compliment_plain": {"$avg": "$compliment_plain"},
                    "compliment_writer": {"$sum": "$compliment_writer"},
                    "avg_compliment_writer": {"$avg": "$compliment_writer"},
                    "compliment_cute": {"$sum": "$compliment_cute"},
                    "avg_compliment_cute": {"$avg": "$compliment_cute"},
                    "average_stars": {"$sum": "$average_stars"},
                    "avg_average_stars": {"$avg": "$average_stars"},
                    "compliment_more": {"$sum": "$compliment_more"},
                    "avg_compliment_more": {"$avg": "$compliment_more"},
                    "compliment_hot": {"$sum": "$compliment_hot"},
                    "avg_compliment_hot": {"$avg": "$compliment_hot"},
                    "cool": {"$sum": "$cool"},
                    "avg_cool": {"$avg": "$cool"},
                    "compliment_profile": {"$sum": "$compliment_profile"},
                    "avg_compliment_profile": {"$avg": "$compliment_profile"},
                    "compliment_cool": {"$sum": "$compliment_cool"},
                    "avg_compliment_cool": {"$avg": "$compliment_cool"}
                },
            }, {"$sort": {"_id": 1}}, {"$limit": num}
        ])

        users = list(users)
        output = []
        for review in reviews:
            if '_id' in review:
                output.append(
                    {
                        "id": str(review['_id']),
                        "count": review['count'],
                        "useful": review['useful'],
                        "avg_useful": review['avg_useful'],
                        "compliment_photos": review['compliment_photos'],
                        "avg_compliment_photos": review['avg_compliment_photos'],
                        "compliment_list": review['compliment_list'],
                        "avg_compliment_list": review['avg_compliment_list'],
                        "compliment_funny": review['compliment_funny'],
                        "avg_compliment_funny": review['avg_compliment_funny'],
                        "funny": review['funny'],
                        "avg_funny": review['avg_funny'],
                        "review_count": review['review_count'],
                        "avg_review_count": review['avg_review_count'],
                        "fans": review['fans'],
                        "avg_fans": review['avg_fans'],
                        "compliment_note": review['compliment_note'],
                        "avg_compliment_note": review['avg_compliment_note'],
                        "compliment_plain": review['compliment_plain'],
                        "avg_compliment_plain": review['avg_compliment_plain'],
                        "compliment_writer": review['compliment_writer'],
                        "avg_compliment_writer": review['avg_compliment_writer'],
                        "compliment_cute": review['compliment_cute'],
                        "avg_compliment_cute": review['avg_compliment_cute'],
                        "average_stars": review['average_stars'],
                        "avg_average_stars": review['avg_average_stars'],
                        "stars": review['stars'],
                        "avg_stars": review['avg_stars'],
                        "compliment_more": review['compliment_more'],
                        "avg_compliment_more": review['avg_compliment_more'],
                        "compliment_hot": review['compliment_hot'],
                        "avg_compliment_hot": review['avg_compliment_hot'],
                        "cool": review['cool'],
                        "avg_cool": review['avg_cool'],
                        "compliment_profile": review['compliment_profile'],
                        "avg_compliment_profile": review['avg_compliment_profile'],
                        "compliment_cool": review['compliment_cool'],
                        "avg_compliment_cool": review['avg_compliment_cool'],
                     } )

        return output
