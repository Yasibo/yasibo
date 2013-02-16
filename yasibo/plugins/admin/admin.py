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
    @botcmd
    def join(self, args):
        if args.startswith('#'):
            log.debug("Joining %s" % args)
            glue.bot.join(args)