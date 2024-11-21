#!/bin/bash

# This script is called in HGCTPGValidation/scripts/produceData_multiconfiguration.py immediately after running cmsDriver.py
# It checks periodically the rss memory of the cmsRun process, if the memory becomes greater than a given limit value, the cmsRun process is killed
# Usage: 
# get_rss_memory.sh $! interval limit
# 1rst argument: "$!" is the PID of python produceData_multiconfiguration.py process
# 2nd argument: interval in seconds
# 3th argument: memory limit

DEBUG=1

# Check if the PID of the last process is provided
if [ -z "$1" ]; then
    echo "ERROR Usage: $0 PID INTERVAL RSS_LIMIT" 1>&2 &&
    exit 1
fi

# Check if the Interval (in s) is provided
if [ -z "$2" ]; then
    echo "ERROR Usage: $0 PID INTERVAL RSS_LIMIT" 1>&2 &&
    exit 1
fi

# Check if the limit RSS is provided
if [ -z "$3" ]; then
    echo "ERROR Usage: $0 PID INTERVAL RSS_LIMIT" 1>&2 &&
    exit 1
fi

# Get the PID of the process
INTERVAL=$2
RSS_limit=$3

echo "STARTS get_rss_memory"

# Waiting for the process cmsRun to be run
# Max waiting time = 120s
i=0
limit_time=120
while true; do
    
    PID=$(ps -eo pid,user,comm | grep cmsRun | grep jenkins | awk '{print $1}')
    
    if [ -z "$PID" ] && [ $i -lt $limit_time ] ; then
       sleep 10
       echo "Waiting for the process cmsRun to be run."
       ((i++))
    elif [ $i -eq $limit_time ] ; then
        echo "WARNING: The PID for the process cmsRun has not been found." 1>&2 &&
        break;
    else
        p_all=$(ps -eo pid,user,comm | grep cmsRun | grep jenkins | awk '{print}')
        echo "=== > Information about the process (PID user name_process): " $p_all
        echo "PID=" $PID
        break;
    fi
done
 
while true; do
    
    if [ ! -e /proc/$PID/status ] ; then
        echo "Process $PID already finished!"
        break;
    else
        # Get the RSS (Resident Set Size) memory usage
        RSS=$(grep -i vmrss /proc/$PID/status | awk '{print $2}')
        if [ "$DEBUG" = "1" ] ; then
            echo "Free memory (RSS) for process PID=$PID: $(( ${RSS} / 1000 )) MB"
        fi
        
        if [ "${RSS}" -gt "${RSS_limit}" ]; then
            echo "ERROR: RSS memory $(( ${RSS} / 1000 )) MB > RSS limit $(( ${RSS_limit} / 1000 )) MB"  1>&2 &&
            kill -9 $PID &&
            exit 1;
        fi  
    fi    
    sleep $INTERVAL
done
