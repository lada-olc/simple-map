import sqlite3
import json

from flask import Flask, render_template

app = Flask(__name__)



@app.route('/')
def index():
    connection = sqlite3.connect("space-race-hackathon.sqlite")
    connection.enable_load_extension(True)
    connection.execute("SELECT load_extension('mod_spatialite')")
    
    points = load_objects(connection, "points")
    lines = load_objects(connection, "lines")
    polygons = load_objects(connection, "polygons")

    connection.close()

    return render_template('simple-map.html', points=json.dumps(points), lines=json.dumps(lines), polygons=json.dumps(polygons))


def load_objects(connection, table_name):
    result = connection.execute(f"SELECT pkuid, name, description, asgeojson(geometry) FROM {table_name}")
    items = []
    for row in result:
        geometry = json.loads(row[3])
        geometry["properties"] = {"description": row[1] or ''}
        items.append(geometry)
    return items
