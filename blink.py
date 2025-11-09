from pybricks.hubs import MoveHub
from pybricks.pupdevices import Motor, ColorDistanceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

def main() -> None:
    hub = MoveHub()
    for _ in range(5):
        hub.light.on(Color.RED)
        print("LED is RED")

        wait(500)

        hub.light.on(Color.GREEN)
        print("LED is GREEN")

        wait(500)


if __name__ == "__main__":
    main()
