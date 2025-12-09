from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from StairClimber import StairClimber

hub = PrimeHub()



def main():
    hub = PrimeHub()
    #The ports can be changed when we have the actual robot
    left_motor = Motor(Port.F, Direction.COUNTERCLOCKWISE)
    right_motor = Motor(Port.E, Direction.CLOCKWISE)
    carriage_motor = Motor(Port.C, Direction.COUNTERCLOCKWISE)
    carriage_wheel_motor = Motor(Port.D, Direction.CLOCKWISE)

    color_sensor = ColorSensor(Port.B)
    dist_sensor = UltrasonicSensor(Port.A)
    robot = StairClimber(left_motor, right_motor, carriage_wheel_motor, carriage_motor, dist_sensor, color_sensor)
    robot.run()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

