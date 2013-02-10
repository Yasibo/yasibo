import plugin

class Hello(plugin.YasiboPlugin):
    def get_events_to_handle(self):
        events = ["pubmsg"]
        handlers = []
        
        for event in events:
            handlers.append((event, getattr(self, "_on_pubmsg")))
            
        return handlers
        
    def _on_pubmsg(self, connection, event):
        msg = event.arguments[0]
        
        if "hello" in msg.lower():
            connection.privmsg(event.target, "Hello!")
