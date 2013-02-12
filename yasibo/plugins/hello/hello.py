#!/usr/bin/python
# -*- coding: utf-8 -*-

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from yasibo.plugin import YasiboPlugin

class Hello(YasiboPlugin):
    def get_events_to_handle(self):
        events = ["pubmsg"]    
        return self._get_handlers(events)
        
    def _on_pubmsg(self, connection, event):
        msg = event.arguments[0]
        
        if "hello" in msg.lower():
            connection.privmsg(event.target, "Hello!")
