import requests_mock
try:
    import RPi.GPIO
except (RuntimeError, ModuleNotFoundError):
    import fake_rpigpio.utils
    fake_rpigpio.utils.install()

from robo_gong import app
from robo_gong.kompass import KOMPASS_URLS


CALL_COUNT=0

def get_mocked_response(request, context):
	global CALL_COUNT
	CALL_COUNT+=1 
	version = "VERSION_1" if CALL_COUNT < 3 else "VERSION_2"
	return [
	{
		"metadata":{
			"name":"simulation-framework",
			"labels":{
				"app.kubernetes.io/version": version
			}
		}
	}
	]


def test_e2e():
	with requests_mock.mock() as m:
		m.get(KOMPASS_URLS["dev"], json=get_mocked_response)
		app.wait_to_gong()
