# Blink Led RaspberryPi (ENGR4)
# Written by Amarie Anderson
# 9.22.2021


import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(21,GPIO.OUT) 
GPIO.setup(26,GPIO.OUT)
GPIO.setwarnings(False)

while True:
	GPIO.output(21,GPIO.HIGH)
	print("blue is bright, green is dim")
	time.sleep(1)
	GPIO.output(21,GPIO.LOW)
	GPIO.output(26,GPIO.HIGH)
	print("blue is dim, green is bright")
	time.sleep(1)
	GPIO.output(26,GPIO.LOW)



