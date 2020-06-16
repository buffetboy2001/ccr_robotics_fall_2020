#!/bin/python3
#
# Write your code here :-)
from gpiozero import Robot
import time

robby = Robot(left=(8, 7), right=(9, 10))

SLEEP_TIME_SECONDS = 0.5
TURN_SPEED = 1


def do_short_leg():
    '''
    Move forward for X seconds, then turn right 90 degrees.
    '''

    robby.forward() # starts forward motion and returns
    time.sleep(3*SLEEP_TIME_SECONDS)
    robby.stop()
    robby.right(TURN_SPEED)
    time.sleep(SLEEP_TIME_SECONDS)
    robby.stop()

    return

#-------
for i in range(1,5):
    do_short_leg()

 
