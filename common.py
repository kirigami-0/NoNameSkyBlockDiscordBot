import json


class Config:
    def __init__(self):
        with open('config.json', 'r') as f:
            self.config = json.load(f)
    
    def loadChannelId(self, key):
        return self.config["channel_id"][key]
