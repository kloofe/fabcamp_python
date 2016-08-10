# FABCamp 3.0 (2016) @ UCI Samueli School of Engineering
# Servo Motor Control by Farzad Ahmadkhanlou, Ph.D., P.E. (8/6/2016)

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)          # Broadcom pin-numbering scheme
GPIO.setup(???, GPIO.OUT)        # What is the gpio pin number we are using?
servo = GPIO.PWM(???, 100)       # Initialize servo on pwmPin 100Hz frequency. What is the gpio pin number we are using?
servo.start(5)

# What range do we want if we want the the handle to rotate 180 degrees? Remember it's good to have some offset
for angle in range(???,???): 
    duty = float(angle) / 10.0 + 2.5
    servo.ChangeDutyCycle(duty)
    time.sleep(0.01)	
	
	
servo.stop()        # stop servo
GPIO.cleanup()      # cleanup all GPIO

