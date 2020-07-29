from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta

wall_e=db.movies.find_one({'title': '월-E'})
target_movie = db.movies.find_one({'title': '월-E'})

same_point_movies= list(db.movies.find(
    {'point': wall_e['point']}
))

for movie in same_point_movies:
    db.movies.update_one(
        {'title':movie['title']},
        {'$set': {'point':'0''}}
                          )

    print('updated'+ movie['title'])
