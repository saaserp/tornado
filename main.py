import os.path

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')

class ContentHandler(tornado.web.RequestHandler):
    def post(self):
        n1 = self.get_argument('n1')
        n2 = self.get_argument('n2')
        n3 = self.get_argument('n3')
        self.render('content.html', n1=n1, n2=n2, n3=n3)


if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application(
            handlers=[(r'/', IndexHandler), (r'/content', ContentHandler)],
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path = os.path.join(os.path.dirname(__file__), "static")
            )

    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
