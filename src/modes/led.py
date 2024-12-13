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


def set_pwm_duty(
    pwm: PWM,
    start: int,
    stop: int,
    step: int,
    pwm_wait: float,
) -> None:
    for duty in range(start, stop, step):
        pwm.duty_u16(duty)
        sleep(pwm_wait)


def set_pwm_duty_double(
    pwm_1: PWM,
    pwm_2: PWM,
    start: int,
    stop: int,
    step: int,
    pwm_wait: float,
) -> None:
    for duty in range(start, stop, step):
        pwm_1.duty_u16(duty)
        pwm_2.duty_u16(stop - duty)

        sleep(pwm_wait)


def turn_on_pwm(
    pwm: PWM,
    wait_time: float,
    dot_wait: float,
    pwm_wait: float,
    pwm_window: int,
    pwm_max: int = 65025,
):
    set_pwm_duty(
        pwm=pwm,
        start=0,
        stop=pwm_max,
        step=pwm_window,
        pwm_wait=pwm_wait,
    )

    sleep(wait_time)
    set_pwm_duty(
        pwm=pwm,
        start=pwm_max,
        stop=0,
        step=-pwm_window,
        pwm_wait=pwm_wait,
    )

    # Each dot or dash within an encoded character is followed by
    # a period of signal absence, called a space, equal to the dot duration
    sleep(dot_wait)
