import RPi.GPIO as GPIO
from flask_cors import CORS
from flask import Flask, request, jsonify
from Raspberry.Supervisor import butler

app = Flask(__name__)
CORS(app)
new_butler = butler()
new_butler.start_supervisor()


@app.route('/')
def index():
    return "Hello, World!"


@app.route('/light', methods=['POST'])
def set_lights_states():
    data = request.get_json()
    print(data)
    new_butler.light_action(data['num'], data['state'])
    return jsonify(data)


@app.route('/lights', methods=['POST'])
def set_all_lights_states():
    data = request.get_json()
    print(data)
    new_butler.light_action(-1, data['state'])
    return jsonify(data)


@app.route('/transport_band', methods=['POST'])
def set_transport_band():
    data = request.get_json()
    print(data)
    return jsonify(data)

@app.route('/transport_band_status', methods=['GET'])
def get_transport_band_status():
    return jsonify({'state': 0})


@app.route('/Garage', methods=['POST'])
def set_garage():
    data = request.get_json()
    new_butler.gate_action(data['state'])
    return jsonify(data)

@app.route('/garage_status', methods=['GET'])
def get_garage_status():
    return jsonify({'state': new_butler.gate_state})


@app.route('/actual_people', methods=['GET'])
def get_actual_people():
    return jsonify({'actual_people': new_butler.clients})


@app.route('/counter_people', methods=['GET'])
def get_counter_people():
    return jsonify({'counter_people': new_butler.clients})


@app.route('/alarm', methods=['POST'])
def set_alarm():
    data = request.get_json()
    print(data)
    return jsonify(data)

@app.route('/alarm_status', methods=['GET'])
def get_alarm_status():
    return jsonify({'state': 0})


if __name__ == '__main__':
    app.run(debug=True)
