#!/usr/bin/env python3
'''
This python code follows after line_following_simple. That one used
no functions. This one introduces simple functions that students need
to fill in. They should already know about the basic control options.
'''
import setup
from gpiozero import LineSensor
from signal import pause
from time import sleep

robby = None

def left_sensor_detected_white():
    print('left on white...do something about it')
    # Add code here
    return

def right_sensor_detected_white():
    print('right on white...do something about it')
    # Add code here
    return

def left_sensor_detected_black():
    print("left on black...")
    # Add code here
    return

def right_sensor_detected_black():
    print("right on black...")
    # Add code here
    return

if __name__ == "__main__":
    '''
    Run robby & follow the line
    '''

    # Setup Robby
    robby = setup.get_robby()
    left_sensor = LineSensor(21)
    right_sensor = LineSensor(14)

    # left sensor
    left_sensor.when_no_line = left_sensor_detected_black
    left_sensor.when_line = left_sensor_detected_white

    # right sensor
    right_sensor.when_no_line = right_sensor_detected_black
    right_sensor.when_line = right_sensor_detected_white

    # start by going forward
    robby.forward(0.5)

    # sleep(10)
    pause()

    print("done")