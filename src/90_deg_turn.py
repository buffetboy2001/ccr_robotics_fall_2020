# Write your code here :-)
from gpiozero import Robot
import time

robby = Robot(left=(8, 7), right=(9, 10))

sleep_time_sec = 0.7
turn_speed = 0.5 

robby.left(turn_speed)  # async
time.sleep(sleep_time_sec)
robby.stop() 
