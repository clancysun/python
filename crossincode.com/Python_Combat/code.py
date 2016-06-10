import web

urls = (
    '/', 'index',
    'movie/(\d+)', 'movie',
)

#movies = [
#    {
#        'title': 'Forrest Gump',
#        'year': 1994,
#    },
#    {
#        'title': 'Titanic',
#        'year': 1997,
#    },
#]

db = web.database(dbn='sqlite', db='MovieSite.db')

render = web.template.render('templates/')

class movie:
    def GET(self, movie_id):
        #movie_id = int(movie_id)
        #movie = db.select('movie', where='id=$movie_id', vars=locals())[0]
        condition = 'id=' + movie_id
        movie = db.select('movie', where=condition)[0]
        return render.movie(movie)

class index:
    def GET(self):
        #return "Hello, world!"

        #page = ''
        #for m in movies:
        #    page += '%s (%d)\n' % (m['title'], m['year'])
        #return page

        #return render.index(movies)

        movies = db.select('movie')
        return render.index(movies)

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
