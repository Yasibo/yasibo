#!/usr/bin/python
# -*- coding: utf-8 -*-

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import time

class Engine:
    def __init__(self):
        pass

    def main_loop(self):
        while(1):
            self.process_events()
            time.sleep(0.1)

    def start(self):
        self.main_loop()

    def process_events(self):
        pass
