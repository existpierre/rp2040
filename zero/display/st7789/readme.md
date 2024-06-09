# ST7789v2 display

## Connection

| DISPLAY | RP2040 |
|--|--|
| VCC | 3V3 |
| GND | 3V3 |
| DIN (MOSI) | GP3 (SCL) |
| CLK=SCK  | GP2 (SDA) |
| CS | GP1 (RX) |
| DC | GP0 (TX) |
| RST | GP4 (not used) |
| BL (Backlight) | Maybe can be analog, i use OUT |

[ALIEXPRES description](https://www.aliexpress.com/item/1005005752009686.html?spm=a2g0o.order_detail.order_detail_item.3.4b1df19cDwnQFs)

[WIKI](http://www.waveshare.com/wiki/1.69inch_LCD_Module?spm=a2g0o.detail.1000023.1.2ae2UE90UE90Mr&file=1.69inch_LCD_Module)

For slideshow create in root folder with name images and add bmp file. Warning - max 2MB memory

## Library requirements

By usage in code

- adafruit_st7789.mpy
- adafruit_slideshow.mpy
- adafruit_display_text folder
- adafruit_display_shapes folder
- adafruit_display_notification folder

