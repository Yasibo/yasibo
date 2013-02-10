#!/usr/bin/python
# -*- coding: utf-8 -*-

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import irc.client

class Yasibo(irc.client.SimpleIRCClient):
    def __init__(self, nickname, server, port=6667):
        irc.client.SimpleIRCClient.__init__(self)

        self.connect(server, port, nickname)

    def join(self, channel):
        self.connection.join(channel)

    def msg(self, channel, msg):
        self.connection.privmsg(channel, msg)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 5:
        print("Usage: yasibo <nickname> <channel> <server> <port>")
        sys.exit(1)

    nickname = str(sys.argv[1])
    channel = str(sys.argv[2])
    server = str(sys.argv[3])
    port = int(sys.argv[4])

    bot = Yasibo(nickname, server, port)
    bot.join(channel)
    bot.start()

