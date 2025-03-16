
from inputs import devices
from inputs import get_gamepad
import controller_inputs

import RPi.GPIO as GPIO
import time

import atexit
atexit.register(GPIO.cleanup)




inputs_list = {"ABS_Y" : 0, "ABS_RY" : 0, "ABS_Z" : 0, "ABS_RZ" : 0, "BTN_START" : 0}

GPIO.cleanup()

# Set up the GPIO mode (BCM or BOARD)
GPIO.setmode(GPIO.BCM)  # Or GPIO.BOARD for physical pin numbering

# Set the GPIO pin as an output pin
GPIO.setwarnings(False)

GPIO.setup(18, GPIO.OUT)

GPIO.setup(16, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)

GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)

GPIO.setup(21, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)
pwmfl = GPIO.PWM(21, 2000)
pwmfl.start(0)
pwmfr = GPIO.PWM(25, 2000)
pwmfr.start(0)



while True:
    

    print("l")
    inputs = controller_inputs.return_controller_inputs()
    print(inputs)
    
    print(round(abs(inputs["ABS_RY"])/330))
    print(round(abs(inputs["ABS_Y"])/330))
    pwmfl.ChangeDutyCycle(round(abs(inputs["ABS_RY"])/330))
    pwmfr.ChangeDutyCycle(round(abs(inputs["ABS_Y"])/330))

    
    if inputs["ABS_RY"] < 0:
        
        
        GPIO.cleanup(20)
        GPIO.setup(16, GPIO.OUT)
        
    if inputs["ABS_RY"] > 0:
        
        GPIO.cleanup(16)
        GPIO.setup(20, GPIO.OUT)

    if inputs["ABS_Y"] < 0:
        
        GPIO.cleanup(24)
        GPIO.setup(23, GPIO.OUT)
        
    if inputs["ABS_Y"] > 0:
        
        GPIO.cleanup(23)
        GPIO.setup(24, GPIO.OUT)

    if inputs["BTN_START"] == 1:
        GPIO.output(18, GPIO.HIGH)

    else:
        GPIO.output(18, GPIO.LOW)
        
    
    
    




# Set up the GPIO mode (BCM or BOARD)
GPIO.setmode(GPIO.BCM)  # Or GPIO.BOARD for physical pin numbering

# Set the GPIO pin as an output pin
GPIO.setup(18, GPIO.OUT)  # Change 18 to your desired GPIO pin

# Turn the GPIO pin ON (High)
GPIO.output(18, GPIO.HIGH)
time.sleep(100)  # Wait for 1 second

# Turn the GPIO pin OFF (Low)
GPIO.output(18, GPIO.LOW)

# Clean up the GPIO settings when done
GPIO.cleanup()
