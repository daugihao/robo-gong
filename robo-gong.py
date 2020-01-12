import requests
import RPi.GPIO as GPIO

from time import sleep
from sys import argv

INTERVAL = 5
SERVICE_VERSIONS={'simulation-framework': None}
SPEED=1
SWING_START=35
SWING_HIGH=50
SWING_END=20

#GPIO.cleanup()
def gong():
	print("Start GPIO")
	GPIO.setmode(GPIO.BOARD)

	PWM_PIN = 11

	GPIO.setup(PWM_PIN,GPIO.OUT)
	p = GPIO.PWM(PWM_PIN, 50)
	p.start(0)
	p.ChangeDutyCycle(SWING_START/10.)
	for step in range(SWING_START,SWING_HIGH,4):
		p.ChangeDutyCycle(step/10.)
		sleep(1./SPEED)
	p.ChangeDutyCycle(SWING_END/10.)
	sleep(1./SPEED)

	GPIO.cleanup()
	print("End GPIO")

#gong()

#import sys
#sys.exit()

while True:
	resp = requests.get("https://services-uk.dev.babylontech.co.uk/kompass/v2/dev/deployments")

	data = resp.json()

	for service in data:
		service_name = service["metadata"]["name"]
		if service_name in SERVICE_VERSIONS:
			current_version = service["metadata"]["labels"]["app.kubernetes.io/version"]
			if SERVICE_VERSIONS[service_name] and \
				SERVICE_VERSIONS[service_name] != current_version:
#				print(f"GONG {service_name} {current_version}")
				gong()
			else:
				print('NO GONG {} {}'.format(service_name, current_version))

			SERVICE_VERSIONS[service_name] =  current_version
	sleep(INTERVAL)



