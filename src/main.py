from machine import Pin  # type: ignore

from modes.intermittent import IntermittentMode
from modes.intermittete_fast import IntermittentFastMode
from modes.morse import MorseMode

from modes.led import blink_led
from components.mode import Mode
from components.button import Button


mode = Mode(
    modes=[
        IntermittentMode(),
        IntermittentFastMode(),
        MorseMode(),
    ]
)

button_03 = Button(pin=3)
button_26 = Button(pin=26)
onbd_led = Pin(25, Pin.OUT)
blink_led(
    pin=onbd_led,
    wait_time=0.5 / 4,
    n=(mode.mode + 1),
)

while True:
    button_03.set_pressed()
    if button_03.is_released():
        mode.next_mode()
        blink_led(
            pin=onbd_led,
            wait_time=0.5 / 4,
            n=(mode.mode + 1),
        )

    button_26.set_pressed()
    if button_26.is_released():
        break

while True:
    mode.run()
