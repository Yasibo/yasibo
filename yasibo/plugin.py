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
        places.append("%s/plugins" % os.path.dirname(os.path.abspath(__file__)))
        
        PluginManagerSingleton.setBehaviour([ConfigurablePluginManager,
                                             VersionedPluginManager])
        self.manager = PluginManagerSingleton.get()
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
        
    def on_connect(self):
        for plugin in self.manager.getAllPlugins():
            if plugin.is_activated:
                plugin.plugin_object.on_connect()
        
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
        
    def _get_handlers(self, events):
        """
        This function is a convienience function which gets the method handler
        for an event in the format: _on_event
        
        Plugins need to also declare the _on_event function.
        """
        handlers = []
        for event in events:
            handlers.append((event, getattr(self, "_on_" + event)))
            
        return handlers
        
    def get_events_to_handle(self):
        """
        Plugins should implement this function to register for IRC events
        
        For supported IRC events see irc/events.py from:
            http://bitbucket.org/jaraco/irc
        """
        return None
        
    def on_connect(self):
        """
        Plugins should implement this function if they need to process something
        when the bot connects to an IRC server.
        """
        pass
    

if __name__ == "__main__":
    PluginManager()
