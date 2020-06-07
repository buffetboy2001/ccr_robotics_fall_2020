# Write your code here :-)
from gpiozero import Robot
import time

robby = Robot(left=(7,8), right=(9,10))

robby.forward()  # async
time.sleep(2)
robby.stop() # async
