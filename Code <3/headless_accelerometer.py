import time

import Adafruit_GPIO.SPI as SPI

import Adafruit_SSD1306
import Adafruit_LSM303

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

lsm303 = Adafruit_LSM303.LSM303()
x = 0
RST = 24

disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, i2c_address=0x3d)
disp.begin()
disp.clear()
disp.display()
width = disp.width
height = disp.height

padding = 3 
top = padding
bottom = height-padding

image = Image.new('1', (width, height))
font = ImageFont.load_default
draw = ImageDraw.Draw(image)

xv = 0
yv = 0
shape = 3

while True:
	draw.rectangle((0,0,width,height), outline=0, fill=0)

	accel, mag = lsm303.read()
	accel_x, accel_y, accel_z = accel

	xv = (accel_x/33) + 32
	yv = (accel_y/33) + 64

	draw.text((1,30), "x: " + (str(round(accel_x/107,3))), fill=255)
	draw.text((64, 50), "x: " + (str(round(accel_x/107,3))), fill=255)
	draw.ellipse((xv/2+(48-shape),yv/2+(5-shape),xv/2+(48+shape),yv/2+(5+shape)), outline = 255, fill = 0)

	
	disp.image(image)
	disp.display()
