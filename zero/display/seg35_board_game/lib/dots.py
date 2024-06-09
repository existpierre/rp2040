from pins_init import cathode_pins, anode_pins

current_led = [0, 0]  # LED matrix start position

def clear_all_pins():
    for cathode in cathode_pins:
        cathode.value = True
    for anode in anode_pins:
        anode.value = False

def move_dot_right():
    global current_led
    clear_all_pins()
    # Constrain within matrix columns
    if current_led[1] < len(anode_pins) - 1:
        current_led[1] += 1
    anode_pins[current_led[1]].value = True
    cathode_pins[current_led[0]].value = False

def move_dot_left():
    global current_led
    clear_all_pins()
    # Constrain within matrix columns
    if current_led[1] > 0:
        current_led[1] -= 1
    anode_pins[current_led[1]].value = True
    cathode_pins[current_led[0]].value = False

def move_dot_up():
    global current_led
    clear_all_pins()
    # Constrain within matrix rows
    if current_led[0] > 0:
        current_led[0] -= 1
    anode_pins[current_led[1]].value = True
    cathode_pins[current_led[0]].value = False

def move_dot_down():
    global current_led
    clear_all_pins()
    # Constrain within matrix rows
    if current_led[0] < len(cathode_pins) - 1:
        current_led[0] += 1
    anode_pins[current_led[1]].value = True
    cathode_pins[current_led[0]].value = False

def show_center_dot():
    global current_led
    clear_all_pins()
    # Set the current LED to the center
    current_led = [3, 2]  # Adjust this if your matrix center is different
    anode_pins[current_led[1]].value = True
    cathode_pins[current_led[0]].value = False
