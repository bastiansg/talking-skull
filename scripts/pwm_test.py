from time import sleep
from machine import Pin, PWM

PWM_WAIT = 1e-6
pwm = PWM(Pin(13))

while True:
    for duty in range(0, 65025, 4):
        pwm.duty_u16(duty)
        sleep(PWM_WAIT)

    for duty in range(65025, 0, -4):
        pwm.duty_u16(duty)
        sleep(PWM_WAIT)

    pwm.duty_u16(0)
