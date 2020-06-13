# Write your code here :-)
from gpiozero import Robot
import time

robby = Robot(left=(8, 7), right=(9, 10))

robby.forward(.5)  # async
# robby.backward()
time.sleep(1)
robby.right(.5)
# robby.left(1)
time.sleep(1)
robby.stop() # async
