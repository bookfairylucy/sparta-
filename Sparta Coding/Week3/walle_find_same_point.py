from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta

wall_e=db.movies.find_one({'title': '월-E'})
target_movie = db.movies.find_one({'title': '월-E'})

same_point_movies= list(db.movies.find(
    {'point': wall_e['point']}
))

print(same_point_movies)

for movie in same_point_movies:
    print(movie['title'])
