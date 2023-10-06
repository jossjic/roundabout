import flask
from flask.json import jsonify
import uuid
from roundabout import Roundabout

games = {}

app = flask.Flask(__name__)


@app.route("/games", methods=["POST"])
def create():
    global games
    id = str(uuid.uuid4())
    games[id] = Roundabout()
    lista = []
    for agent in games[id].schedule.agents:
        lista.append({"id": agent.unique_id, "x": int(agent.pos[0]), "z": int(
            agent.pos[1]), "type": agent.type, "condition": agent.condition})

    return jsonify(lista), 201, {'Location': f"/games/{id}"}


@app.route("/games/<id>", methods=["GET"])
def queryState(id):
    global model
    model = games[id]
    model.step()
    lista = []
    for agent in model.schedule.agents:
        lista.append({"id": agent.unique_id, "x": int(agent.pos[0]), "z": int(
            agent.pos[1]), "type": agent.type, "condition": agent.condition})
    return jsonify(lista)


app.run()
