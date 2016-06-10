import web

urls = (
    '/', 'index',
)

render = web.template.render('templates/')

db = web.database(dbn='sqlite', db='MovieSite.db')

class index:
    def GET(self):
        movies = db.select('movie')
        return render.index(movies)

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()

