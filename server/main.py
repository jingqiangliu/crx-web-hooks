#!/usr/bin/env python

from google.appengine.ext import webapp
from google.appengine.ext.webapp import util

import handlers

def main():
    application = webapp.WSGIApplication([
            ('/', handlers.MainHandler),
            ('/hook/.*', handlers.HookHandler),
            ('/channel', handlers.ChannelHandler),
        ],
        debug=True)
    util.run_wsgi_app(application)

if __name__ == '__main__':
    main()
