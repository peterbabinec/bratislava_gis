from flask import Flask, jsonify, render_template, request
from database import DatabasePort
import json
from psycopg2.extras import RealDictCursor, DictCursor
from itertools import chain

app = Flask(__name__, template_folder="./templates", static_folder="./static")
app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/api/v1.0/hello", methods=['GET'])
def hello():
    name = request.args.get('name')
    return get_hello(name)


@app.route("/api/v1.0/fitness", methods=['GET'])
def fitness():
    dist = request.args.get('dist')
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    return get_fitness(dist, lat, lon)


def get_fitness(dist, lat, lon):
    dp = DatabasePort()
    with dp.connection_handler(commit=True, cursor_factory=DictCursor) as cursor:
        query = "SELECT json_build_object(" \
                "'type', 'Feature'," \
                "'geometry', ST_AsGeoJSON(ST_Transform(sub.way, 4326))::json," \
                "'properties', json_build_object(" \
                "   'title', sub.name," \
                "   'description', coalesce(sub.leisure, sub.amenity)," \
                "   'marker-color', '#3bb2d0'," \
                "   'marker-size', 'medium'," \
                "   'marker-symbol', 'building'" \
                "   )" \
                ") FROM (" \
                "SELECT way, name, leisure, amenity FROM planet_osm_point WHERE leisure = 'fitness_centre' OR amenity='gym' " \
                ") AS sub;"
        # query = "SELECT name FROM planet_osm_point WHERE leisure = 'fitness_centre';"
        cursor.execute(query)
        rows = list(chain(*cursor.fetchall()))
        return jsonify(rows)






def get_hello(name):
    hello_message = {
        'hello': 'world',
        'name': name
    }
    return jsonify(hello_message)


if __name__ == "__main__":
    app.run()

