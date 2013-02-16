#!/usr/bin/python
# -*- coding: utf-8 -*-

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

# python lib
import inspect
import logging

# 3rd party
import irc.client

# yasibo
from yasibo.db import DBManager
from yasibo.plugin import PluginManager
from yasibo import glue

log = logging.getLogger(__name__)

class Yasibo(irc.client.SimpleIRCClient):
    def __init__(self, nickname, server, port=6667):
        irc.client.SimpleIRCClient.__init__(self)
        glue.bot = self
        
        # Initialize variables
        self.commands = {}
        self.plugman = PluginManager()
        glue.plugman = self.plugman
        self._dbman = DBManager()
        glue._dbman = self._dbman
        
        # Initialize bot
        self.connect(server, port, nickname)
        log.info('Yasibo initialized')
        
    def register_event(self, event, handler, priority=0):
        self.ircobj.add_global_handler(event, handler, priority)
        
    def unregister_event(self, event, handler, priority=0):
        self.ircobj.remove_global_handler(event, handler, priority)
        
    def add_botcmd(self, cmd):
        for name, value in inspect.getmembers(cmd, inspect.ismethod):
            if getattr(value, '_botcmd', False):
                name = getattr(value, '_botcmd_name')
                self.commands[name] = value

        
    def del_botcmd(self, cmd):
        for name, value in inspect.getmembers(cmd, inspect.ismethod):
            if getattr(value, '_botcmd', False):
                name = getattr(value, '_botcmd_name')
                if name in self.commands:
                    del(self.commands[name])
        
    def _process_botcmd(self, connection, event):
        msg = event.arguments[0]
        
        if msg.startswith('!'):
            split = msg.split(' ', 1)
            cmd = split[0].lstrip('!')
            args = split[1]
            
            self.commands[cmd](args)
    
    def join(self, channel):
        self.connection.join(channel)

    def msg(self, channel, msg):
        self.connection.privmsg(channel, msg)
    
    ###
    ### Events
    ###
    def on_privmsg(self, connection, event):
        self._process_botcmd(connection, event)
            
    def on_pubmsg(self, connection, event):
        self._process_botcmd(connection, event)
