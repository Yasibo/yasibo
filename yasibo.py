#!/usr/bin/python
# -*- coding: utf-8 -*-

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import irc.client

from plugin import PluginManager

class Yasibo(irc.client.SimpleIRCClient):
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
                self._register_event(event, function)
                print("%s registered: %s" % (plugin.name, event))
        
        # Initialize bot
        self.connect(server, port, nickname)
        
    def _register_event(self, event, handler, priority=0):
        self.ircobj.add_global_handler(event, handler, priority)

    def join(self, channel):
        self.connection.join(channel)

    def msg(self, channel, msg):
        self.connection.privmsg(channel, msg)

    def on_pubmsg(self, c, e):
        try:
            #addressee
            a = e.arguments[0].split(":", 1)
            if len(a) > 1 and irc.strings.lower(a[0]) == irc.strings.lower(self.connection.get_nickname()):
                self.do_command(e, a[1].strip())
            print("----")
            print(str(e.type))
            print(str(e.source))
            print(str(e.target))
            # This breaks on Regex
            print(str(e.arguments))
        except:
            print("I AM SLAIN!")
    
    def do_command(self, e, cmd):
        nick = e.source.nick
        c = self.connection
        import re

        m = re.search('tell (.+?) to (.+?)\.', cmd)
        if m:
            msg = m.group(1)
            who = m.group(2)
            c.notice(who, msg)
        else:
            c.notice(nick, "Not understood: " + cmd)
        
    def on_join(self, c, e):
        c.privmsg(e.target, "HELLO FRIENDS!")
        pass
        
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
    