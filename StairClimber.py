from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch


'''
This is the code for our stair climbing robot
'''
class StairClimber:
    def __init__(self, left_motor, right_motor, carriage_motor, dist_sensor, color_sensor):
        self.left_motor = left_motor
        self.right_motor = right_motor
        self.carriage_motor = carriage_motor
        self.color_sensor = color_sensor

    # move forward function
    def move_forward(self):
        pass

    # turn function
    def turn_robot(self, degrees)

