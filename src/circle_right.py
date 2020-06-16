# Write your code here :-)
from gpiozero import Robot
import time

robby = Robot(left=(8, 7), right=(9, 10))

robby.forward(curve_right=.75)  # async
time.sleep(20)
robby.stop() # async
