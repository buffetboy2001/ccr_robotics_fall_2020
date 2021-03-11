#!/usr/bin/env python3
from gpiozero import Robot, LineSensor
from signal import pause
from time import sleep

robby = Robot(left=(7, 8), right=(9, 10))
left_sensor = LineSensor(17)
right_sensor = LineSensor(27)

left_sensor.when_line = robby.left
left_sensor.when_no_line = robby.forward

right_sensor.when_line = robby.right
right_sensor.when_no_line = robby.forward

robby.forward()
sleep(10)