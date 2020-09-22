# Raspberry Pi Communication

Your Pi is a computer on it's own. But, it's not connected to a monitor, keyboard, or mouse. :( So, if you want to see it and type words on it...what ya gonna do?

Follow these instructions to get your Kano connected to your Pi. This will allow you to wirelessly control the Pi from your Kano.

You will need these on your project mat:

* USB Battery Pack
* Raspberry Pi
* USB-C wire

Next:

* Turn on your Kano and log in as `Team-whatever`
* Make sure you have an internet connection
    * Get Mr. Bowman if you don't!
* Turn on the Mobile Hotspot connection
* Connect the USB-C to your Pi and then to your USB battery pack
    * This should make your Pi come alive! Look for Red & Green LEDs.
* On the Kano, you should see the Pi connect in the Mobile Hotspot page
    * Figure out the IP address of the Pi -- Mr. Bowman can show you how
* On the Kano:
    * Open a terminal window
    * Type: `ssh pi@<rpi_ip>`
    * Type: `./run_vncserver.sh`
    * Type: `exit`
    * Open VNC Viewer
    * Connect to the Pi
* In the Pi view, open your code editor:
    * `code-oss` is your friend when it comes to writing Python code!

FYI: This connection to you Pi will last for as long as the Pi is on. If you turn it off or run out of battery power for the Pi, the connection will drop.
