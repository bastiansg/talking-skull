from time import sleep
from machine import Pin, PWM


MESSAGE = (
    "ese fantasma que corre delante de ti, hermano mio, es mas bello que tu "
    "por que no le das tu carne y tus huesos?"
)

DOT_WAIT = 0.5
DASH_WAIT = DOT_WAIT * 3
BLINK_WAIT = DOT_WAIT / 4

CHAR_PAUSE_SIMBOL = "@"
WORD_PAUSE_SIMBOL = "#"

PWM_MAX = 65025
PWM_WINDOW = 8
PWM_WAIT = 1e-3

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
    ",": "--..--",
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
    encoded_chars = f"{CHAR_PAUSE_SIMBOL}".join(CODE_MAP[char] for char in word)
    return encoded_chars


def turn_on_pwm(pwm: PWM, wait_time: float):
    for duty in range(0, PWM_MAX, PWM_WINDOW):
        pwm.duty_u16(duty)
        sleep(PWM_WAIT)

    sleep(wait_time)

    for duty in range(PWM_MAX, 0, -PWM_WINDOW):
        pwm.duty_u16(duty)
        sleep(PWM_WAIT)

    # Each dot or dash within an encoded character is followed by
    # a period of signal absence, called a space, equal to the dot duration
    sleep(DOT_WAIT)


def turn_on_led(led: Pin, wait_time: float):
    led.value(1)
    sleep(wait_time)
    led.value(0)


def blink_led(led: Pin, wait_time: float, n: int):
    for _ in range(n):
        turn_on_led(led, wait_time)
        sleep(wait_time)


message = normalize_text(MESSAGE)
encoded_words = (get_encoded_chars(word) for word in message.split())
encoded_message = f"{WORD_PAUSE_SIMBOL}".join(encoded_words)

pwm = PWM(Pin(9))
pwm.freq(1000)
onbd_led = Pin(25, Pin.OUT)

while True:
    for symbol in encoded_message:
        # The dot duration is the basic unit of time measurement
        if symbol == ".":
            turn_on_pwm(pwm, DOT_WAIT)
            continue

        # The duration of a dash is three times the duration of a dot
        if symbol == "-":
            turn_on_pwm(pwm, DASH_WAIT)
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
