# Write your code here :-)
from gpiozero import Robot
import time
import setup

robby = setup.get_robby()
robby.forward()  # async
time.sleep(2)
robby.stop() # async
