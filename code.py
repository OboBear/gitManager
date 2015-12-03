# -*- coding: UTF-8 -*-  
#!/usr/bin/env python 
import web
import commands
import controller.index
import controller.command
import controller.show


urls=(
    '/','index',
    '/command','command',
    '/show','show'
)



class index:
    def GET(self):
        render = web.template.render('templates/')
        name = 'index'
        return render.index()



        

if __name__ == "__main__":
    app = web.application(urls,globals())
    app.run()
