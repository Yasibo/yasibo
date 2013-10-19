#!/usr/bin/python
# -*- coding: utf-8 -*-

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.


class Commands:
    def __init__(self):
        self.list = {}

    def addCommand(self, cmd):
        for name, value in inspect.getmembers(cmd, inspect.ismethod):
            if getattr(value, '_botcmd', False):
                name = getattr(value, '_botcmd_name')
                self.commands[name] = value
                log.debug("Added command \"%s\" to command list" % name)


    def remCommand(self, cmd):
        for name, value in inspect.getmembers(cmd, inspect.ismethod):
            if getattr(value, '_botcmd', False):
                name = getattr(value, '_botcmd_name')
                if name in self.commands:
                    del(self.commands[name])
