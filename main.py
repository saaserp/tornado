import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.options

from tornado.options import define,options

define("port",default=8000,type = int)

class MainHandler(tornado.web.RequestHandler):
    def get(self):
    	arg = self.get_argument('q','hello')
        self.write("Hello, world"+arg)

application = tornado.web.Application([
    (r"/", MainHandler),
])

if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(MainHandlers=[(r"/",MainHandler)])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
