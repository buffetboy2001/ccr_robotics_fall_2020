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
    # Add your code here
    robby.forward()
    return

def right_sensor_detected_white():
    print('right on white...do something about it')
    # Add your code here
    robby.forward()
    return

def left_sensor_detected_black():
    print("left on black...")
    # Add your code here
    robby.left()
    return

def right_sensor_detected_black():
    print("right on black...")
    # Add your code here
    robby.right()
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
    robby.forward(0.75)

    sleep(20)
    # pause()

    robby.stop()
    print("done")