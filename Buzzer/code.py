import time
import board
import pwmio

# Define a list of tones/music notes to play.

TONE_FREQ = [
    1047,
    1047,
    1568,
    1568,
    1760,
    1760,
    1568,
    0,
    1397,
    1397,
    1319,
    1319,
    1175,
    1175,
    1047,
    0,
    1568,
    1568,
    1397,
    1397,
    1319,
    1319,
    1175,
    0,
    1568,
    1568,
    1397,
    1397,
    1319,
    1319,
    1175,
    0,
    1047,
    1047,
    1568,
    1568,
    1760,
    1760,
    1568,
    0,
    1397,
    1397,
    1319,
    1319,
    1175,
    1175,
    1047,
    0,
]

# Buzzer
buzzer = pwmio.PWMOut(board.GP27, variable_frequency=True)

buzzer.frequency = TONE_FREQ[0]
buzzer.duty_cycle = 32768

while True:
    for note in TONE_FREQ:
        if note:
            buzzer.frequency = note
        time.sleep(0.1)
