from gpiozero import Robot

def get_robby():
    '''
    Create the Robot object with wheels configured
    '''
    robby = Robot(left=(8, 7), right=(9, 10))
    return robby
