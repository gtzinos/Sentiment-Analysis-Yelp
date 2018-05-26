from .databaseTable import DatabaseTable
import pymongo

class Maps(DatabaseTable):

    def __init__(self, name):
        DatabaseTable.__init__(self, name)


    def find_restaurants(self, db, num):
        if(num==0):
            return db[self.name].find({}, {'_id':False,'name':True,'latitude':True, 
            'longitude':True, 'stars':True, 'neighborhood':True, 'address':True})
        else:
            return db[self.name].find({}, {'_id':False,'name':True,'latitude':True, 'longitude':True, 
            'stars':True, 'neighborhood':True, 'address':True}).limit(num)
    
    def find_5star_restaurants(self,db, num):
        return db[self.name].find({'stars':5}, {'_id':False,'name':True,'latitude':True, 
        'longitude':True, 'stars':True, 'neighborhood':True, 'address':True}).limit(num)

    def find_wifi_restaurants(self, db, num):
        return db[self.name].find({'attributes.WiFi': 'free'}, {'_id':False,'name':True,'latitude':True, 
        'longitude':True, 'stars':True, 'neighborhood':True, 'address':True, 'attributes':True}).limit(num)

    def find_good_for_kids(self, db, num):
        return db[self.name].find({'attributes.GoodForKids': True}, {'_id':False,'name':True,'latitude':True, 
        'longitude':True, 'stars':True, 'neighborhood':True, 'address':True, 'attributes.GoodForKids':True}).limit(num)

    def find_credit_reservations(self, db, num):
        return db[self.name].find({'attributes.BusinessAcceptsCreditCards':True, 'attributes.RestaurantsReservations':True}, {'_id':False,'name':True,'latitude':True, 
        'longitude':True, 'stars':True, 'neighborhood':True, 'address':True, 'attributes.BusinessAcceptsCreditCards':True, 'attributes.RestaurantsReservations':True}).limit(num)