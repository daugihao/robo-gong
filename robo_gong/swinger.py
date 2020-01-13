from time import sleep

from robo_gong.decorators import with_gpio

PWM_PIN = 11

SPEED=10
SWING_START=35
SWING_HIGH=55
SWING_END=20

@with_gpio(PWM_PIN)
def strike(GPIO):
	p = GPIO.PWM(PWM_PIN, 50)
	p.start(0)
	p.ChangeDutyCycle(1.8)
	sleep(.5)
	p.ChangeDutyCycle(3.)
	sleep(.5)

@with_gpio(PWM_PIN)
def back_swing(GPIO):
	p = GPIO.PWM(PWM_PIN, 50)
	p.start(0)
	p.ChangeDutyCycle(8.)
	sleep(2)
	#p.ChangeDutyCycle(SWING_HIGH/10.)
	#for step in range(SWING_START,SWING_HIGH,10):
	#	sleep(1./SPEED)
	#	p.ChangeDutyCycle(step/10.)
