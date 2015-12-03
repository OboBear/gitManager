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
