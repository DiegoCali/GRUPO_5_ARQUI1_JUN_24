import requests
from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
class MainData:
    def __init__(self, totalClientIn, totalClientOut, clientsIn, clientsOut, conditionConveyorBelt, gate, alarm):
        self.totalClientsIn = totalClientIn
        self.totalClientsOut = totalClientOut
        self.clientsIn = clientsIn
        self.clientsOut = clientsOut
        self.conditionConveyorBelt = conditionConveyorBelt
        self.gate = gate
        self.alarm = alarm


class Light:
    def __init__(self, id, state):
        self.id = id
        self.state = state

#crear una lista de luces
lights = []

for i in range(10):
	lights.append(Light(i, False))

data = MainData(0, 0, 0, 0, False, False, False)

def test(request):
    global lights
    global data
    loadData()
    return render(request, 'test.html', { 'lights': lights, 'data': data})

def loadData():
    print("Loading data")
    global data
    
    #Load actual people
    response = requests.get('http://127.0.0.1:5000/actual_people')
    print(response.json())
    data.totalClientsIn = response.json()['actual_people']

    #counter people
    response = requests.get('http://127.0.0.1:5000/counter_people')
    print(response.json())
    data.clientsIn = response.json()['counter_people']

    #trasnport band
    response = requests.get('http://127.0.0.1:5000/transport_band_status')
    print(response.json())
    state = response.json()['state']
    if state == 1:
        data.conditionConveyorBelt = True
    else:
        data.conditionConveyorBelt = False

   
    #gate
    response = requests.get('http://127.0.0.1:5000/garage_status')
    print(response.json())
    state = response.json()['state']
    if state == 1:
        data.gate = True
    else:
        data.gate = False

    #alarm
    response = requests.get('http://127.0.0.1:5000/alarm_status')
    print(response.json())
    state = response.json()['state']
    if state == 1:
        data.gate = True
    else:
        data.gate = False

                            
    


def set_all_lights_states(request):
    global data
    global lights
    if request.method == 'POST':
        id_light = request.POST.get('id')
        action = request.POST.get('action')
        id_light = int(id_light)
        print(f"ID: {id_light}, Action: {action}")
        print("Request received")

        if action == 'on':
            lights[id_light].state = True
            dataResponse = {'state': 1}
        elif action == 'off':
            lights[id_light].state = False
            dataResponse = {'state': 0}
        
        response = requests.post('http://127.0.0.1:5000/lights', json=dataResponse)
        if response.status_code == 200:
            
            return render(request, 'test.html', { 'lights': lights, 'data': data})
        else:
            return JsonResponse({'message': 'Failed to set lights state'}, status=500)
    else:
        return JsonResponse({'message': 'Invalid request method'}, status=400)


    
def set_lights_states(request):
    global data
    global lights
    if request.method == 'POST':
        print("Request received")
        id_light = request.POST.get('id')
        action = request.POST.get('action')
        id_light = int(id_light)

        print(f"ID: {id_light}, Action: {action}")
        if action == 'on':
            lights[id_light].state = True
            dataResponse = {'num': id_light, 'state': 1}
        elif action == 'off':
            lights[id_light].state = False
            dataResponse = {'num': id_light, 'state': 0}

        response = requests.post('http://127.0.0.1:5000/light', json=dataResponse)
        if response.status_code == 200:
            
            return render(request, 'test.html', { 'lights': lights, 'data': data})
        else:
            return JsonResponse({'message': 'Failed to set lights state'}, status=500)
        
    else:
        return JsonResponse({'message': 'Invalid request method'}, status=400)
    
def set_transport_band(request):
    global data
    if request.method == 'POST':
        print("Request received")
        action = request.POST.get('action')
        if action == 'on':
            data.conditionConveyorBelt = True
            dataResponse = {'state': 1}
        elif action == 'off':
            data.conditionConveyorBelt = False
            dataResponse = {'state': 0}

        response = requests.post('http://127.0.0.1:5000/transport_band', json=dataResponse)
        if response.status_code == 200:
            return render(request, 'test.html', { 'lights': lights, 'data': data})
        else:
            return JsonResponse({'message': 'Failed to set transport band state'}, status=500)
        
    else:
        return JsonResponse({'message': 'Invalid request method'}, status=400)

def set_garage(request):
    global data
    if request.method == 'POST':
        print("Request received")
        action = request.POST.get('action')
        if action == 'on':
            data.gate = True
            dataResponse = {'state': 1}
        elif action == 'off':
            data.gate = False
            dataResponse = {'state': 0}

        response = requests.post('http://127.0.0.1:5000/Garage', json=dataResponse)
        if response.status_code == 200:
            return render(request, 'test.html', { 'lights': lights, 'data': data})
        else:
            return JsonResponse({'message': 'Failed to set garage state'}, status=500)
    else:
        return JsonResponse({'message': 'Invalid request method'}, status=400)
