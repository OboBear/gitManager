# -*- coding: UTF-8 -*-  
#!/usr/bin/env python 
import web
import commands
from controller.index import index
from controller.command import commands
from controller.show import show


urls=(
    '/','index',
    '/command','command',
    '/show','show'
)
        

if __name__ == "__main__":
    app = web.application(urls,globals())
    app.run()
