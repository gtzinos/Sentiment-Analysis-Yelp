from flask import Flask, render_template
from config import *
from db_queries import *

db = openConnection(db_hostname, db_name, db_port)

def relation_stars_with_textlength():
    global db

    restaurants = Restaurants(db_restaurants_table_name)

    restaurants.find_all(db)

top = find_count(db, "reviews")

print(top)
