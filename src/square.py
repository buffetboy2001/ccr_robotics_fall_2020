#!/bin/python3
#
# Write your code here :-)
from gpiozero import Robot
import time

robby = Robot(left=(8, 7), right=(9, 10))

SLEEP_TIME_SECONDS = 1 

def do_short_leg():
    '''
    Move forward for X seconds, then turn right 90 degrees.
    '''

    robby.forward() # starts forward motion and returns
    time.sleep(SLEEP_TIME_SECONDS)
    robby.stop()
    robby.right(.4)
    time.sleep(SLEEP_TIME_SECONDS)
    robby.stop()

    return

#-------
do_short_leg()

 
