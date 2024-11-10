from time import sleep
from machine import Pin, PWM  # type: ignore

from .text import normalize_text, get_encoded_chars
from .led import turn_on_led, blink_led, turn_on_pwm


DEFAULT_MESSAGE = "human after all"


class MorseMode:
    def __init__(
        self,
        dot_wait: float = 0.5,
        char_pause_symbol: str = "@",
        word_pause_symbol: str = "#",
        pwm_wait: float = 1e-3,
        pwm_max: int = 65025,
        pwm_window: int = 32,
        message: str = DEFAULT_MESSAGE,
    ):
        self.dot_wait = dot_wait
        self.dash_wait = dot_wait * 3
        self.blink_wait = dot_wait / 4

        self.char_pause_symbol = char_pause_symbol
        self.word_pause_symbol = word_pause_symbol
        self.pwm_wait = pwm_wait
        self.pwm_max = pwm_max
        self.pwm_window = pwm_window

        self.encoded_message = self._get_encoded_message(message=message)
        print(f"encoded_message => {self.encoded_message}")

        self.pwm = PWM(Pin(9))
        self.pwm.freq(1000)
        self.onbd_led = Pin(25, Pin.OUT)

    def _get_encoded_message(self, message: str) -> str:
        message = normalize_text(message)
        encoded_words = (
            get_encoded_chars(
                word=word,
                char_pause_symbol=self.char_pause_symbol,
            )
            for word in message.split()
        )

        return f"{self.word_pause_symbol}".join(encoded_words)

    def run(self) -> None:
        for symbol in self.encoded_message:
            # The dot duration is the basic unit of time measurement
            if symbol == ".":
                turn_on_pwm(
                    pwm=self.pwm,
                    wait_time=self.dot_wait,
                    dot_wait=self.dot_wait,
                    pwm_wait=self.pwm_wait,
                    pwm_window=self.pwm_window,
                )

                continue

            # The duration of a dash is three times the duration of a dot
            if symbol == "-":
                turn_on_pwm(
                    pwm=self.pwm,
                    wait_time=self.dash_wait,
                    dot_wait=self.dot_wait,
                    pwm_wait=self.pwm_wait,
                    pwm_window=self.pwm_window,
                )

                continue

            # The letters of a word are separated by a space of duration
            # equal to three dots (one dash)
            if symbol == self.char_pause_symbol:
                blink_led(self.onbd_led, self.blink_wait, 1)
                sleep(self.dash_wait)
                continue

            # Words are separated by a space equal to seven dots
            if symbol == self.word_pause_symbol:
                blink_led(self.onbd_led, self.blink_wait, 2)
                sleep(self.dot_wait * 7)

        turn_on_led(self.onbd_led, self.dot_wait * 20)
