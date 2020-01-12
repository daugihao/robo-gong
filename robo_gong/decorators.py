from RPi import GPIO
from functools import wraps

from .safe_gpio import SafeGPIO



def with_gpio(pwm_pin):
    def inner(func):
        """
        This decorator ensure GPIO.cleanup() is called when function call ends, 
        also it injects GPIO as first argument into your function
        """
        @wraps(func)
        def wrapper(*args, **kwargs):
            with SafeGPIO(pwm_pin) as GPIO:
                return func(GPIO, *args, **kwargs)
        return wrapper
    return inner

