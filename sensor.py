from pybricks.hubs import MoveHub
from pybricks.pupdevices import Motor, ColorDistanceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

def main():
    cds = ColorDistanceSensor(port=Port.C)
    print("go")
    while True:
        print(cds.distance())
        print(cds.color())
        wait(500)

if __name__ == "__main__":
    main()