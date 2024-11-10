from machine import Pin, PWM  # type: ignore

from .led import set_pwm_duty


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
        set_pwm_duty(
            pwm=self.pwm,
            start=0,
            stop=self.pwm_max,
            step=self.pwm_window,
            pwm_wait=self.pwm_wait,
        )

        set_pwm_duty(
            pwm=self.pwm,
            start=self.pwm_max,
            stop=0,
            step=-self.pwm_window,
            pwm_wait=self.pwm_wait,
        )

        self.pwm.duty_u16(0)
