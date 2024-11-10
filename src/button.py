from machine import Pin  # type: ignore


class Button:
    def __init__(self, pin: int):
        self.button = Pin(pin, Pin.IN, Pin.PULL_UP)
        self.pressed = False

    def set_pressed(self) -> None:
        if self.button.value() == 0:
            self.pressed = True

    def is_released(self) -> bool:
        if self.pressed and self.button.value() == 1:
            self.pressed = False
            return True

        return False
