import web
import commands
urls=(
    '/','git',   
)

class git:
    def GET(self):
        (status,output) = commands.getstatusoutput('git pull origin master')
        return 'output:'+output

if __name__ == "__main__":
    app = web.application(urls,globals())
    app.run()

