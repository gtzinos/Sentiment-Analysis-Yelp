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
        for user in users:
            if '_id' in user:
                output.append(
                    {
                        "id": str(user['_id']),
                        "count": user['count'],
                        "useful": user['useful'],
                        "avg_useful": user['avg_useful'],
                        "compliment_photos": user['compliment_photos'],
                        "avg_compliment_photos": user['avg_compliment_photos'],
                        "compliment_list": user['compliment_list'],
                        "avg_compliment_list": user['avg_compliment_list'],
                        "compliment_funny": user['compliment_funny'],
                        "avg_compliment_funny": user['avg_compliment_funny'],
                        "funny": user['funny'],
                        "avg_funny": user['avg_funny'],
                        "review_count": user['review_count'],
                        "avg_review_count": user['avg_review_count'],
                        "fans": user['fans'],
                        "avg_fans": user['avg_fans'],
                        "compliment_note": user['compliment_note'],
                        "avg_compliment_note": user['avg_compliment_note'],
                        "compliment_plain": user['compliment_plain'],
                        "avg_compliment_plain": user['avg_compliment_plain'],
                        "compliment_writer": user['compliment_writer'],
                        "avg_compliment_writer": user['avg_compliment_writer'],
                        "compliment_cute": user['compliment_cute'],
                        "avg_compliment_cute": user['avg_compliment_cute'],
                        "average_stars": user['average_stars'],
                        "avg_average_stars": user['avg_average_stars'],
                        "compliment_more": user['compliment_more'],
                        "avg_compliment_more": user['avg_compliment_more'],
                        "compliment_hot": user['compliment_hot'],
                        "avg_compliment_hot": user['avg_compliment_hot'],
                        "cool": user['cool'],
                        "avg_cool": user['avg_cool'],
                        "compliment_profile": user['compliment_profile'],
                        "avg_compliment_profile": user['avg_compliment_profile'],
                        "compliment_cool": user['compliment_cool'],
                        "avg_compliment_cool": user['avg_compliment_cool'],
                     } )

        return output

    @staticmethod
    def get_goodUsers_list(db, userTableName):

      filteredGoodUsers = db[userTableName].find(
        {"useful": {"$gte": 50},
         "compliment_profile": {"$gte": 1},
         "funny": {"$gte": 20},
         "cool": {"$gte": 10},
         "fans": {"$gte": 0},
         "average_stars": {"$gte": 1, "$lte": 4.5}
         }
      )

      goodUsersList = list(filteredGoodUsers)
      outputList = []
      for user in goodUsersList:
        if '_id' in user:
          outputList.extend(
            {
              str(user['user_id'])
            }
          )

      return outputList
