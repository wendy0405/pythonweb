from tornado.web import RequestHandler, HTTPError
class ErrorHandler():

    def prepare(self):
        super(ErrorHandler, self).prepare()
        self.set_status(404)
        raise HTTPError(404)