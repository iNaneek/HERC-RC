from inputs import devices
from inputs import get_gamepad
import controller_inputs


import RPi.GPIO as GPIO
import time


import atexit
atexit.register(GPIO.cleanup)

inputs_list = {"ABS_Y" : 0, "ABS_RY" : 0, "ABS_Z" : 0, "ABS_RZ" : 0, "BTN_START" : 0}

GPIO.setwarnings(False)
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)


# Set the GPIO pins as an output pin

#laser range finder
GPIO.setup(18, GPIO.OUT)


GPIO.setup(16, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)


GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)


GPIO.setup(21, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)

#PWM setup
pwmfl = GPIO.PWM(21, 2000)
pwmfl.start(0)
pwmfr = GPIO.PWM(25, 2000)
pwmfr.start(0)





#main look
while True:
    #print("test")
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
       
        GPIO.cleanup(23)
        GPIO.setup(24, GPIO.OUT)
       
    if inputs["ABS_Y"] > 0:
       
        GPIO.cleanup(24)
        GPIO.setup(23, GPIO.OUT)
