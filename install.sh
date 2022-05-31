#!/bin/bash

cp shutdown-button.py /bin/shutdown-button.py

echo "sudo python3 /bin/shutdown-button.py &" > /etc/rc.local
sudo python3 /bin/shutdown-button.py &

echo "Script installed and added to rc.local to start the script on bootup"
