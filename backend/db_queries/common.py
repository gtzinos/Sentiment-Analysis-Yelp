def find_all(db, collection_name):
    return db[collection_name].find({})

def find_count(db, collection_name):
    return db[collection_name].find({}).count()
