#!/usr/bin/python
# -*- coding: utf-8 -*-

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import logging
import threading

import tornado.ioloop
import tornado.web

from yasibo.plugin.yasibo import YasiboPlugin
from yasibo import botcmd
from yasibo import glue

log = logging.getLogger(__name__)


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

class WebServer(YasiboPlugin, threading.Thread):
    def __init__(self):
        super(WebServer, self).__init__()
        threading.Thread.__init__(self, name="yasibo-web")
        self.daemon = True  # Daemon threads will exit one app exists when True
        self.start()
        log.info('WebServer initialized.')

    def run(self):
        application = tornado.web.Application([
            (r"/", MainHandler),
        ])
        application.listen(8888)
        tornado.ioloop.IOLoop.instance().start()
