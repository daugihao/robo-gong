from time import sleep

from robo_gong.decorators import with_gpio

PWM_PIN = 11

SPEED=1
SWING_START=35
SWING_HIGH=50
SWING_END=20

@with_gpio(PWM_PIN)
def strike(GPIO):
	p = GPIO.PWM(PWM_PIN, 50)
	p.start(SWING_END/10.)
	p.ChangeDutyCycle(SWING_END/10.)

@with_gpio(PWM_PIN)
def back_swing(GPIO):
	p = GPIO.PWM(PWM_PIN, 50)
	p.start(0)
	p.ChangeDutyCycle(SWING_START/10.)
	for step in range(SWING_START,SWING_HIGH,4):
		sleep(1./SPEED)
		p.ChangeDutyCycle(step/10.)
