# Write your code here :-)
from gpiozero import Robot
import time

robby = Robot(left=(7,8), right=(9,10))

# robby.forward()  # async
robby.backward()
# robby.right(1)
# robby.left(1)
time.sleep(10)
robby.stop() # async