from time import sleep
from machine import Pin, PWM  # type: ignore


def turn_on_led(pin: Pin, wait_time: float):
    pin.value(1)
    sleep(wait_time)
    pin.value(0)


def blink_led(pin: Pin, wait_time: float, n: int):
    for _ in range(n):
        turn_on_led(pin, wait_time)
        sleep(wait_time)


def turn_on_pwm(
    pwm: PWM,
    wait_time: float,
    dot_wait: float,
    pwm_wait: float,
    pwm_window: int,
    pwm_max: int = 65025,
):
    for duty in range(0, pwm_max, pwm_window):
        pwm.duty_u16(duty)
        sleep(pwm_wait)

    sleep(wait_time)

    for duty in range(pwm_max, 0, -pwm_window):
        pwm.duty_u16(duty)
        sleep(pwm_wait)

    # Each dot or dash within an encoded character is followed by
    # a period of signal absence, called a space, equal to the dot duration
    sleep(dot_wait)
