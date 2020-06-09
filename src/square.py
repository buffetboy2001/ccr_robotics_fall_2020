#!/bin/python3
#
# Write your code here :-)
from gpiozero import Robot
import time

robby = Robot(left=(7,8), right=(9,10))

def do_short_leg():
    '''
    Move forward for X seconds, then turn right 90 degrees.
    '''

    robby.forward() # starts forward motion and returns
    time.sleep(9)
    robby.stop()
    robby.right(.8)
    time.sleep(1.5)
    robby.stop()

    return

#-------
do_short_leg()

 
