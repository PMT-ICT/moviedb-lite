import json
from tempfile import NamedTemporaryFile

import csv
import shutil
from uuid import uuid4

from schema import Schema, Or, SchemaError, Optional

from imdblite.config import MOVIES_DB

fields = ['id', 'uuid', 'json']

movie_schema = Schema({
    'name': str,
    'score': Or(int, float),
    Optional('uuid'): str,
    Optional('links'): {'self': str},
    'platforms': [str],
    'studio': str
})

def _movie_dto(row):
    return {
        'uuid': row['uuid'],
        'links': {
            'self': f'/movie/{row["uuid"]}'
        },
        **json.loads(row['json'])
    }

def top10():
    return sorted(
        get_movies(),
        key=lambda m: m['score'],
        reverse=True
    )[0:10]


def get_movies():
    with open(MOVIES_DB, 'r') as csv_file:
        reader = csv.DictReader(csv_file, fields, delimiter=';')
        movies = [_movie_dto(row) for row in reader]
    
    return movies

def get_movie(uuid):
    with open(MOVIES_DB, 'r') as csv_file:
        reader = csv.DictReader(csv_file, fields, delimiter=';')

        try:
            return next(
                _movie_dto(row) for row in reader
                if row['uuid'] == uuid
            )
        except StopIteration:
            return 'Movie not found.', 404

def add_movie(body):
    try:
        movie_schema.validate(body)
    except SchemaError as e:
        return str(e), 400

    movies = get_movies()
    id = len(movies) + 1
    uuid = uuid4()

    with open(MOVIES_DB, 'a') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fields, delimiter=';')
        writer.writerow({'id': id, 'uuid': uuid, 'json': json.dumps(body)})


def update_movie(uuid, body):
    try:
        movie_schema.validate(body)
    except SchemaError as e:
        return str(e), 400
    
    temp_file = NamedTemporaryFile(mode='w', delete=False)

    updated = False

    with open(MOVIES_DB, 'r') as csv_file, temp_file:
        reader = csv.DictReader(csv_file, fields, delimiter=';')
        writer = csv.DictWriter(temp_file, fields, delimiter=';')

        for row in reader:
            if row['uuid'] == uuid:
                old_json = json.loads(row['json'])
                new_json = json.dumps({**old_json, **body})
                new_row = {**row, 'json': new_json}
                writer.writerow(new_row)
                updated = True
            else:
                writer.writerow(row)
    
    shutil.move(temp_file.name, MOVIES_DB)

    if updated:
        return body, 204
    return 'Movie not found.', 404

def delete_movie(uuid):
    temp_file = NamedTemporaryFile(mode='w', delete=False)
    deleted = False

    with open(MOVIES_DB, 'r') as csv_file, temp_file:
        reader = csv.DictReader(csv_file, fields, delimiter=';')
        writer = csv.DictWriter(temp_file, fields, delimiter=';')

        for row in reader:
            if row['uuid'] == uuid:
                deleted = True
                continue
            writer.writerow(row)

    shutil.move(temp_file.name, MOVIES_DB)

    if deleted:
        return 'Movie deleted.', 204
    return 'Movie not found.', 404