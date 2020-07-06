import setup
from gpiozero import LineSensor
from signal import pause
from time import sleep

robby = None

def left_line_detected_response():
    print('turn left slightly')
    robby.forward(curve_left=.5)  # async
    return

def right_line_detected_response():
    print('turn right slightly')
    robby.forward(curve_right=.5)  # async
    return

def when_no_line_do_this():
    robby.forward(.5)
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

    # find the line first by hunting left & right
    while right_sensor.value > 0.25:
        robby.left(0.5)  # async
        sleep(.1) 

    pause()
    
    print("done")
