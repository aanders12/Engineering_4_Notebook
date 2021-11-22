# Blink Led RaspberryPi (ENGR4)
# Written by Amarie Anderson
# 9.22.2021


import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM) # sets pin numbering to BCM numbering
GPIO.setup(21,GPIO.OUT) #sets pin 21 as output for led
GPIO.setup(26,GPIO.OUT) #sets pin 26 as output for led
GPIO.setwarnings(False)

while True:
	GPIO.output(21,GPIO.HIGH) #turns light on 
	print("blue is bright, green is dim")
	time.sleep(1) #second long break
	GPIO.output(21,GPIO.LOW) #turns light off
	GPIO.output(26,GPIO.HIGH)
	print("blue is dim, green is bright")
	time.sleep(1)
	GPIO.output(26,GPIO.LOW)



