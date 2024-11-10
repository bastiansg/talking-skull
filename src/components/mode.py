class Mode:
    def __init__(self, modes: list):
        self.modes = modes
        self.mode = 0

    def next_mode(self) -> None:
        self.mode = 0 if self.mode == (len(self.modes) - 1) else self.mode + 1

    def run(self) -> None:
        self.modes[self.mode].run()
