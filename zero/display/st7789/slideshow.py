import board
import busio
import terminalio
import displayio
from adafruit_slideshow import PlayBackOrder, SlideShow

# INIT CONFIG

DISPLAY_WIDTH = 240
DISPLAY_HEIGHT = 300

# Starting in CircuitPython 9.x fourwire will be a seperate internal library
# rather than a component of the displayio library
try:
    from fourwire import FourWire
except ImportError:
    from displayio import FourWire
from adafruit_display_text import label
from adafruit_st7789 import ST7789

# Release any resources currently in use for the displays
displayio.release_displays()

spi = busio.SPI(board.GP2, MOSI=board.GP3)
tft_cs = board.GP1
tft_dc = board.GP0
tft_backlight = board.GP5

display_bus = FourWire(spi, command=tft_dc, chip_select=tft_cs)

display = ST7789(
    display_bus,
    width=DISPLAY_WIDTH,
    height=DISPLAY_HEIGHT,
    rowstart=0,
    backlight_pin=tft_backlight,
    rotation=180,
)


slideshow = SlideShow(display,
                      folder="/images",
                      loop=False,
                      order=PlayBackOrder.ALPHABETICAL,
                      dwell=300)

while slideshow.update():
    pass
