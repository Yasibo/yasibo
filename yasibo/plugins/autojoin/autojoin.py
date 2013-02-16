#!/usr/bin/python
# -*- coding: utf-8 -*-

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import configparser
import logging

from yasibo.plugin import YasiboPlugin
from yasibo import botcmd
from yasibo import glue

log = logging.getLogger(__name__)

class AutoJoin(YasiboPlugin):
    channels = []
    
    def on_connect(self):
        try:
            channels = glue.plugman.manager.readOptionFromPlugin("Default", "AutoJoin", "channels")
            for channel in channels.split(','):
                self.channels.append(channel)
        except (configparser.NoSectionError, configparser.NoOptionError):
            log.debug("Config file non-existant or plugin section missing.")
            
        for channel in self.channels:
            glue.bot.join(channel)
            log.debug("Auto joined channel %s" % channel)
    
    def add_channel(self, channel):
        self.channels.append(channel)
        channels = ','.join(self.channels)
        glue.plugman.manager.registerOptionFromPlugin("Default", "AutoJoin", "channels", channels)
        log.info("Added channel %s from autojoin." % channel)
        
    def del_channel(self, channel):
        self.channels.remove(channel)
        log.info("Removed channel %s from autojoin." % channel)
        
    @botcmd(admin=True)
    def autojoin(self, args):
        """
        Usage: autojoin <channel>
        
        Adds a channel to the bot autojoin list. At next boot the bot will automatically join channels in list.
        """
        self.add_channel(args)
        
    @botcmd(admin=True)
    def unautojoin(self, args):
        """
        Usage: unautojoin <channe>
        
        Removes a channel from the bot autojoin list.
        """
        self.del_channel(args)
