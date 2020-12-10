#!/bin/bash

# Battery stuff

CAP="$(cat /sys/class/power_supply/BAT0/capacity)"
STATUS="$(cat /sys/class/power_supply/BAT0/status)"


if [ "$STATUS" = "Discharging" ]; then
    if [ "$CAP" -ge 90 ]; then
        ICON=""; 
    elif [ "$CAP" -lt 90 ]; then
        ICON=""; 
    elif [ "$CAP" -lt 80 ]; then
        ICON=""; 
    elif [ "$CAP" -lt 70 ]; then
        ICON=""; 
    elif [ "$CAP" -lt 60 ]; then
        ICON=""; 
    elif [ "$CAP" -lt 50 ]; then
        ICON=""; 
    elif [ "$CAP" -lt 40 ]; then
        ICON=""; 
    elif [ "$CAP" -lt 30 ]; then
        ICON=""; 
    elif [ "$CAP" -lt 20 ]; then
        ICON=""; 
    else
        ICON="";
    fi
elif [ "$STATUS" = "Not charging"  ]; then
    ICON=""

elif [ "$STATUS" = "Charging" ]; then
    ICON=""
fi

echo " ${CAP}% ${ICON} "
