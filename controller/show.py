# -*- coding: UTF-8 -*-
import __init__
#import web
#import commands

class show:
    def POST(self):
        postParams = web.input();
        commandName = postParams.get('request')
        if commandName == 'repo':
            (status, output) = commands.getstatusoutput('ls ~/gitRepository/pythonServer/')
            return output;
        if commandName == 'auth':
            (status, output) = commands.getstatusoutput('cat ~/.ssh/authorized_keys')
            return output;