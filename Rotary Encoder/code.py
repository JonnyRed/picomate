import rotaryio
import board
import digitalio

encoder = rotaryio.IncrementalEncoder(board.GP7, board.GP6)
switch = digitalio.DigitalInOut(board.GP26)
switch.direction = digitalio.Direction.INPUT
switch.pull = digitalio.Pull.DOWN
last_position = encoder.position

switch_state = switch.value
while True:
    position = encoder.position

    if last_position is None or position != last_position:
        print(f"Rotary: {position}")

    last_position = position

    if switch_state != switch.value:
        switch_state = switch.value
        print("Switch is " + ("ON" if switch.value else "OFF"))
