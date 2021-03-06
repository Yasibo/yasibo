#!/usr/bin/python
# -*- coding: utf-8 -*-

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.


import logging

from yasibo.plugin.yasibo import YasiboPlugin

log = logging.getLogger(__name__)


class HelloWorld(YasiboPlugin):

    def __init__(self):
        super(HelloWorld, self).__init__()
        log.info('Hello World!')
