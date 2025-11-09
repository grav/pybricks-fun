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

```bash
pybricksdev run ble blink.py
```
