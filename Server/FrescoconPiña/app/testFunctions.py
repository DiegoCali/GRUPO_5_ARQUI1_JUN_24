actual_people = 0
counter_people = 0
lights = [3, 5, 7, 11, 13, 15, 16, 19, 21, 23]
display = [1, 2, 3, 4]
transport_band = [5]


def lights_actions(num, state):
    try:
        print(f"Light {lights[int(num)]} is {state}")
    except IndexError:
        print(f"Light {num} does not exist")


def all_lights_action(state):
    for light in lights:
        print(f"Light {light} is {state}")


def actual_people_action():
    global actual_people
    actual_people += 1
    print(f"Actual people: {actual_people}")


def transport_band_action(state):
    print(f"Transport band is {state}")


def garage_action(state):
    print(f"Garage is {state}")


def alarm_action(state):
    print(f"Alarm is {state}")