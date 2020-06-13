# Write your code here :-)
from gpiozero import Robot
import time


robby = Robot(left=(8, 7), right=(9, 10))
robby.forward()  # async
time.sleep(5)
robby.stop() # async
