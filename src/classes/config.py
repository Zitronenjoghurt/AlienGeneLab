import json
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
GENE_FILE_PATH = os.path.join(current_dir, '..', 'config.json')

class Config:
    __instance = None

    def __init__(self) -> None:
        self.settings = {}
        with open(GENE_FILE_PATH, 'r') as json_file:
            data = json.load(json_file)
            configurations = data.items()

            for setting in configurations:
                self.settings[setting[0]] = setting[1]

    def get_instance():
        if Config.__instance is None:
            Config.__instance = Config()
        return Config.__instance

    def get_setting(self, setting):
        return self.settings[setting]
    
    def get_personality_expression(self):
        setting = self.get_setting('personality_expression')
        return {int(key): int(value) for key, value in setting.items()}