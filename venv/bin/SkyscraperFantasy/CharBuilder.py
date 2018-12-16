import json
import logging


class CharBuilder:

    def __init__(self):
        logging.basicConfig(level=logging.INFO)
        logging.info('Character Builder Initializing...')
        versionJSON = json.load(open("data/default/version.json"))
        self.version = (versionJSON['major'], versionJSON['minor'], versionJSON['patch'], versionJSON['tag'])
        self.version_text = f"{self.version[0]}.{self.version[1]}.{self.version[2]}-{self.version[3]}" if self.version[3] is not "" else f"{self.version[0]}.{self.version[1]}.{self.version[2]}"
        logging.info(f"Character Builder Version {self.version_text}")

        logging.info('Loading Races...')
        raceJSON = json.load(open("data/default/races.json"))
        self.races = list()
        for race in raceJSON:
            self.races.append(Race(race))
        logging.info(f"Loaded {len(self.races)} races.")


class Race:

    def __init__(self, json_data):
        self.name = json_data['name']
        self.description = json_data['description']
        self.deity = json_data['deity']
        self.traits = json_data['traits']

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"{self.name}"


class Skill:
    pass


class Ability:
    pass


class Trait:
    pass
