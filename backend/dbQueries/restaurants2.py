import pymongo
from .databaseTable import DatabaseTable


class Restaurants2(DatabaseTable):

    def __init__(self, name):
        DatabaseTable.__init__(self, name)

    def get_restaurants_by_neighborhood(self, db):
        restaurants = db[self.name].aggregate([
            {
                "$group": {
                    "_id": "$neighborhood", "count": {"$sum": 1}
                }
            }
        ])

        restaurants = list(restaurants)
        output = []
        for restaurant in restaurants:
            if '_id' in restaurant:
                output.append(
                    {
                        "neighborhood": str(restaurant['_id']),
                        "count": restaurant['count']
                    }
                )

        return output

    def get_restaurants_by_meals(self, db):
        output = []
        meals=['dessert','latenight','lunch','dinner','brunch','breakfast']

        for meal in meals:
            restaurants = db[self.name].aggregate([
                {
                    "$match": {"attributes.GoodForMeal."+meal: True}
                },
                {
                    "$group": {"_id": meal, "count": {"$sum":1}}
                }
            ])

            restaurants = list(restaurants)
            
            for restaurant in restaurants:
                if '_id' in restaurant:
                    output.append(
                        {
                            "meal": str(restaurant['_id']),
                            "count": restaurant['count']
                        }
                    )

        return output
