from modes.intermittent import IntermittentMode
from modes.morse import MorseMode

from mode import Mode
from button import Button


mode = Mode(
    modes=[
        IntermittentMode(),
        MorseMode(),
    ]
)

button_03 = Button(pin=3)
button_26 = Button(pin=26)


while True:
    button_03.set_pressed()
    if button_03.is_released():
        mode.next_mode()

    button_26.set_pressed()
    if button_26.is_released():
        break

while True:
    mode.run()
