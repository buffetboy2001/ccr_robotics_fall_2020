# Follow the Black Line

**Module Goal**: write Python code to use the line sensors and follow the line!

*Acknowledgement*: the python snippet in this module is copied directly from the [official Raspberry Pi tutorial](https://projects.raspberrypi.org/en/projects/rpi-python-line-following). 

## Python Code

Open a new file: **follow_line.py** (Mr. Bowman may have created an empty file for you)

```python
#!/bin/python3
from gpiozero import Robot, LineSensor
from signal import pause
from time import sleep

robot = Robot(left=(7, 8), right=(9, 10))
left_sensor = LineSensor(17)
right_sensor = LineSensor(27)

left_sensor.when_line = robot.left
left_sensor.when_no_line = robot.forward

right_sensor.when_line = robot.right
right_sensor.when_no_line = robot.forward

pause()
```

Start `Robby` over top of the black line such that both line sensors show a blue light. Run the code!

This is a basic line-following algorithm. It won't be pretty! But, it should work.

**Challenge**: Discuss your ideas for making a better algorithm.

---

**Module Complete**