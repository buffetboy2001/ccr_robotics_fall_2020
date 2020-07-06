import setup
from gpiozero import LineSensor
from signal import pause
from time import sleep

robby = None

def left_line_detected_response():
    pass

def right_line_detected_response():
    pass

def when_no_line_do_this():
    robby.forward()
    return

if __name__ == "__main__":
    '''
    Run robby & follow the line indefinitely
    '''

    # Setup Robby
    robby = setup.get_robby()
    left_sensor = LineSensor(21)
    right_sensor = LineSensor(14)

    # line detected behavior
    left_sensor.when_no_line = when_no_line_do_this
    right_sensor.when_no_line = when_no_line_do_this

    # no line detected behavior
    left_sensor.when_line = lambda: print('No line detected') # when_no_line_do_this()
    right_sensor.when_line = lambda: print('No line detected') # when_no_line_do_this()

    pause()
    
    print("done")
