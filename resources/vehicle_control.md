# Vehicle Control

**Module Goal**: learn to make Robby go left & right.

Let's learn how to turn `Robby` left and right.

## Stop & Turn

When you have a two-wheeled drive system like `Robby`, the wheels provide both the drive motion of the vehicle and also the steering control. How is that? Think of a tank. It only has tracks and yet it goes forward, backward, left, and right. Why? Because it can make the two tracks turn opposite directions from each other. `Robby` can do the same thing with its wheels!

In python, we have some commands that will help us do this:
* `stop()` will make the wheels stop spinning;
* `sleep()` will make the current motion continue for some amount of time;
* `left()` will make `Robby` turn left;
* `right()` will make `Robby` turn right.

Time to try it out. In `code-oss`, create a new file and add this:

```python
#!/bin/python3

# left turn module
from gpiozero import Robot
import time

# Students: modify the left/right numbers based on your design!
robby = Robot(left=(7, 8), right=(9, 10))

robby.left(turn_speed)
time.sleep(1.0)
robby.stop()
```

Make sure you save it: `turn_left.py`.

Then run it. In the terminal:
* Change directories by typing `cd robotics_class` and then **Enter**
* `python3 turn_left.py` and then **Enter**

`Robby` should have turned left by some amount. Maybe not much, maybe a lot. Discuss what happened.

**Challenge**: what can you do to make `Robby` turns a precise 90-degrees? Make it happen!

## Turning While Going Forward

TODO
* Turn left/right while going forward
  * Make the vehicle turn in a circle


---

**Module Complete**
