# Write your code here :-)
from gpiozero import Robot
import time

robby = Robot(right=(7,8), left=(9,10))

robby.forward()  # async
time.sleep(9)
robby.stop() # async
