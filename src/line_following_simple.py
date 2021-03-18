#!/usr/bin/env python3
from gpiozero import Robot, LineSensor
from signal import pause
from time import sleep

robby = Robot(left=(8, 7), right=(9, 10))
left_sensor = LineSensor(21)
right_sensor = LineSensor(14)

left_sensor.when_line = robby.forward
left_sensor.when_no_line = robby.left

right_sensor.when_line = robby.forward
right_sensor.when_no_line = robby.right

robby.forward(0.5)
sleep(30)
robby.stop()
