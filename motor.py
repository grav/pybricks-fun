from pybricks.pupdevices import Motor, ColorDistanceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop

def main() -> None:
    motor_a = Motor(Port.A, Direction.CLOCKWISE)
    motor_b = Motor(Port.B, Direction.CLOCKWISE)
    while True:
        motor_a.run_until_stalled(500)
        motor_b.run_until_stalled(500)

if __name__ == "__main__":
    main()
