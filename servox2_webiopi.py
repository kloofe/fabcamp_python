# FABCamp 3.0 (2016) @ UCI Samueli School of Engineering
# Servo Motor Control by Farzad Ahmadkhanlou, Ph.D., P.E. (8/6/2016)

# External module imports
import time

import RPi.GPIO as GPIO

# Pin Definitons:
servo1Pin = 12  # Tilt Servo --> Broadcom pin 17 (P1 pin 11)
servo2Pin = 6   # Pan Servo --> Broadcom pin 18 (P1 pin 12)

servo1CWPin = 20    # pin to command counter clockwise rotation
servo1CCWPin = 16   # pin to command clockwise rotation
servo2CWPin = 19    # pin to command counter clockwise rotation
servo2CCWPin = 26   # pin to command clockwise rotation

# Pin Setup:
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)  # Broadcom pin-numbering scheme
GPIO.setup(servo1Pin, GPIO.OUT)
GPIO.setup(servo2Pin, GPIO.OUT)
GPIO.setup(servo1CWPin, GPIO.OUT)
GPIO.setup(servo1CCWPin, GPIO.OUT)
GPIO.setup(servo2CWPin, GPIO.OUT)
GPIO.setup(servo2CCWPin, GPIO.OUT)

# Initial state for LEDs:
ledPin = 21
GPIO.setup(ledPin, GPIO.OUT)  # LED pin set as output
GPIO.output(ledPin, GPIO.LOW)

# Initialize PWM @ 100Hz frequency
servo1 = GPIO.PWM(servo1Pin, 100)
servo2 = GPIO.PWM(servo2Pin, 100)

# Initial state for servos:
angle1 = 90
angle2 = 90
servo1.start(float(angle1) / 10.0 + 2.5)
servo2.start(float(angle2) / 10.0 + 2.5)

offset1 = 40
offset2 = 10

print("Here we go! Press CTRL+C to exit")
try:
    while 1:
        # Servo motor 1
        if GPIO.input(servo1CWPin):  # Clockwise
            angle1 = min(angle1 + 5, 180 - offset1)
            duty1 = float(angle1) / 10.0 + 2.5
            servo1.ChangeDutyCycle(duty1)
            GPIO.output(ledPin, GPIO.HIGH)
            time.sleep(0.075)
            GPIO.output(ledPin, GPIO.LOW)
            time.sleep(0.075)
            if angle1 == 180 - offset1:
                GPIO.output(servo1CWPin, GPIO.LOW)
        elif GPIO.input(servo1CCWPin):  # Counter Clockwise
            angle1 = max(angle1 - 5, offset1)
            duty1 = float(angle1) / 10.0 + 2.5
            servo1.ChangeDutyCycle(duty1)
            GPIO.output(ledPin, GPIO.HIGH)
            time.sleep(0.075)
            GPIO.output(ledPin, GPIO.LOW)
            time.sleep(0.075)
            if angle1 == offset1:
                GPIO.output(servo1CCWPin, GPIO.LOW)

        # Servo motor 2
        if GPIO.input(servo2CWPin):  # Clockwise
            angle2 = min(angle2 + 5, 180 - offset2)
            duty2 = float(angle2) / 10.0 + 2.5
            servo2.ChangeDutyCycle(duty2)
            GPIO.output(ledPin, GPIO.HIGH)
            time.sleep(0.075)
            GPIO.output(ledPin, GPIO.LOW)
            time.sleep(0.075)
            if angle2 == 180 - offset2:
                GPIO.output(servo2CWPin, GPIO.LOW)
        elif GPIO.input(servo2CCWPin):  # Counter Clockwise
            angle2 = max(angle2 - 5, offset2)
            duty2 = float(angle2) / 10.0 + 2.5
            servo2.ChangeDutyCycle(duty2)
            GPIO.output(ledPin, GPIO.HIGH)
            time.sleep(0.075)
            GPIO.output(ledPin, GPIO.LOW)
            time.sleep(0.075)
            if angle2 == offset2:
                GPIO.output(servo2CCWPin, GPIO.LOW)
        else:
            GPIO.output(ledPin, GPIO.LOW)

except KeyboardInterrupt:  # If CTRL+C is pressed, exit cleanly:
    servo1.stop()
    servo2.stop()
    GPIO.cleanup()  # cleanup all GPIO
