#!/usr/bin/python
# -*- coding: utf-8 -*-

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.


import logging

log = logging.getLogger(__name__)


class YasiboPlugin(IPlugin):
    def activate(self):
        super(YasiboPlugin, self).activate()

        glue.bot.add_botcmd(self)

        handlers = self.get_events_to_handle()
        if handlers is not None:
            for handler in handlers:
                event, function = handler
                glue.bot.register_event(event, function)
                log.debug("Registered event: %s" % (event))

        log.info("Plugin Activated")

    def deactivate(self):
        super(YasiboPlugin, self).deactivate()

        glue.bot.del_botcmd(self)

        handlers = self.get_events_to_handle()
        if handlers is not None:
            for handler in handlers:
                event, function = handler
                glue.bot.unregister_event(event, function)
                log.debug("Unregistered event: %s" % (event))

        log.info("Plugin Deactivated")
