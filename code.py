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




class command:
    def POST(self):
        postParams = web.input();
        commandName = postParams.get('command')
        print 'command:'+commandName+'\n'
        if commandName=="help":
            return ''' show git:列出仓库列表\n show auth:列出授权公钥\n create git'''
        return 'command'

class show:
    def POST(self):
        postParams = web.input();
        commandName = postParams.get('request')
        if commandName == 'repo':
            (status, output) = commands.getstatusoutput('ls ~/gitRepository/pythonServer/')
            return output;
        if commandName == 'auth'
            (status, output) = commands.getstatusoutput('cat ~/.ssh/authorized_keys')
            return output;
        

if __name__ == "__main__":
    app = web.application(urls,globals())
    app.run()
