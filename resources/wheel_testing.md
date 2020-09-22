# Wheel Testing and Basic Assembly

Before doing the full assembly, you'll need to make sure your wheels work. This module will show you how to test it all -- using the Pi.

You will need these on your project mat:

* the Motor Controller Board (L298N)
* AA battery holder
* Both motors (wheels don't need to be connected). 
* Raspberry Pi

![mat view](pics/components_on_mat.jpg)

## Drive Wheel Assembly Steps

* On the L298N Motor Controller board, identify the wire ports labeled:
    * OUT1, OUT2, OUT3, OUT4, GND, 12V.
    * Make sure at least two teammates can find them.
* Using a screwdriver, loosen the screws in the terminal blocks labeled OUT1, OUT2, OUT3, and OUT4. Insert the ends of four wires into the terminal blocks.
* Connect the wires from the battery holder to the L298N Motor Controller board.
    * Black wire to GND
    * Red wire to 12V
* Tighten all screws _gently_ so that the wires stay in-place.

## Power Assembly

The Raspberry Pi computer can only provide so much electrical energy to other things connected to it. In the case of the L298N motor controller and the wheels, they need more electricity than the Pi can give. :( 

No worries! You'll fix this problem by also connecting 4 AA batteries and use _those_ to power the wheels.

* On the L298N Motor Controller board, identify the wire ports labeled:
    * 12V, GND
    * Make sure at least two teammates can find them.
* Get the AA battery case
* Loosen the screws on those and insert:
    * the red wire on the AA battery case to 12V
    * the black wire on the AA battery case to GND
* Tighten all screws _gently_ so that the wires stay in-place.

## Connect the Raspberry Pi to your Components

Time to get your components connected to the robot brain -- the Raspberry Pi!
