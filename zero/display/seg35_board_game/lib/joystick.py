from pins_init import BTN_UP, BTN_DOWN, BTN_LEFT, BTN_RIGHT#, BTN_MIDDLE
import time

# initial button states
prev_state_up = BTN_UP.value
prev_state_down = BTN_DOWN.value
prev_state_left = BTN_LEFT.value
prev_state_right = BTN_RIGHT.value
# prev_state_middle = BTN_MIDDLE.value


# Button checking functions
def check_up_button(callback):
    global prev_state_up
    cur_state = BTN_UP.value
    if cur_state != prev_state_up:
        prev_state_up = cur_state
        if cur_state:
            callback()
#             while BTN_UP.value:
#                 time.sleep(0.1)
#     else:
#         time.sleep(0.1)


def check_down_button(callback):
    global prev_state_down
    cur_state = BTN_DOWN.value
    if cur_state != prev_state_down:
        prev_state_down = cur_state
        if cur_state:
            callback()
#             while BTN_DOWN.value:
#                 time.sleep(0.1)
#     else:
#         time.sleep(0.1)


def check_left_button(callback):
    global prev_state_left
    cur_state = BTN_LEFT.value
    if cur_state != prev_state_left:
        prev_state_left = cur_state
        if cur_state:
            callback()
#             while BTN_LEFT.value:
#                 time.sleep(0.1)
#     else:
#         time.sleep(0.1)


def check_right_button(callback):
    global prev_state_right
    cur_state = BTN_RIGHT.value
    if cur_state != prev_state_right:
        prev_state_right = cur_state
        if cur_state:
            callback()
#             while BTN_RIGHT.value:
#                 time.sleep(0.1)
#     else:
#         time.sleep(0.1)


# def check_middle_button(callback):
#     global prev_state_middle
#     cur_state = BTN_MIDDLE.value
#     if cur_state != prev_state_middle:
#         prev_state_middle = cur_state
#         if cur_state:
#             callback()
#             while BTN_MIDDLE.value:
#                 time.sleep(0.1)
#     else:
#         time.sleep(0.1)
