from inputs import devices
from inputs import get_gamepad

import controller_inputs
import laser_tracking

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

#Laser
GPIO.setup(18, GPIO.OUT)

#FR
GPIO.setup(16, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)

#FL
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)

#PWM
GPIO.setup(21, GPIO.OUT) #PWM - Orange bottom right
GPIO.setup(25, GPIO.OUT) #PWM - Brown
pwmfr = GPIO.PWM(21, 2000)
pwmfr.start(0)
pwmfl = GPIO.PWM(25, 2000)
pwmfl.start(0)



#'''
#RL top left
GPIO.setup(9, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
#RR - Bottom left
GPIO.setup(19, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)

GPIO.setup(10, GPIO.OUT) #PWM RL
pwmrl = GPIO.PWM(10, 2000) #both direction at 100% duty
pwmrl.start(0)

GPIO.setup(13, GPIO.OUT) #PMW RR
pwmrr = GPIO.PWM(13, 2000) #PWM only goes in reverse 
pwmrr.start(0)

'''
GPIO.cleanup(10)
GPIO.cleanup(9)
GPIO.cleanup(11)
GPIO.cleanup(13)
GPIO.cleanup(19)
GPIO.cleanup(26)
#'''

laserCoolDown = 0

while True:
    
    laserCoolDown -= 1
    #print(laserCoolDown)

    #print("l")
    inputs = controller_inputs.return_controller_inputs()
    # print(inputs)
    

    #print(round(abs(inputs["ABS_Y"])/330),round(abs(inputs["ABS_RY"])/330))
    #print(round(abs(inputs["ABS_RY"])/330))
    #print(round(abs(inputs["ABS_Y"])/330))
    pwmfr.ChangeDutyCycle(round(abs(inputs["ABS_RY"])/330))
    pwmrr.ChangeDutyCycle(round(abs(inputs["ABS_RY"])/330))
    pwmfl.ChangeDutyCycle(round(abs(inputs["ABS_Y"])/330))
    pwmrl.ChangeDutyCycle(round(abs(inputs["ABS_Y"])/330))
    
    #end PWM

    
    # Wheel direction control 
    if inputs["ABS_RY"] < 0: #FR and RR
        
        
        GPIO.cleanup(20)         # Front - stops 20 (low)
        GPIO.setup(16, GPIO.OUT) # initializes 16

        
        GPIO.cleanup(26)         #same thing for rear side - Doesnt work properly
        GPIO.setup(19, GPIO.OUT)
        
    if inputs["ABS_RY"] > 0:
        
        GPIO.cleanup(16)
        GPIO.setup(20, GPIO.OUT)

        
        GPIO.cleanup(19)         #doesnt work properly
        GPIO.setup(26, GPIO.OUT)

    if inputs["ABS_Y"] < 0:      #RL and FL
        
        GPIO.cleanup(24)
        GPIO.setup(23, GPIO.OUT)

        GPIO.cleanup(11)
        GPIO.setup(9, GPIO.OUT)
        
    if inputs["ABS_Y"] > 0:
        
        GPIO.cleanup(23)
        GPIO.setup(24, GPIO.OUT)

        GPIO.cleanup(9)
        GPIO.setup(11, GPIO.OUT)
    
    


    if inputs["BTN_START"] == 1:
        GPIO.output(18, GPIO.HIGH)

    else:
        GPIO.output(18, GPIO.LOW)

    if (inputs['BTN_WEST'] == 1) and (laserCoolDown < 0):
        print(laser_tracking.process_laser_image())
        laserCoolDown = 100

        
        
    
    
    




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
