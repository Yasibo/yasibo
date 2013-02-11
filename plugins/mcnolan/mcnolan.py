#!/usr/bin/python
# -*- coding: utf-8 -*-

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import plugin

class Hello(plugin.YasiboPlugin):
    def get_events_to_handle(self):
        events = ["join", "pubmsg"]    
        return self._get_handlers(events)
        
    def _on_join(self, c, e):
        c.privmsg(e.target, "HELLO FRIENDS!")
        
    def _on_pubmsg(self, c, e):
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