#!/usr/bin/python
# -*- coding: utf-8 -*-

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import logging
import sys

from yasibo.engine import Engine

logging.getLogger('').setLevel(logging.NOTSET)
logging.getLogger('yapsy').setLevel(logging.INFO)
logging.info('Initialize logger...')

bot = Engine()
bot.start()
