import flask
from flask.json import jsonify
import uuid
from roundabout import Roundabout
import socket

games = {}

app = flask.Flask(__name__)


def obtener_direccion_ipv4():
    try:
        # Obtener el nombre del host local
        hostname = socket.gethostname()

        # Obtener la dirección IPv4 asociada con el nombre del host
        direccion_ipv4 = socket.gethostbyname(hostname)

        return direccion_ipv4
    except Exception as e:
        print("Error al obtener la dirección IPv4:", str(e))
        return None


@app.route("/games", methods=["POST"])
def create():
    global games
    id = str(uuid.uuid4())
    games[id] = Roundabout()
    lista = []
    for agent in games[id].schedule.agents:
        if agent.type == "Car":
            lista.append({"id": agent.unique_id, "x": int(agent.pos[0]), "z": int(
                agent.pos[1]), "type": agent.type, "condition": agent.condition, "direction": agent.direction})
        else:
            lista.append({"id": agent.unique_id, "x": int(agent.pos[0]), "z": int(
                agent.pos[1]), "type": agent.type, "condition": agent.condition})

    return jsonify(lista), 201, {'Location': f"/games/{id}"}


@app.route("/games/<id>", methods=["GET"])
def queryState(id):
    if id not in games:
        # Handle the case where the provided ID doesn't exist
        return "Game not found", 404

    model = games[id]
    model.step()
    lista = []

    # Ensure the game has agents
    if hasattr(model.schedule, "agents"):
        for agent in model.schedule.agents:
            if agent.type == "Car":
                lista.append({
                    "id": agent.unique_id,
                    "x": int(agent.pos[0]),
                    "z": int(agent.pos[1]),
                    "type": agent.type,
                    "condition": agent.condition,
                    "direction": agent.direction
                })
            else:
                lista.append({
                    "id": agent.unique_id,
                    "x": int(agent.pos[0]),
                    "z": int(agent.pos[1]),
                    "type": agent.type,
                    "condition": agent.condition
                })

    if lista:
        # If the list is not empty, return it as JSON
        return jsonify(lista)
    else:
        # Handle the case where there's no JSON data to return
        return "No game data available", 404


app.run(host=f"{obtener_direccion_ipv4()}")
