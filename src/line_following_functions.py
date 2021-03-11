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

def left_line_detected_response():
    print('left: detected line...do something about it')
    # Add code here
    return

def right_line_detected_response():
    print('right: detected line...do something about it')
    # Add code here
    return

def when_no_line_left_do_this():
    print("left: no line")
    # Add code here
    return

def when_no_line_right_do_this():
    print("right: no line")
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

    # line detected behavior
    left_sensor.when_no_line = when_no_line_left_do_this
    right_sensor.when_no_line = when_no_line_right_do_this

    # no line detected behavior
    left_sensor.when_line = left_line_detected_response
    right_sensor.when_line = right_line_detected_response

    # start by going forward
    robby.forward(0.5)

    sleep(10)
    
    print("done")
