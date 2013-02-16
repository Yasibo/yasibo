#!/usr/bin/python
# -*- coding: utf-8 -*-

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import os.path
import random

from yasibo.plugin import YasiboPlugin

class Hello(YasiboPlugin):
    # List of keywords to respond to
    rspto = {"hi", "hello"}
    
    def __init__(self):
        super(Hello, self).__init__()
        self._dirname = os.path.dirname(__file__)
        self._rspfile = os.path.join(self._dirname, "responses.txt")
    
    def get_events_to_handle(self):
        events = ["pubmsg"]
        return self._get_handlers(events)
        
    def _on_pubmsg(self, connection, event):
        msg = event.arguments[0]
        s = self.rspto & set(msg.lower().split())
        if len(s):
            random_response = random.choice(open(self._rspfile).readlines()).rstrip()
            connection.privmsg(event.target, random_response)
