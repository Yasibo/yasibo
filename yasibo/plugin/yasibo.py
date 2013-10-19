#!/usr/bin/python
# -*- coding: utf-8 -*-

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.


import logging

from yapsy.IPlugin import IPlugin

from yasibo import glue

log = logging.getLogger(__name__)


class YasiboPlugin(IPlugin):
    def activate(self):
        super(YasiboPlugin, self).activate()

        glue.bot.add_botcmd(self)

        log.info("Plugin Activated")

    def deactivate(self):
        super(YasiboPlugin, self).deactivate()

        glue.bot.del_botcmd(self)

        log.info("Plugin Deactivated")
