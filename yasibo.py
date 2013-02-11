#!/usr/bin/python
# -*- coding: utf-8 -*-

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import irc.client

from plugin import PluginManager

class Yasibo(irc.client.SimpleIRCClient):
    _join_handlers = []
    _pubmsg_handlers = []

    def __init__(self, nickname, server, port=6667):
        irc.client.SimpleIRCClient.__init__(self)
        
        # Initialize variables
        self.plugman = PluginManager()
        
        # Initialize plugins
        for plugin in self.plugman.manager.getAllPlugins():
            print(plugin.name)
            handlers = plugin.plugin_object.get_events_to_handle()
            for handler in handlers:
                event, function = handler
                getattr(self, "register_on_" + event)(function)
                print("%s registered: %s" % (plugin.name, event))
        
        # Initialize bot
        self.connect(server, port, nickname)

    def join(self, channel):
        self.connection.join(channel)

    def msg(self, channel, msg):
        self.connection.privmsg(channel, msg)

    ###
    ### Events
    ###
    
    def register_on_join(self, function):
        self._join_handlers.append(function)
        
    def on_join(self, connection, event):
        for handler in self._join_handlers:
            handler(connection, event)
        
    def register_on_pubmsg(self, function):
        self._pubmsg_handlers.append(function)
        
    def on_pubmsg(self, connection, event):
        for handler in self._pubmsg_handlers:
            handler(connection, event)
        
if __name__ == "__main__":
    import sys
    if len(sys.argv) != 5:
        print("Usage: yasibo <nickname> <channel> <server> <port>")
        sys.exit(1)

    nickname = str(sys.argv[1])
    channel = str(sys.argv[2])
    server = str(sys.argv[3])
    port = int(sys.argv[4])

    bot = Yasibo(nickname, server, port)
    bot.join(channel)
    bot.start()
    