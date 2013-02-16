#!/usr/bin/python
# -*- coding: utf-8 -*-

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import logging

from yasibo.plugin import YasiboPlugin
from yasibo import botcmd
from yasibo import glue

log = logging.getLogger(__name__)

class Help(YasiboPlugin):
        
    @botcmd()
    def help(self, msg, args):
        """
        Usage: help <command>
        """
        split = args.split(' ', 1)
        cmd = split[0]
        nick = msg.source.nick
        
        log.debug("%s requested help on %s" % (nick, cmd))
        if cmd in glue.bot.commands:
            helpmsg = glue.bot.commands[cmd].__doc__
            for helpline in helpmsg.split('\n'):
                glue.bot.connection.notice(nick, helpline)
                
