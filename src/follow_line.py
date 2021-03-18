#!/usr/bin/env python3

import setup
from gpiozero import LineSensor
from signal import pause
from time import sleep

CURVE_FRACTION = 0.85
SLEEP_DURATION_SECONDS = 0.3
FORWARD_SPEED = 0.4 # below 0.5 and there is too much friction to move
LEFT_IS_ON_LINE = False
RIGHT_IS_ON_LINE = False

robby = None

def left_line_detected_response():
    print('left: detected line')
    global LEFT_IS_ON_LINE
    LEFT_IS_ON_LINE = True
    if LEFT_IS_ON_LINE and RIGHT_IS_ON_LINE:
        # robby.forward(0.3)
        # print('stopped')
        return
    robby.forward(curve_left=CURVE_FRACTION)
    # sleep(SLEEP_DURATION_SECONDS)
    robby.forward(FORWARD_SPEED)
    return

def right_line_detected_response():
    print('right: detected line')
    global RIGHT_IS_ON_LINE
    RIGHT_IS_ON_LINE = True
    if LEFT_IS_ON_LINE and RIGHT_IS_ON_LINE:
        # robby.forward(0.3)
        # print('stopped')
        return
    robby.forward(curve_right=CURVE_FRACTION)
    #sleep(SLEEP_DURATION_SECONDS)
    robby.forward(FORWARD_SPEED)
    return

def when_no_line_left_do_this():
    print("left: no line")
    global LEFT_IS_ON_LINE
    LEFT_IS_ON_LINE = False
    robby.forward(FORWARD_SPEED)
    return

def when_no_line_right_do_this():
    print("right: no line")
    global RIGHT_IS_ON_LINE
    RIGHT_IS_ON_LINE = False
    robby.forward(FORWARD_SPEED)
    return

if __name__ == "__main__":
    '''
    Run robby & follow the line indefinitely
    '''

    # Setup Robby
    robby = setup.get_robby()
    left_sensor = LineSensor(21)
    right_sensor = LineSensor(14)

    # line detected behavior
    right_sensor.when_line = when_no_line_right_do_this
    left_sensor.when_line = when_no_line_left_do_this

    # no line detected behavior
    right_sensor.when_no_line = right_line_detected_response
    left_sensor.when_no_line = left_line_detected_response

    # start by going forward
    robby.forward(FORWARD_SPEED)
    # pause()
    sleep(200)

    print("done")