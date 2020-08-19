# Disorganized Material & Content

* L298N focused discussion: https://www.teachmemicro.com/use-l298n-motor-driver/
* Line Following Discussion: https://create.arduino.cc/projecthub/robocircuits/line-follower-robot-arduino-299bae
* Switch Circuit: https://www.circuitbasics.com/how-to-set-up-buttons-and-switches-on-the-raspberry-pi/
* 3D Base Plate for Pi: https://www.thingiverse.com/thing:4175498

## Pre-class Setup Todo

*  Make each Kano to setup a wifi share by default. Make each rpi connect only to correct kano.


----

## Building Robby: A Simple Guide

_by Mr. Bowman_

This guide has my name on it, but is lovingly based on the wonderful guide found [on raspberrypi.org](https://projects.raspberrypi.org/en/projects/build-a-buggy). In some cases, I have even copied & pasted their text. :) Think of this as a modern example of pseudopigraphy.

### Vehicle Assembly

* Design Decision: Figure out which end is forward. Draw an arrow on the board pointing forward
* Decorate your chassis! May as well. You have markers -- take turns & go for it!
* Design Decision: Decide if you want to use one castor wheel or two. Screw them into place.

### Wheel Testing & Assembly

You will need these on your project mat:

* the Motor Controller Board (L298N)
* AA battery holder
* Both motors (wheels don't need to be connected). Wires must be connected.
* Raspberry Pi

Assembly Steps:

* On the L298N Motor Controller board, identify the wire ports labeled:
    * OUT1, OUT2, OUT3, OUT4, GND, 12V. 
    * Make sure at least two teammates can find them.
* Using a screwdriver, loosen the screws in the terminal blocks labeled OUT1, OUT2, OUT3, and OUT4. Insert the stripped ends of wire into the terminal blocks.
* Connect the wires from the battery holder to the L298N Motor Controller board.
    * Black wire to GND
    * Red wire to 12V
* Tighten all screws _gently_ so that the wires stay in-place.


