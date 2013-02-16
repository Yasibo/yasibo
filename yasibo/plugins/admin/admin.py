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

class Admin(YasiboPlugin):
    @botcmd(admin=True)
    def enable(self, msg, args):
        plugin = glue.plugman.manager.activatePluginByName(args)
        if plugin:
            log.info("%s activated." % args)
        else:
            log.info("%s plugin does not exist." % args)
    
    @botcmd(admin=True)
    def disable(self, msg, args):
        plugin = glue.plugman.manager.deactivatePluginByName(args)
        if plugin:
            log.info("%s deactivated." % args)
        else:
            log.info("%s plugin does not exist." % args)
        
    @botcmd(admin=True)
    def join(self, msg, args):
        if args.startswith('#'):
            log.debug("Joining %s" % args)
            glue.bot.join(args)
