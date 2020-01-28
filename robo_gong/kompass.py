from collections import defaultdict
import requests
from time import sleep
from datetime import datetime

CHECK_INTERVAL = 5 # Seconds
KOMPASS_URLS = {
	"dev":"https://services-uk.dev.babylontech.co.uk/kompass/v2/dev/deployments",
	"staging":"https://services-uk.staging.babylontech.co.uk/kompass/v2/staging/deployments",
	"preprod":"https://services-uk.preprod.babylontech.co.uk/kompass/v2/preprod/deployments",
	"prod": "https://services.babylonpartners.com/kompass/v2/prod/deployments"
}


def detect_version_change(services, envs=["dev"]):
	"""
	Return only once a service version change has been detected.
	"""
	# Store map of last seen service versions
	service_versions={env: {service_name: None for service_name in services} for env in envs}
	while True:
		print(datetime.now())	
		print('Checking for version change in services {}'.format(service_versions))
		for env in envs:
			resp = requests.get(KOMPASS_URLS[env])
			data = resp.json()
			for service in data:
				service_name = service["metadata"]["name"]
				if service_name in service_versions[env]:
					try:
						current_version = service["metadata"]["labels"].get("app.kubernetes.io/version","UNKNOWN")
						is_changed = service_versions[env].get(service_name) and \
							service_versions[env].get(service_name) != current_version
						if is_changed:
							print("Version Change Detected {} {}".format(service_name,current_version))
							return True
					except KeyError:
						pass
					service_versions[env][service_name] =  current_version
		sleep(CHECK_INTERVAL)
