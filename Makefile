NAME=robo-gong
SERVICE_NAME=robo-gong
COMMIT_ID=$(shell git rev-parse HEAD)
SEMVER_VERSION=$(shell git describe --abbrev=0 --tags)

install:
	# Setup Venv
	#pip3 install virtualenv
	#python3 -m virtualenv --python=python3 venv
	# Install requirements
	#bash -c 'source venv/bin/activate && pip install -r requirements.txt'
	# Install Daemon
	#pip3 install supervisor
	sudo mkdir -p /etc/supervisor/conf.d/
	sudo bash -c "echo_supervisord_conf > /etc/supervisor/supervisord.conf"
	sudo cp supervisord.conf /etc/supervisor/conf.d/robo-gong.conf
	# Restart Daemon
	sudo supervisorctl reload
