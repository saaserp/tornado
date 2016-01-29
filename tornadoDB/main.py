from tornado import httpserver ,ioloop,web
from tornado.options import define,options
import torndb
import tornado.options
from handler import HANDLERS,TEMPLATE_PATH

define("port",default=9000,help="run on the given port",type=int)
define("mysql_host",default="127.0.0.1:3306",help="database host and port")
define("mysql_database",default="tornado",help="database name")
define("mysql_user",default="root",help="database user name")
define("mysql_password",default="123456",help="database password")

class Application(web.Application):
        def __init__(self):
            handlers=HANDLERS
            settings=dict(
                template_path=TEMPLATE_PATH,
                xsrf_cookies=False,
                cookie_secret = "11oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=",
            )

            web.Application.__init__(self,handlers,**settings)
        
            self.db=torndb.Connection(
                host = options.mysql_host,database = options.mysql_database,
                user = options.mysql_user,password = options.mysql_password             )


if __name__ == '__main__':
    tornado.options.parse_command_line()
    http_server = httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    ioloop.IOLoop.instance().start()
