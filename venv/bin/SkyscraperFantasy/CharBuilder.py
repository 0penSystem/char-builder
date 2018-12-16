import json
import logging
from enum import IntEnum


class CharBuilder:

    def __init__(self):
        logging.basicConfig(level=logging.INFO, format='%(msg)s')
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

        logging.info('Loading Skills...')
        self.skills = list()
        skillJSON = json.load(open('data/default/skills.json'))
        for skill in skillJSON:
            self.skills.append(Skill(skill))
        logging.info(f'Loaded {len(self.skills)} skills.')

        self.skills.sort(key= lambda x: (x.type, x.name))
        currType = ""
        for skill in self.skills:
            if currType != skill.type:
                currType = skill.type
                logging.info(f"{currType} skills:")
            logging.info(f'\t{skill}')


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

    def __init__(self, j):
        self.name = j['name']
        self.type = j['type']
        self.description = j['description']
        self.default_rank = Rank[str.upper(j['default'])]

    def __str__(self):
        return f"{self.name} ({self.default_rank.name})"

    def __repr__(self):
        return f"{self.name} ({self.default_rank.name})"


class Ability:
    pass


class Trait:
    pass

class Rank(IntEnum):
    A = 5
    B = 4
    C = 3
    D = 2
    E = 1
    U = 0
    X = -1
