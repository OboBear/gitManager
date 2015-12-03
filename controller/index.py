# -*- coding: UTF-8 -*-

import web
import commands

class index:
    def GET(self):
        return "index"
        render = web.template.render('templates/')
        name = 'index'
        return render.index()
