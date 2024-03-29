import board
import digitalio

button = digitalio.DigitalInOut(board.GP26)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP

last_value = button.value
while True:
    if last_value != button.value:
        last_value = button.value
        print("Button is " + ("released" if button.value else "pressed"))
