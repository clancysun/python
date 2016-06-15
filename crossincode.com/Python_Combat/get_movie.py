# -*- coding: utf-8 -*-
import urllib
import json
import time
import web

db = web.database(dbn='sqlite', db='MovieSite.db')

movie_ids = []
for index in range(0, 250, 50):
    print index
    response = urllib.urlopen('http://api.douban.com/v2/movie/top250?start=%d&count=50' % index)
    data = response.read()
    # print data
    if 'msg' in data:
        print data
        break

    data_json = json.loads(data)
    movie250 = data_json['subjects']
    for movie in movie250:
        movie_ids.append(int(movie['id']))
        print movie['id'], movie['title']
    time.sleep(3)
print movie_ids

def add_movie(data):
    movie = json.loads(data)
    db.insert('movie',
        id=int(movie['id']),
        title=movie['title'],
        origin=movie['original_title'],
        url=movie['alt'],
        rating=movie['rating']['average'],
        image=movie['images']['large'],
        directors=','.join([d['name'] for d in movie['directors']]),
        casts=','.join([c['name'] for c in movie['casts']]),
        year=movie['year'],
        genres=','.join(movie['genres']),
        countries=','.join(movie['countries']),
        summary=movie['summary'],
    )
    print movie['title']

count = 0
for mid in movie_ids:
    print count, mid
    response = urllib.urlopen('http://api.douban.com/v2/movie/subject/%s' % mid)
    data = response.read()
    if 'msg' in data:
        print data
    else:
        add_movie(data)
        count += 1
    time.sleep(3)
