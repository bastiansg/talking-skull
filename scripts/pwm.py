from time import sleep
from machine import Pin, PWM


PWM_WAIT = 1e-3
PWM_MAX = 65025
PWM_WINDOW = 16


pwm = PWM(Pin(9))
pwm.freq(1000)

while True:
    for duty in range(0, PWM_MAX, PWM_WINDOW):
        pwm.duty_u16(duty)
        sleep(PWM_WAIT)

    for duty in range(PWM_MAX, 0, -PWM_WINDOW):
        pwm.duty_u16(duty)
        sleep(PWM_WAIT)

    pwm.duty_u16(0)
