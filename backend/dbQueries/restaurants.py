import pymongo
from .databaseTable import DatabaseTable

class Restaurants(DatabaseTable):

    def __init__(self, name):
        DatabaseTable.__init__(self, name)


    def find_top_restaurants(self, db, num):
        return db[self.name].find({}, {'_id': False}).sort([('review_count', pymongo.DESCENDING)]).limit(num)

    def get_restaurants_by_wifi(self, db):

        restaurants = db[self.name].aggregate([
            {
                "$group":
                {
                  "_id": "$attributes.WiFi",
                  "count": {"$sum": 1},
                  "review_count": {"$sum": "$review_count"},
                  "avg_review_count": {"$avg": "$review_count"},
                  "stars": {"$sum": "$stars"},
                  "avg_stars": {"$avg": "$stars"},
                },
            }
        ])

        restaurants = list(restaurants)
        output = []
        for restaurant in restaurants:
            if '_id' in restaurant:
                output.append(
                    {
                        "id": str(restaurant['_id']),
                        "count": restaurant['count'],
                        "review_count": restaurant['review_count'],
                        "avg_review_count": restaurant['avg_review_count'],
                        "stars": restaurant['stars'],
                        "avg_stars": restaurant['avg_stars']
                    }
                )

        return output

    @staticmethod
    def get_restaurant_list(db, restaurant_type, restaurantTableName):

      japaneseFilteredRestaurants = db[restaurantTableName].find({"categories": restaurant_type})
      japaneseRestaurantsList = list(japaneseFilteredRestaurants)
      outputList = []
      for restaurant in japaneseRestaurantsList:
        if '_id' in restaurant:
          outputList.extend(
            {
              str(restaurant['business_id'])
            }
          )

      return outputList
