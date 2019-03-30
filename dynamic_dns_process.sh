#!/bin/bash

# Check wether the required python 3 package is installed
python3 --version > /dev/null 2>&1
return_code=$?
if [[ $return_code -ne 0 ]]
then
        echo 'Python 3 not installed, exiting...'
        exit 1
fi

if [[ "$1" = "start" ]]; then
  pid=$(ps aux | grep 'python3 dynamic.dns.py' | grep -v 'grep' | awk '{print $2}')
  if [[ "$pid" != "" ]]; then
    echo "Dynamic DNS process is already running..."
  else
    nohup python3 dynamic_dns.py > /dev/null 2>&1 &
    pid=$(ps aux | grep 'python3 dynamic.dns.py' | grep -v 'grep' | awk '{print $2}')
    echo "Dynamic DNS process started with PID=$pid"
  fi
elif [[ "$1" = "stop" ]]; then
  kill $(ps aux | grep 'python3 dynamic.dns.py' | grep -v 'grep' | awk '{print $2}')
  echo "Dynamic DNS process killed..."
elif [[ "$1" = "status" ]]; then
  pid=$(ps aux | grep 'python3 dynamic.dns.py' | grep -v 'grep' | awk '{print $2}')
  if [[ "$pid" = "" ]]; then
    echo "Dynamic DNS process is not running..."
  else
    echo "Dynamic DNS process is running with PID=$pid"
  fi
else
  echo "Wrong argument!"
fi
