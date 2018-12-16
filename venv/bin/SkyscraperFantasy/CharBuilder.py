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
        races = list()
        for race in raceJSON:
            races.append(Race(race))
        self.races = {race.name:race for race in races}
        logging.info(f"Loaded {len(self.races)} races.")

        logging.info('Loading Skills...')
        skills = list()
        skillJSON = json.load(open('data/default/skills.json'))
        for skill in skillJSON:
            skills.append(Skill(skill))

        self.skills = {skill.name:skill for skill in skills}
        logging.info(f'Loaded {len(self.skills)} skills.')



        logging.info('Loading Traits...')
        traits = list()
        traitJSON = json.load(open('data/default/traits.json'))
        for trait in traitJSON:
            traits.append(Trait(trait))


        self.traits = {x.id:x for x in traits}

        logging.info(f'Loaded {len(self.traits)} traits.')



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


class Trait:

    def __init__(self, j):
        self.name = j['name']
        self.id = j['id']
        self.type = j['type']
        self.description = j['description']



class Ability:
    pass



class Rank(IntEnum):
    A = 5
    B = 4
    C = 3
    D = 2
    E = 1
    U = 0
    X = -1
