import tornado.ioloop
import tornado.web
import tornado.options
import routers
from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)

if __name__ == "__main__":
    app = tornado.web.Application(routers.router)
    app.listen(options.port)
    print 'Server running on http://0.0.0.0:%d' % (options.port)
    tornado.ioloop.IOLoop.current().start()