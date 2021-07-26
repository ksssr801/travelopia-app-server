#!/bin/sh

INSTDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
echo $INSTDIR
SOURCEDIR="$(dirname "$INSTDIR")"
echo $SOURCEDIR

cd /opt
python3 -m venv TravelopiaEnv
source TravelopiaEnv/bin/activate
cd $INSTDIR
echo "Virtual environment (TravelopiaEnv) has been created."
echo ""
echo "Installing the Python dependencies"
pip3 install --upgrade pip
chmod +x requirements.sh
./requirements.sh
python3 manage.py makemigrations
python3 manage.py migrate
echo ""
echo "All Python dependencies has been installed"
chmod +x run_travelopia_server.sh

