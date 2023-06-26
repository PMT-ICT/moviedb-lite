import json
from uuid import uuid4

from imdblite.config import ACTORS_DB, MOVIES_DB, PLATFORMS_DB, STUDIOS_DB


movies = [
    {"name": "Harry Potter and the Philosopher's Stone", "score": 7.2, "platforms": ["HBO"], 'studio': 'Warner Bros.'},
    {"name": "Harry Potter and the Chamber of Secrets", "score": 8.1, "platforms": ["HBO"], 'studio': 'Warner Bros.'},
    {"name": "Harry Potter and the Prisoner of Azkaban", "score": 9.3, "platforms": ["HBO"], 'studio': 'Warner Bros.'},
    {"name": "Harry Potter and the Goblet of Fire", "score": 8.5, "platforms": ["HBO"], 'studio': 'Warner Bros.'},
    {"name": "Harry Potter and the Order of the Phoenix", "score": 7, "platforms": ["HBO"], 'studio': 'Warner Bros.'},
    {"name": "Harry Potter and the Half-Blood Prince", "score": 9, "platforms": ["HBO"], 'studio': 'Warner Bros.'},
    {"name": "Harry Potter and the Deathly Hallows - Part 1", "score": 7, "platforms": ["HBO"], 'studio': 'Warner Bros.'},
    {"name": "Harry Potter and the Deathly Hallows - Part 2", "score": 8, "platforms": ["HBO"], 'studio': 'Warner Bros.'},

    {"name": "My Neighbour Totoro", "score": 9.9, "platforms": ["Netflix", "Disney+"], 'studio': 'Studio Ghibli'},
    {"name": "Kiki's Delivery Service", "score": 8, "platforms": ["Netflix"], 'studio': 'Studio Ghibli'},
    {"name": "Princess Mononoke", "score": 10, "platforms": ["Amazon Prime"], 'studio': 'Studio Ghibli'},

    {"name": "The Avengers", "score": 10, "platforms": ["Disney+"], 'studio': 'Marvel'},
    {"name": "Ant-man", "score": 8, "platforms": ["Disney+"], 'studio': 'Marvel'},
    {"name": "Guardians of the Galaxy", "score": 7, "platforms": ["Disney+"], 'studio': 'Marvel'}
]

actors = [
    {"first_name": "Daniel", "last_name": "Radcliffe"},
    {"first_name": "Rupert", "last_name": "Grint"},
    {"first_name": "Emma", "last_name": "Watson"},
    {"first_name": "John", "last_name": "Cleese"},
    {"first_name": "Robbie", "last_name": "Coltrane"},
    {"first_name": "Maggie", "last_name": "Smith"},
    {"first_name": "Warwick", "last_name": "Davis"},
    {"first_name": "Richard", "last_name": "Harris"},
    {"first_name": "John", "last_name": "Hurt"},
    {"first_name": "Alan", "last_name": "Rickman"},
    {"first_name": "Julie", "last_name": "Walters"},
    {"first_name": "Ian", "last_name": "Hart"},
    {"first_name": "Richard", "last_name": "Griffiths"},
    {"first_name": "Fiona", "last_name": "Shaw"},
]

studios = [
    {"name": "Marvel"},
    {"name": "Warner Bros."},
    {"name": "Studio Ghibli"}
]

platforms = [
    {"name": "Netflix"},
    {"name": "Amazon Prime"},
    {"name": "Disney+"},
    {"name": "HBO"},
    {"name": "Pathé Thuis"},
]

def create_entities(filename, entities):
    with open(filename, "a+") as csv_file:
        for id, entity in enumerate(entities, 1):
            uuid = uuid4()
            json_string = json.dumps(entity)
            csv_file.write(f"{id};{uuid};{json_string}\n")

if __name__ == "__main__":
    create_entities(MOVIES_DB, movies)
    create_entities(ACTORS_DB, actors)
    create_entities(STUDIOS_DB, studios)
    create_entities(PLATFORMS_DB, platforms)
    
    
