import board
import digitalio
import busio
import bmi160 as BMI160

def setup_pin(pin: object) -> object:
    p = digitalio.DigitalInOut(pin)
    p.direction = digitalio.Direction.OUTPUT
    p.value = False
    return p


cathode_pins = [setup_pin(pin) for pin in [board.GP11, board.GP10, board.GP1, board.GP8, board.GP3, board.GP4, board.GP5]]
anode_pins = [setup_pin(pin) for pin in [board.GP0, board.GP2, board.GP9, board.GP6, board.GP7]]

BTN_SET = digitalio.DigitalInOut(board.GP14)
BTN_SET.direction = digitalio.Direction.INPUT
BTN_SET.pull = digitalio.Pull.DOWN

BTN_UP = digitalio.DigitalInOut(board.GP15)
BTN_UP.direction = digitalio.Direction.INPUT
BTN_UP.pull = digitalio.Pull.DOWN

BTN_DOWN = digitalio.DigitalInOut(board.GP28)
BTN_DOWN.direction = digitalio.Direction.INPUT
BTN_DOWN.pull = digitalio.Pull.DOWN

BTN_LEFT = digitalio.DigitalInOut(board.GP27)
BTN_LEFT.direction = digitalio.Direction.INPUT
BTN_LEFT.pull = digitalio.Pull.DOWN

BTN_RIGHT = digitalio.DigitalInOut(board.GP26)
BTN_RIGHT.direction = digitalio.Direction.INPUT
BTN_RIGHT.pull = digitalio.Pull.DOWN

# BTN_MIDDLE = digitalio.DigitalInOut(board.GP15)
# BTN_MIDDLE.direction = digitalio.Direction.INPUT

i2c = busio.I2C(board.GP13, board.GP12)
bmi = BMI160.BMI160(i2c)
