#!/usr/bin/python
# -*- coding: utf-8 -*-

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

def botcmd(*args, **kwargs):
    """
    Decorator to declare a function as a bot command
    
    Parameters:
        name    = Name of the command
        admin   = Sets the command to be an admin command
                  Admin commands do not work in public channels user must msg
                  bot directly.
    """

    def create_botcmd(func, name=None, admin=False):
        if not hasattr(func, '_botcmd'):
            setattr(func, '_botcmd', True)
            setattr(func, '_botcmd_name', name or func.__name__)
            setattr(func, '_botcmd_admin', admin)
        return func

    return create_botcmd(args[0], **kwargs)