# -*- coding: UTF-8 -*-

import web
import commands

class command:
    def POST(self):
        postParams = web.input();
        commandName = postParams.get('command')
        print 'command:'+commandName+'\n'
        if commandName=="help":
            return ''' repo:列出git仓库列表\n auth:列出授权公钥\n'''
        return 'command'
