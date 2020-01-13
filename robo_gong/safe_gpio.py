from RPi import GPIO
import warnings

class SafeGPIO(object):

	pwm_pin = None

	def __init__(self, pwm_pin):
		self.pwm_pin = pwm_pin

	def __enter__(self):
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(self.pwm_pin, GPIO.OUT)
		return GPIO

	def __exit__(self, *args, **kwargs):
		with warnings.catch_warnings():
			warnings.simplefilter("error")
			try:
				GPIO.cleanup()
			except RuntimeWarning:
				pass
