'''
Here is where we will run the program and we will be initializing all of the values
'''
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch



def main():
    hub = PrimeHub()
    # The ports can be changed when we have the actual robot

    back_wheels = Motor(Port.A)
    front_wheeels = Motor(Port.C)
    carraige_motor = Motor(Port.E)

    color_sensor = ColorSensor(Port.D)
    dist_sensor = UltrasonicSensor(Port.B)

    
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

