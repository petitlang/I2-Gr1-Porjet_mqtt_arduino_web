import flask
import uuid
import sqlite3

app = flask.Flask(__name__)
app.secret_key = uuid.uuid4().hex

db_path = 'animal_tracking.db'

def get_animal_data():
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute("SELECT name, x, y ,temperature FROM animal_data WHERE name='Panda'")
    data = c.fetchone()
    conn.close()
    if data:
        return {'name': data[0], 'x': data[1], 'y': data[2],'temperature': data[3]}
    return None

@app.route('/')
def position():
    data = get_animal_data()
    if data:
        return flask.render_template("position.html", nom=data['name'], x=data['x'], y=data['y'], temperature=data['temperature'])
    return "No data available"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
