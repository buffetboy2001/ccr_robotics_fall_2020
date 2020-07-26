import setup
from gpiozero import LineSensor
from signal import pause
from time import sleep

DEADBAND_DURATION_SEC = 0.2
FORWARD_SPEED = 0.5 # below 0.5 and there is too much friction to move

robby = None

def left_line_detected_response():
    print('turn left')
    robby.forward(curve_left=0.85)
    sleep(DEADBAND_DURATION_SEC)
    robby.forward(FORWARD_SPEED)
    return

def right_line_detected_response():
    print('turn right')
    robby.forward(curve_right=0.85)
    sleep(DEADBAND_DURATION_SEC)
    robby.forward(FORWARD_SPEED)
    return

def when_no_line_do_this():
    robby.forward(FORWARD_SPEED)
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
    left_sensor.when_line = left_line_detected_response
    right_sensor.when_line = right_line_detected_response

    # start by going forward
    robby.forward(FORWARD_SPEED)
    pause()
    
    print("done")
