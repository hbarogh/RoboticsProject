from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from enum import Enum

'''
This is the code for our stair climbing robot

- back_motor is the motor that controls the back wheels
- front motor is the motor that controls the front wheels

- All of the measurements will be in cm
'''


class ClimbingDirections(Enum):
    UP = "up"
    DOWN = "down"


class StairClimber:
    def __init__(self, left_motor, right_motor, carriage_motor, dist_sensor, color_sensor):
        self.left_motor = left_motor
        self.right_motor = right_motor
        self.carriage_motor = carriage_motor
        self.dist_sensor = dist_sensor
        self.color_sensor = color_sensor

        #making the drive base here and will be using this to control the robot
        wheel_diameter = 56 #this is in mm
        axel_track = 120 #might need to be changed later
        self.drive_base = DriveBase(self.left_motor, self.right_motor, wheel_diameter, axel_track)

    # FUNCTIONS THAT ARE DONE=========================================
    '''
    This is our move forward function and it keeps the robot moving forward until the ultrasonic sensor 
    detects something within 2 cm
    '''
    def move_forward(self, speed=200):
        while self.dist_sensor.distance() > 20:
            self.drive_base.drive(speed, 0) #putting zero for the turn rate
        self.stop_robot()

    '''
    This function will stop the robot from moving horizontally
    '''

    def stop_robot(self):
        self.drive_base.stop()

    '''
    This function will be detecting a step for the robot to CLIMB
    '''

    def detect_step(self):
        # this will just be returning if a step is within the threshold
        # this will be the true if there is something within 2 cm from the ultrasonic sensor
        return self.dist_sensor.distance() < 20

    '''
        This will be the function to rotate the robot
        '''

    def turn_robot(self, degrees):
        self.drive_base.turn(degrees)  # for full roation we can just use 360 for 360 degrees

    # FUNCTIONS THAT NEED TO BE COMPLETED==============================


    '''
    This will be the function for operating the carriage motor
    - this will be where we will need to operate the carriage motor and will need to have the degrees and distance
    '''

    def operate_carriage_motor(self, dist):

        # calculating the input to the run function here: NEED TO DO THIS ==============================================
        self.carriage_motor.run()

    '''
    This will be the function for climbing a step 
    '''

    def climb_step(self):
        # 3 step process
        # 1st step accellerate with both front and back motors, and then we will also be lowering the carriage to keep back wheels on the ground
        self.move_forward()
        self.operate_carriage(ClimbingDirections.DOWN)

        # 2nd step: need a way to determine when we have completed step 1
        # DO THIS PART=====================================================

        # 3rd step: will be to accellerate with front motors and raising the carriage
        self.move_forward()
        self.operate_carriage(ClimbingDirections.UP)

    '''
    This will be the function of raising/lowering the carrraige and also how much we need to adjust it by
    FINISH FUNCTION!!!
    '''

    def operate_carriage(self, direction):
        if direction == ClimbingDirections.UP:
            self.operate_carriage_motor(30)  # this will be changed need to calculate the input that we need to put in there ********************
        else:  # this will be for when we need the direction to go down
            self.operate_carriage_motor(-30)  # also need to get this done **********************************

    '''
    This will be the function to determine if we have completed the descent of the stairs
    - One way we could do it is that we could log how many stairs that we climbed to do the acsent and then once we have climbed 
    down that amount then we are at that descent and done. Not sure if that's allowed
    '''

    def completed_descent(self):

        pass

    '''
    This function will be used to determine if we have completed the ascent of the stairs
    '''

    def completed_ascent(self):
        pass

    '''
    This will be the main function for how the robot runs and will be climbing robots
    '''

    def run(self):

        # going to have a ascending part of running and decsending part of running
        while not self.completed_ascent():
            if not self.detect_step():
                self.move_forward()
            else:
                self.climb_step()

        # this will be the descending part of running the program
        # first need to turn the robot
        self.turn_robot(360)
        while not self.completed_descent():
            if not self.detect_step_descent():
                self.move_forward()
            else:
                self.descend_step()
