#!/usr/bin/python
# -*- coding: utf-8 -*-

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import os
from ConfigParser import SafeConfigParser

from xdg.BaseDirectory import save_config_path, xdg_data_dirs

from yapsy.IPlugin import IPlugin
from yapsy.PluginManager import PluginManagerSingleton
from yapsy.ConfigurablePluginManager import ConfigurablePluginManager
from yapsy.VersionedPluginManager import VersionedPluginManager

class PluginManager(object):
    def __init__(self):
        """
        Initialize the PluginManager including:
            - plugin configuration directory
            - plugin search locations
        """
        config_path = save_config_path("yasibo")
        config_file = os.path.join(config_path, "plugins.conf")
        places = []
        [places.append(os.path.join(path, "yasibo", "plugins")) for path in xdg_data_dirs]
        
        PluginManagerSingleton.setBehaviour([ConfigurablePluginManager,
                                             VersionedPluginManager])
        self.manager = PluginManagerSingleton.get()
        self.manager.setPluginPlaces(places)
        
        parser = SafeConfigParser()
        parser.read(config_file)
        self.manager.setConfigParser(parser, self.save)
        
    def save(self):
        """
        Saves the plugin configuration to file.
        """
        f = open(self.config_file, "w")
        self.config.write(f)
        f.close()
        
class YasiboPlugin(IPlugin):
    def activate(self):
        print("Plugin Activated: %s" % self.name)
        
    def deactivate(self):
        print("Plugin Deactivated")
    

if __name__ == "__main__":
    PluginManager()