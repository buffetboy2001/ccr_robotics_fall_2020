# Write your code here :-)
from gpiozero import Robot
import time

robby = Robot(right=(7,8), left=(9,10))

# robby.forward()  # async
# robby.backward()
robby.right(1)
# robby.left(1)
time.sleep(1.1)
robby.stop() # async
