from time import sleep
from machine import Pin


MESSAGE = "ruido de ola"


DOT_WAIT = 0.5
DASH_WAIT = DOT_WAIT * 3
BLINK_WAIT = DOT_WAIT / 4

CHAR_PAUSE_SIMBOL = "@"
WORD_PAUSE_SIMBOL = "#"


CODE_MAP = {
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "ñ": "--.--",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
    ", ": "--..--",
    ".": ".-.-.-",
    "?": "..--..",
    "/": "-..-.",
    "-": "-....-",
    "(": "-.--.",
    ")": "-.--.-",
}


def normalize_text(text: str) -> str:
    text = " ".join(text.split())
    return text


def get_encoded_chars(word: str) -> str:
    encoded_chars = f"{CHAR_PAUSE_SIMBOL}".join(
        CODE_MAP[char] for char in word
    )

    return encoded_chars


def turn_on_led(pin: Pin, wait_time: float):
    pin.value(1)
    sleep(wait_time)
    pin.value(0)


def blink_led(pin: Pin, wait_time: float, n: int):
    for _ in range(n):
        turn_on_led(pin, wait_time)
        sleep(wait_time)


message = normalize_text(MESSAGE)
encoded_words = (get_encoded_chars(word) for word in message.split())
encoded_message = f"{WORD_PAUSE_SIMBOL}".join(encoded_words)

pin_13 = Pin(13, Pin.OUT)
onbd_led = Pin(25, Pin.OUT)

while True:
    for symbol in encoded_message:
        # The dot duration is the basic unit of time measurement
        if symbol == ".":
            turn_on_led(pin_13, DOT_WAIT)
            sleep(DOT_WAIT)
            continue

        # The duration of a dash is three times the duration of a dot
        if symbol == "-":
            turn_on_led(pin_13, DASH_WAIT)
            sleep(DOT_WAIT)
            continue

        # The letters of a word are separated by a space of duration
        # equal to three dots (one dash)
        if symbol == CHAR_PAUSE_SIMBOL:
            blink_led(onbd_led, BLINK_WAIT, 1)
            sleep(DASH_WAIT)
            continue

        # Words are separated by a space equal to seven dots
        if symbol == WORD_PAUSE_SIMBOL:
            blink_led(onbd_led, BLINK_WAIT, 2)
            sleep(DOT_WAIT * 7)

    turn_on_led(onbd_led, DOT_WAIT * 20)
