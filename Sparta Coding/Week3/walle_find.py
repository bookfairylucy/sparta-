from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta

wall_e=db.movies.find_one({'title': '월-E'})
target_movie = db.movies.find_one({'title': '월-E'})
print(wall_e)