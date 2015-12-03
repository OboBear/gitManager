import web
import commands

class index:
    def GET(self):
        render = web.template.render('templates/')
        name = 'index'
        return render.index()
