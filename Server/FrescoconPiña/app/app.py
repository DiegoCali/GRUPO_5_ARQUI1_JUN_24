import testFunctions
from flask_cors import CORS
from flask import Flask, request, jsonify


app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
    return "Hello, World!"


@app.route('/light', methods=['POST'])
def set_lights_states():
    data = request.get_json()
    testFunctions.lights_actions(data['num'], data['state'])
    return jsonify(data)


@app.route('/lights', methods=['POST'])
def set_all_lights_states():
    data = request.get_json()
    testFunctions.all_lights_action(data['state'])
    return jsonify(data)


@app.route('/transport_band', methods=['POST'])
def set_transport_band():
    data = request.get_json()
    testFunctions.transport_band_action(data['state'])
    return jsonify(data)


@app.route('/Garage', methods=['POST'])
def set_garage():
    data = request.get_json()
    testFunctions.garage_action(data['state'])
    return jsonify(data)


@app.route('/actual_people', methods=['GET'])
def get_actual_people():
    return jsonify({'actual_people': testFunctions.actual_people})


@app.route('/counter_people', methods=['GET'])
def get_counter_people():
    return jsonify({'counter_people': testFunctions.counter_people})


@app.route('/alarm', methods=['POST'])
def set_alarm():
    data = request.get_json()
    testFunctions.alarm_action(data['state'])
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
