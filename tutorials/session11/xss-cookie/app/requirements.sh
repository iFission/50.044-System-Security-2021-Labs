sudo apt-get install libffi-dev
python3 -m pip install -r dev_requirements.txt --no-cache-dir
sudo python3 -m pip install markupsafe
sudo python3 setup.py develop
