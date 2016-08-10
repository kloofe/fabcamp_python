# FABCamp 3.0 (2016) @ UCI Samueli School of Engineering
# Servo Motor Control by Farzad Ahmadkhanlou, Ph.D., P.E. (8/6/2016)

# External module imports
import RPi.GPIO as GPIO
import time

# Pin Definitons:
pwmPin = ??? # Broadcom pin ???
ledPin = ??? # Broadcom pin ???
CWPin=???    # pin to command counter clockwise rotation
CCWPin=???   # pin to command clockwise rotation

dc = 10 # duty cycle (0-22.5) for PWM pin
angle=90
offset=10

# Pin Setup:
GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
GPIO.setup(ledPin, GPIO.OUT) # LED pin set as output
GPIO.setup(pwmPin, GPIO.OUT) # PWM pin set as output
pwm = GPIO.PWM(pwmPin, 100)  # Initialize PWM on pwmPin 100Hz frequency

GPIO.setup(CWPin, GPIO.OUT) # Button pin set as input
GPIO.setup(CCWPin, GPIO.OUT) # Button pin set as input

# Initial state for LEDs:
GPIO.output(ledPin, GPIO.LOW)
pwm.start(dc)


print("Here we go! Press CTRL+C to exit")
try:
    while 1:
        if GPIO.input(CWPin): # button is released
            angle=min(angle+5,180-offset)
            duty = float(angle) / 10.0 + 2.5
            pwm.ChangeDutyCycle(duty)            
            GPIO.output(ledPin, GPIO.???) # How do you turn the LED on (Hint: Look later in the elif)
            time.sleep(0.075)
            GPIO.output(ledPin, GPIO.???) # How do you turn the LED off (Hint: Look later in the elif)
            time.sleep(0.075)
            if angle==180-offset:
                GPIO.output(CWPin, GPIO.LOW)
        elif GPIO.input(CCWPin): # button is released
            angle=max(angle-5,offset)
            duty = float(angle) / 10.0 + 2.5
            pwm.ChangeDutyCycle(duty)            
            GPIO.output(ledPin, GPIO.HIGH)
            time.sleep(0.075)
            GPIO.output(ledPin, GPIO.LOW)
            time.sleep(0.075)
            if angle==offset:
                GPIO.output(CCWPin, GPIO.LOW)
        else: # button is pressed:
            GPIO.output(ledPin, GPIO.LOW)

except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
    pwm.stop() # stop PWM
    GPIO.cleanup() # cleanup all GPIO
