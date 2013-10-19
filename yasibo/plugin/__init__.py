#!/usr/bin/python
# -*- coding: utf-8 -*-

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

# python lib
import logging
import os
from configparser import SafeConfigParser

# 3rd party
from xdg.BaseDirectory import save_config_path, xdg_data_dirs

from yapsy.IPlugin import IPlugin
from yapsy.PluginManager import PluginManagerSingleton
from yapsy.ConfigurablePluginManager import ConfigurablePluginManager
from yapsy.VersionedPluginManager import VersionedPluginManager

# yasibo
from yasibo import glue

log = logging.getLogger(__name__)


class PluginManager(object):
    def __init__(self):
        """
        Initialize the PluginManager including:
            - plugin configuration directory
            - plugin search locations
        """
        self.config_path = save_config_path("yasibo")
        self.config_file = os.path.join(self.config_path, "plugins.conf")
        places = []
        [places.append(os.path.join(path, "yasibo", "plugins")) for path in xdg_data_dirs]
        # dev location
        places.append("%s/../plugins" % os.path.dirname(os.path.abspath(__file__)))

        PluginManagerSingleton.setBehaviour([ConfigurablePluginManager,
                                             VersionedPluginManager])
        self.manager = PluginManagerSingleton.get()
        locator = self.manager.getPluginLocator()
        locator.setPluginInfoExtension("yasibo-plugin")
        self.manager.setPluginPlaces(places)

        self.config = SafeConfigParser()
        self.config.read(self.config_file)
        self.manager.setConfigParser(self.config, self.save)

        self.manager.collectPlugins()
        log.debug("Config file: %s" % self.config_file)

    def save(self):
        """
        Saves the plugin configuration to file.
        """
        f = open(self.config_file, "w")
        self.config.write(f)
        f.close()
