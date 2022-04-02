import json

class BotSettings:

    def __init__(self, path):
        self.path = path
        self.settings = self.load_settings()

    def load_settings(self):
        with open(self.path, 'r') as f:
            return json.load(f)
