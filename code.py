# -*- coding: UTF-8 -*-  
#!/usr/bin/env python 
import web
import commands
urls=(
    '/','index',
    '/command','command',    
)

class index:
    def GET(self):
        render = web.template.render('templates/')
        name = 'index'
        return render.index() 

class command:
    def POST(self):
        postParams = web.input();
        commandName = postParams.get('command')
        print 'command:'+commandName+'\n'
        if commandName=="help":
            return ''' show git:列出仓库列表\n show auth:列出授权公钥\n create git'''
        return 'command'    
        



if __name__ == "__main__":
    app = web.application(urls,globals())
    app.run()
