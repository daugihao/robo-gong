NAME=robo-gong
SERVICE_NAME=robo-gong
COMMIT_ID=$(shell git rev-parse HEAD)
SEMVER_VERSION=$(shell git describe --abbrev=0 --tags)

install:
	# Setup Venv
	pip install virtualenv
	virtualenv --python=python3 venv
	source venv/bin/activate
	# Install requirements
	pip install -r requirements.txt
	deactivate
	# Install Daemon
	sudo apt-get install supervisord
	cp supervisord.conf /etc/supervisor/conf.d/robo-gong.conf
	# Restart Daemon
	sudo supervisord restart
