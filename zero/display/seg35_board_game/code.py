from letters import display_pattern, display_patternSleep, display_sequence, get_all_characters, get_random_letter, get_all_character_objects
from dots import clear_all_pins, move_dot_right, move_dot_left, move_dot_down, move_dot_up
from board_mode import BOARD_MODE, get_current_mode, check_mode_button, get_current_mode_name
from joystick import check_up_button, check_down_button, check_left_button, check_right_button
from pins_init import bmi
from letters import LETTERS
import time

currentMode = get_current_mode()
text_displaying = False

LETTER_LIST = get_all_character_objects()
index = 0

# random_letter = get_random_letter()
random_letter = get_random_letter()
current_letter = LETTER_LIST[0]

def check_mode_callback():
    global text_displaying
    text_displaying = False

def show_data_callback():
    global text_displaying
    text_displaying = False

def stop_showing_callback():
    global text_displaying
    text_displaying = True

def next_letter_callback():
    global random_letter
    global index
    global current_letter
    if (currentMode == BOARD_MODE.RANDOM_LETTER):
        random_letter = get_random_letter()
    if (currentMode == BOARD_MODE.TEST_LETTERS):
        index = (index + 1) % len(LETTER_LIST)
        print(index)
        current_letter = LETTER_LIST[index]


def show_temperature():
    global text_displaying
    calibration = 0.5
    text_displaying = True
    temperature = bmi.temperature - calibration
    temperature_string = f"{temperature:.1f}*"
    display_sequence(temperature_string , 0.05)

def show_text(text):
    global text_displaying
    text_displaying = True
    display_sequence(text , 0.05)

def show_random():
    display_patternSleep(random_letter, 0.0008)

def show_letter():
    display_patternSleep(current_letter, 0.0008)


while True:
    check_mode_button(check_mode_callback)
    currentMode = get_current_mode()
    if (currentMode == BOARD_MODE.GYRO_BALL):
        text_displaying = False
        accx, accy, accz = bmi.acceleration
        # If not in balance, move the dot based on the accelerometer readings
        if abs(accx) > abs(accy):
            if accx > 0:
                move_dot_right()
            else:
                move_dot_left()
        else:
            if accy > 0:
                move_dot_up()
            else:
                move_dot_down()

        time.sleep(0.15)
    elif (currentMode == BOARD_MODE.MOVE_DOT):
        check_up_button(move_dot_up)
        check_down_button(move_dot_down)
        check_left_button(move_dot_left)
        check_right_button(move_dot_right)
    elif (currentMode == BOARD_MODE.TEMPERATURE):
        check_down_button(show_data_callback)
        if (text_displaying == False):
            show_temperature()
    elif (currentMode == BOARD_MODE.SHOW_TEXT):
        check_down_button(show_data_callback)
        if (text_displaying == False):
            display_patternSleep(LETTERS["#"], 0.0002)
    elif (currentMode == BOARD_MODE.RANDOM_LETTER):
        check_up_button(next_letter_callback)
        if (text_displaying == False):
            show_random()
    elif (currentMode == BOARD_MODE.TEST_LETTERS):
        check_up_button(next_letter_callback)
        if (text_displaying == False):
            show_letter()