from time import sleep
from machine import Pin, PWM  # type: ignore


class IntermittentMode:
    def __init__(
        self,
        pwm_wait: float = 1e-3,
        pwm_max: int = 65025,
        pwm_window: int = 16,
    ):
        self.pwm_wait = pwm_wait
        self.pwm_max = pwm_max
        self.pwm_window = pwm_window

        self.pwm = PWM(Pin(9))
        self.pwm.freq(1000)

    def run(self) -> None:
        for duty in range(0, self.pwm_max, self.pwm_window):
            self.pwm.duty_u16(duty)
            sleep(self.pwm_wait)

        for duty in range(self.pwm_max, 0, -self.pwm_window):
            self.pwm.duty_u16(duty)
            sleep(self.pwm_wait)

        self.pwm.duty_u16(0)
