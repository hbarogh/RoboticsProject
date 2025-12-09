from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

'''
This is the code for our stair climbing robot
- All of the measurements will be in cm
'''


class ClimbingDirections:
    UP = "up"
    DOWN = "down"


class StairClimber:
    def __init__(self, left_motor, right_motor, carriage_wheel_motor, carriage_motor, dist_sensor, color_sensor):
        self.left_motor = left_motor
        self.right_motor = right_motor
        self.carriage_wheel_motor = carriage_wheel_motor
        self.carriage_motor = carriage_motor
        self.dist_sensor = dist_sensor
        self.color_sensor = color_sensor
        self.number_of_steps = 0
        # making the drive base here and will be using this to control the robot
        wheel_diameter = 56  # this is in mm
        axel_track = 120  # might need to be changed later
        self.drive_base = DriveBase(self.left_motor, self.right_motor, wheel_diameter, axel_track)

    # FUNCTIONS THAT ARE DONE=========================================
    '''
    This is our move forward function and it keeps the robot moving forward until the ultrasonic sensor 
    detects something within 2 cm
    '''

    def move_forward(self, speed=700):
        print("inside move forward function")
        self.drive_base.drive(speed, 0)
        while not self.detect_step():
            wait(1)
        self.stop_robot()
        print("finished the move forward function")

    '''
    This function will stop the robot from moving horizontally
    '''

    def stop_robot(self):
        self.drive_base.stop()
        print("hit the stop robot function")

    '''
    This function will be detecting a step for the robot to CLIMB
    '''

    def detect_step(self):
        # this will be the true if there is something within 2 cm from the ultrasonic sensor
        step_detected = self.dist_sensor.distance() < 3000
        print(f"step detected: {step_detected}")
        return step_detected

    '''
    This function will be used to detect when there is step there when the robot is decending
'''

    def detect_step_descending(self):
        color = self.color_sensor.color()
        # if we see black, need to check if there is a big change in distance from the ultrasonic sensor
        # if there is a distance greater than 10 cm, then we know that we have hit the top of the stairs
        if color == Color.BLACK:
            return self.dist_sensor.distance() > 100
        return False

    '''
        This will be the function to rotate the robot
    '''

    def turn_robot(self, degrees):
        self.drive_base.turn(degrees)

    '''
    This will be the function for operating the carriage motor
    '''

    def operate_carriage_motor(self, speed, target_angle):
        self.carriage_motor.run_target(speed, target_angle)
        # self.carriage_motor.run_until_stalled(speed, duty_limit=90)

    '''
        This will be the function of raising/lowering the carriage and also how much we need to adjust it by
    '''

    def operate_carriage(self, direction):
        if direction == ClimbingDirections.UP:
            self.operate_carriage_motor(2000, 1000)
        else:  # this will be for when we need the direction to go down
            self.operate_carriage_motor(-250, -1000)

    # FUNCTIONS THAT NEED TO BE COMPLETED==============================
    '''
    This will be the function for climbing a step 
    '''

    def climb_step(self):
        # 3-step process
        # 1st step accelerate with both front and back motors, and then we will also be lowering the carriage to keep back wheels on the ground

        self.move_forward()
        self.operate_carriage(ClimbingDirections.UP)
        # 2nd step: we need the carriage wheel motors to run so that the carriage wheels are flush with the stair
        watch = StopWatch()
        while watch.time() < 1000:
            self.carriage_wheel_motor.run(200)

        # 3rd step: will be to accelerate with front motors and raising the carriage
        self.operate_carriage(ClimbingDirections.DOWN)

        self.number_of_steps += 1

    '''
    This will be the function for going down steps
    '''

    def descend_step(self):
        # every time we go down a step we will be subtracting one from the num_steps
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
        # if we see black, need to check if there is a big change in distance from the ultrasonic sensor
        # if there is a distance greater than 5 cm, then we know that we have hit the top of the stairs
        if color == Color.BLACK:
            if self.dist_sensor.distance() > 50:
                print("completed ascent")
                return True

        return False

    '''
    This will be the main function for how the robot runs and will be climbing robots
    '''

    def run(self):

        # # going to have a ascending part of running and descending part of running
        # while not self.completed_ascent():
        #     if not self.detect_step():
        #         self.move_forward()
        #     else:
        #         print("hit inside the else")
        #         self.climb_step()

        # # this will be the descending part of running the program
        # # first need to turn the robot
        # while not self.completed_descent():
        #     if not self.detect_step_descending():
        #         self.move_forward()
        #     else:
        #         self.descend_step()

        while not self.completed_ascent():
            print("trying to operate carriage")
            watch = StopWatch()

            self.drive_base.drive(500, 0)
            self.carriage_motor.run(700)  # NON-BLOCKING
            self.carriage_wheel_motor.run(700)  # NON-BLOCKING

            while watch.time() < 5000:
                wait(10)

            self.drive_base.stop()
            self.carriage_motor.stop()
            self.carriage_wheel_motor.stop()
            self.drive_base.drive(500, 0)
            self.operate_carriage(ClimbingDirections.DOWN)
            print("finished the while loop")


