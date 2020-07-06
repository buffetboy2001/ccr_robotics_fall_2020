import setup
from gpiozero import LineSensor
from signal import pause
from time import sleep
 
def left_line_detected_response():
    pass

def right_line_detected_response():
    pass

def when_no_line_do_this():
    pass

if __name__ == "__main__":
    '''
    Run robby & follow the line indefinitely
    '''

    # Setup Robby
    robby = setup.get_robby()
    left_sensor = LineSensor(21)
    right_sensor = LineSensor(2)

    left_sensor.when_line = lambda: print('Line detected @ left sensor') # left_line_detected_response()
    right_sensor.when_line = lambda: print('Line detected @ right sensor') # right_line_detected_response()
    left_sensor.when_no_line = lambda: print('No line detected') # when_no_line_do_this()
    right_sensor.when_no_line = lambda: print('No line detected') # when_no_line_do_this()

    pause()
    
    print("done")