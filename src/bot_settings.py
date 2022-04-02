import json

class BotSettings:

    def __init__(self):
        self.path = "settings/bot_settings.json"
        self.settings = self.load_settings()

    def load_settings(self):
        with open(self.path, 'r') as f:
            return json.load(f)
