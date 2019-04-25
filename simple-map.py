from flask import Flask, render_template, request
app = Flask(__name__)

import sqlite3

@app.route('/')
def index():
    connection = sqlite3.connect("space-race-hackathon.sqlite")
    connection.enable_load_extension(True)
    connection.execute("SELECT load_extension('mod_spatialite')")
    
    result = connection.execute("SELECT pkuid, name, description, asgeojson(geometry) FROM points2")
    print(result)
    points = [row[3] for row in result]
    
    connection.close()
    print(points)    
    
    return render_template('simple-map.html', points=points)

@app.route('/add_point', methods=('GET', 'POST'))
def add_point():
    if request.method == 'POST':
        connection = sqlite3.connect("space-race-hackathon.sqlite")
        connection.enable_load_extension(True)
        connection.execute("SELECT load_extension('mod_spatialite')")
#        connection.execute("SELECT DisableSpatialIndex( 'points2' , 'geometry' )")
    
        cursor = connection.cursor()
        point = request.form['point']
        cursor.execute(f"INSERT INTO points2 (geometry) VALUES (GeomFromGeoJSON('{point}'))")
        connection.commit()

        connection.close()
    return "OK"
