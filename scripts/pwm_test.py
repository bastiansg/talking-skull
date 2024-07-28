from time import sleep
from machine import Pin, PWM


PWM_WAIT = 1e-6
PWM_MAX = 65025
PWM_WINDOW = 8
PWM_WAIT = 1e-6


pwm = PWM(Pin(13))
pwm.freq(1000)

while True:
    for duty in range(0, PWM_MAX, PWM_WINDOW):
        pwm.duty_u16(duty)
        sleep(PWM_WAIT)

    for duty in range(PWM_MAX, 0, -PWM_WINDOW):
        pwm.duty_u16(duty)
        sleep(PWM_WAIT)

    pwm.duty_u16(0)
