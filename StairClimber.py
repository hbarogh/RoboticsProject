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
        self.number_of_steps = 0
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
        self.drive.drive(speed, 0)
        while self.dist_sensor.distance() > self.detect_distance:
            wait(10)
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
        # this will be the true if there is something within 2 cm from the ultrasonic sensor
        return self.dist_sensor.distance() < 20

    '''
        This will be the function to rotate the robot
        '''

    def turn_robot(self, degrees):
        self.drive_base.turn(degrees)  # for full roation we can just use 360 for 360 degrees

    '''
    This will be the function for operating the carriage motor
    '''

    def operate_carriage_motor(self, speed):
        self.carriage_motor.run_until_stalled(speed)

    '''
        This will be the function of raising/lowering the carriage and also how much we need to adjust it by
        '''

    def operate_carriage(self, direction):
        if direction == ClimbingDirections.UP:
            self.operate_carriage_motor(200)
        else:  # this will be for when we need the direction to go down
            self.operate_carriage_motor(-200)


    # FUNCTIONS THAT NEED TO BE COMPLETED==============================
    '''
    This will be the function for climbing a step 
    '''
    def climb_step(self):
        # 3-step process
        # 1st step accelerate with both front and back motors, and then we will also be lowering the carriage to keep back wheels on the ground

        self.move_forward()
        self.operate_carriage(ClimbingDirections.DOWN)

        # 2nd step: need a way to determine when we have completed step 1
        # DO THIS PART=====================================================

        # 3rd step: will be to accelerate with front motors and raising the carriage
        self.move_forward()
        self.operate_carriage(ClimbingDirections.UP)
        self.number_of_steps += 1

    '''
    This will be the function for going down steps
    '''
    def descend_step(self):
        #every time we go down a step we will be subtracting one from the num_steps
        self.number_of_steps -= 1
        pass


    '''
    This will be the function to determine if we have completed the descent of the stairs
    - One way we could do it is that we could log how many stairs that we climbed to do the accent and then once we have climbed 
    down that amount then we are at that descent and done.
    '''
    def completed_descent(self):
        num_steps = self.number_of_steps
        if num_steps == 0:
            return True

        return False

    '''
    This function will be used to determine if we have completed the ascent of the stairs
    - One way we could do this is by looking for the color black and then see if the distance using the ultrasonic
    sensor is really far or has a big jump (if it hangs over the edge) and then we would know that we have completed 
    the ascent.
    '''
    def completed_ascent(self):
        color = self.color_sensor.color()
        #if we see black, need to check if there is a big change in distance from the ultrasonic sensor
        #if there is a distance greater than 5 cm, then we know that we have hit the top of the stairs
        if color == Color.BLACK:
            if self.dist_sensor.distance() > 50:
                return True

        return False



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
