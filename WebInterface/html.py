import flask
import uuid

liste=["vds","32","43"]
nom = liste[0]
x = liste[1]
y = liste[2]
# Web site initialisation
app = flask.Flask(__name__)
app.secret_key = uuid.uuid4().hex  # Unique ID of the web site (for sessions)

@app.route('/position')
def position():
  return flask.render_template("position.html", x=x, y=y)


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=80)
