from flask import Flask, render_template
from config import *
from db_queries import *

db = openConnection(db_hostname, db_name, db_port)

top = find_count(db, "reviews")

print(top)
