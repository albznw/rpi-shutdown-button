# Raspberry Pi shutdown through momentary swtich script
# Author: Albin Winkelmann

import os
import time
import RPi.GPIO as GPIO

button_pin = 3

# Setup button pin
GPIO.setmode(GPIO.BCM)
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Callback function when button is pressed
def shutdown(channel):
    os.system("sudo shutdown -h now")

# Add callback function to button press event
GPIO.add_event_detect(button_pin, GPIO.FALLING, bouncetime=500, callback=shutdown)

# Halt program to make sure it never exits
while True:
    time.sleep(1)
