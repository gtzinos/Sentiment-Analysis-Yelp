from .databaseTable import DatabaseTable
import pymongo

class Maps(DatabaseTable):

    def __init__(self, name):
        DatabaseTable.__init__(self, name)


    def find_restaurants(self, db, num):
        return db[self.name].find({}, {'_id':False,'name':True,'latitude':True, 
            'longitude':True, 'stars':True, 'neighborhood':True, 'address':True}).limit(num)
    
    def find_5star_restaurants(self,db, num):
        return db[self.name].find({'stars':5}, {'_id':False,'name':True,'latitude':True, 
        'longitude':True, 'stars':True, 'neighborhood':True, 'address':True}).limit(num)

    def find_wifi_restaurants(self, db, stars, num):
        return db[self.name].find({ "$and": [{ "$or": [{"attributes.WiFi":"paid"}, {"attributes.WiFi":"free"}] }, { "stars": {"$lte": stars} }] }, {'_id':False,'name':True,'latitude':True, 
        'longitude':True, 'stars':True, 'neighborhood':True, 'address':True, 'attributes':True}).limit(num)

    def find_wifi_tv_restaurants(self, db, stars, num):
        return db[self.name].find({ "$and": [{ "$or": [{"attributes.WiFi":"paid"}, {"attributes.WiFi":"free"}] }, { "attributes.HasTV": True }, { "stars": {"$lte": stars} }] }, {'_id':False,'name':True,'latitude':True, 
        'longitude':True, 'stars':True, 'neighborhood':True, 'address':True, 'attributes':True}).limit(num)

    def find_gfk_hh_os_rest(self, db, stars, num):
        return db[self.name].find({ "$and": [{"attributes.GoodForKids": True}, {"attributes.HappyHour": True}, {"attributes.OutdoorSeating": True}, { "stars": {"$lte": stars} }] }, {'_id':False,'name':True,'latitude':True, 
        'longitude':True, 'stars':True, 'neighborhood':True, 'address':True, 'attributes':True}).limit(num)

    def find_gfk_hh_os_rest_no_limit(self, db, stars):
        return db[self.name].find({ "$and": [{"attributes.GoodForKids": True}, {"attributes.HappyHour": True}, {"attributes.OutdoorSeating": True}, { "stars": {"$lte": stars} }] }, {'_id':False,'name':True,'latitude':True, 
        'longitude':True, 'stars':True, 'neighborhood':True, 'address':True, 'attributes':True})