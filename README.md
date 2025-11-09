# Pybricks fun

MicroPython getting started for the Lego Boost robot.

## Installing Pybricks firmware

1. Go to <https://code.pybricks.com/>
2. Press cogwheel -> Install Pybricks -> Follow guide, selecting the "BOOST Move Hub"

## Deps/venv managed via UV

```bash
uv venv
source .venv/bin/activate        
```

## Uploading hello world

Ensure that the Boost is turned on (pressing the button)

```bash
pybricksdev run ble blink.py
```

## Running the program

Just press that button!

## Shutting down

Hold that button!
