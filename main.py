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

    left_motor = Motor(Port.A)
    right_motor = Motor(Port.C)
    carriage_motor = Motor(Port.E)


    color_sensor = ColorSensor(Port.D)
    dist_sensor = UltrasonicSensor(Port.B)
    robot = StairClimber(left_motor, right_motor, carriage_motor, dist_sensor, color_sensor)
    robot.run()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

