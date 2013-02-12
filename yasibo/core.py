#!/usr/bin/python
# -*- coding: utf-8 -*-

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import irc.client

from yasibo.plugin import PluginManager

from yasibo import glue

class Yasibo(irc.client.SimpleIRCClient):
    def __init__(self, nickname, server, port=6667):
        irc.client.SimpleIRCClient.__init__(self)
        glue.bot = self
        
        # Initialize variables
        self.plugman = PluginManager()
        glue.plugman = self.plugman
        
        # Initialize bot
        self.connect(server, port, nickname)
        
    def _register_event(self, event, handler, priority=0):
        self.ircobj.add_global_handler(event, handler, priority)
        
    def _unregister_event(self, event, handler, priority=0):
        self.ircobj.remove_global_handler(event, handler, priority)

    def join(self, channel):
        self.connection.join(channel)

    def msg(self, channel, msg):
        self.connection.privmsg(channel, msg)
        
