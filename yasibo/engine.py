#!/usr/bin/python
# -*- coding: utf-8 -*-

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import inspect
import logging
import time

from yasibo.plugin import PluginManager
from yasibo import glue

log = logging.getLogger(__name__)


class Engine:
    def __init__(self):
        glue.bot = self
        self.commands = {}
        glue.plugman = PluginManager()

    def main_loop(self):
        while(1):
            self.process_events()
            time.sleep(0.1)

    def start(self):
        self.main_loop()

    def process_events(self):
        pass


    def add_botcmd(self, cmd):
        for name, value in inspect.getmembers(cmd, inspect.ismethod):
            if getattr(value, '_botcmd', False):
                name = getattr(value, '_botcmd_name')
                self.commands[name] = value
                log.debug("Added command \"%s\" to command list" % name)

    def del_botcmd(self, cmd):
        for name, value in inspect.getmembers(cmd, inspect.ismethod):
            if getattr(value, '_botcmd', False):
                name = getattr(value, '_botcmd_name')
                if name in self.commands:
                    del(self.commands[name])
