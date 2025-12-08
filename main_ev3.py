from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, GyroSensor, TouchSensor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Port, Direction, Button
from StairClimber_ev3 import StairClimberV2


def main():
    hub = EV3Brick()
    #The ports can be changed when we have the actual robot

    left_motor = Motor(Port.A)
    right_motor = Motor(Port.C)
    carriage_motor = Motor(Port.B)


    color_sensor = ColorSensor(Port.S1)
    dist_sensor = UltrasonicSensor(Port.S2)
    robot = StairClimberV2(left_motor, right_motor, carriage_motor, dist_sensor, color_sensor)
    robot.run()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

