from collections import defaultdict
import requests
from time import sleep

CHECK_INTERVAL = 5 # Seconds
KOMPASS_URLS = {
	"dev":"https://services-uk.dev.babylontech.co.uk/kompass/v2/dev/deployments"
}


def detect_version_change(services, env="dev"):
	"""
	Return only once a service version change has been detected.
	"""
	# Store map of last seen service versions
	service_versions= {service_name: None for service_name in services}
	service_versions = defaultdict()
	while True:
		print('Checking for version change in services {}'.format(service_versions))
		resp = requests.get(KOMPASS_URLS[env])
		data = resp.json()
		for service in data:
			service_name = service["metadata"]["name"]
			if service_name in service_versions or True:
				try:
					current_version = service["metadata"]["labels"].get("app.kubernetes.io/version","UNKNOWN")
					if service_versions.get(service_name) and \
						service_versions.get(service_name) != current_version:
						print("Version Change Detected {} {}".format(service_name,current_version))
						return True
				except KeyError:
					pass
				service_versions[service_name] =  current_version
		sleep(CHECK_INTERVAL)
