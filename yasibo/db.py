#!/usr/bin/python
# -*- coding: utf-8 -*-

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import logging
import sqlite3

log = logging.getLogger(__name__)

class DBManager(object):
    def __init__(self):
        log.info("DB initialized: SQLite3 v" + sqlite3.sqlite_version)
        self.conn = sqlite3.connect('yasibo.sqlite3')
        self.cur = self.conn.cursor()

    def selftest(self):
        try:
            self.raw_execute("DROP TABLE IF EXISTS dbtest")
            self.raw_execute("create table dbtest (id, value)")
            self.raw_execute("insert into dbtest values (%d, \"%s\")" % (5, "This is a test"))
            array = self.raw_fetch("select * from dbtest where id = %d" % 5)
            (id, value) = array[0]
            if id is 5 and value == "This is a test":
                self.raw_execute("DROP TABLE IF EXISTS dbtest")
                return True
            return False
        except:
            return False
        
    def get_version(self):
        return sqlite3.sqlite_version
        
    def raw_execute(self, command):
        try:
            self.cur.execute(command)
            return self.conn.commit()
        except:
            return None
        
    def raw_fetch(self, command):
        try:
            self.cur.execute(command)
            return self.cur.fetchall()
        except:
            return None