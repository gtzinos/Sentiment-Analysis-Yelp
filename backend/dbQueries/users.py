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
