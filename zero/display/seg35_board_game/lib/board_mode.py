import time
from pins_init import BTN_SET

class BOARD_MODE:
    RANDOM_LETTER = 1
    GYRO_BALL = 2
    MOVE_DOT = 3
    TEMPERATURE = 4
    SHOW_TEXT = 5
    TEST_LETTERS = 6


currentMode = BOARD_MODE.RANDOM_LETTER

# Store all mode options in a list
mode_options = [BOARD_MODE.GYRO_BALL, BOARD_MODE.MOVE_DOT, BOARD_MODE.TEMPERATURE, BOARD_MODE.SHOW_TEXT, BOARD_MODE.RANDOM_LETTER, BOARD_MODE.TEST_LETTERS]


def nextMode():
    global currentMode
    # get the index of the current mode in the list, increment it, and then take the modulus to handle overflow
    currentMode = mode_options[(mode_options.index(currentMode) + 1) % len(mode_options)]


def get_current_mode():
    return currentMode


def get_current_mode_name():
    if (currentMode == BOARD_MODE.GYRO_BALL):
        return "Gyro Ball"
    if (currentMode == BOARD_MODE.MOVE_DOT):
        return "Move Ball"
    if (currentMode == BOARD_MODE.TEMPERATURE):
        return "Check Temperature"
    if (currentMode == BOARD_MODE.SHOW_TEXT):
        return "Show Text"
    if (currentMode == BOARD_MODE.RANDOM_LETTER):
        return "Random Letther game"
    if (currentMode == BOARD_MODE.TEST_LETTERS):
        return "Test letters"



prev_state = BTN_SET.value


def check_mode_button(callback):
    global prev_state
    cur_state = BTN_SET.value
    if cur_state != prev_state:
        prev_state = cur_state  # update state
        if cur_state:  # Button released
            nextMode()
            callback()
            print("New mode: " + get_current_mode_name())
            while BTN_SET.value:  # Wait until button is pressed
                time.sleep(0.1)

