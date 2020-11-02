#!/bin/sh
# env_launcher.sh
# launches correct python scripts with directory management

cd /home/pi/env_info_code
sleep 5
python3 record_env.py >> logs/logs&
exit 0