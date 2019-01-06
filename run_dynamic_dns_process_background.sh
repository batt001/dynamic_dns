#!/bin/bash
nohup python dynamic_dns.py > /dev/null 2>&1 &
pid=$(ps aux | grep 'python dynamic.dns.py' | grep -v 'grep' | awk '{print $2}')
echo $pid
