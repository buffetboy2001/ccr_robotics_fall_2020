# Write your code here :-)
from gpiozero import Robot
import time

robby = Robot(right=(7,8), left=(9,10))

robby.forward(curve_right=.5)  # async
time.sleep(20)
robby.stop() # async
