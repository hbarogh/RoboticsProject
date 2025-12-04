from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

'''
This is the code for our stair climbing robot

- back_motor is the motor that controls the back wheels
- front motor is the motor that controls the front wheels

- All of the measurements will be in cm
- NEED TO DO'S:
    - GET THE RIGHT PORTS FOR ALL OF THE THINGS
    - MEASURE FROM THE ULTRASONIC SENSOR TO THE GROUND
    - 
'''


class StairClimber:
    def __init__(self, back_motor, front_motor, carriage_motor, dist_sensor, color_sensor):
        self.back_motor = back_motor
        self.front_motor = front_motor
        self.carriage_motor = carriage_motor
        self.dist_sensor = dist_sensor
        self.color_sensor = color_sensor

    # FUNCTIONS THAT ARE DONE=========================================
    '''
    This is our move forward function and it keeps the robot moving forward until the ultrasonic sensor 
    detects something within 2 cm
    '''

    def move_forward(self, speed=200):
        while self.dist_sensor.distance() > 20:
            self.back_motor.run(speed)
            self.front_motor.run(speed)

        self.stop_robot()

    '''
    This function will stop the robot from moving horizontally
    '''

    def stop_robot(self):
        self.back_motor.brake()
        self.front_motor.brake()

    # FUNCTIONS THAT NEED TO BE COMPLETED==============================

    '''
    This will be the function to rotate the robot
    COMPLETE THIS FUNCTION
    '''

    def turn_robot(self, degrees):
        pass

    '''
    This function will be detecting a step for the robot to CLIMB
    '''

    def detect_step(self):
        # this will just be returning if a step is within the threshold
        # this will be the true if there is something within 2 cm from the ultrasonic sensor
        return self.dist_sensor.distance() < 20

    '''
    This function will be used to determine if we have completed the ascent of the stairs
    FINISH THIS FUNCTION!!!!!!!!!!!!!!!!!
    '''

    def completed_ascent(self):
        pass

    '''
    This will be the function of raising the carrraige and also how much we need to raise it by
    FINISH FUNCTION!!!
    '''

    def raise_carriage(self):
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
        self.turn_robot()
        while not self.completed_descent():
            if not self.detect_step_descent():
                self.move_forward()
            else:
                self.descend_step()
