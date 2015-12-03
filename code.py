# -*- coding: UTF-8 -*-  
#!/usr/bin/env python 
import web
import commands
import controller/index


urls=(
    '/','index',
    '/command','command',
    '/show','show'
)







        

if __name__ == "__main__":
    app = web.application(urls,globals())
    app.run()
