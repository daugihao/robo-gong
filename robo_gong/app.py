from time import sleep

from robo_gong.swinger import strike, back_swing
#from robo_gong.kompass import detect_version_change


COOLDOWN = 60 # Seconds

WATCHED_SERVICES = [
	"simulation-framework"
]

def wait_to_gong():

	# Wait for version change
#	detect_version_change(WATCHED_SERVICES)

	# Hit that gong
	back_swing()
	strike()


if __name__ == "__main__":
	wait_to_gong()

	# Sleep so that we do not trigger multiple gongs soon after each other
	sleep(COOLDOWN)
	exit() # Supervisor will restart the python program
