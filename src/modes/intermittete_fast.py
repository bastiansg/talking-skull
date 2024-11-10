from .intermittent import IntermittentMode


class IntermittentFastMode:
    def __init__(self):
        self.mode = IntermittentMode(pwm_window=128)

    def run(self) -> None:
        self.mode.run()
