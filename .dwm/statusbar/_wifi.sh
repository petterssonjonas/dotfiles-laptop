#!/bin/bash

# Wifi SSID and strengh

STR="$(grep wlo1 /proc/net/wireless | awk '{print $4}' | sed 's/[^0-9]//g')"
STR=$((STR-30))
SSID="$(iw dev | grep ssid | awk '{print $2}')"

[ "$STR" -lt 35 ] && ICON=" "
[ "$STR" -ge 35 ] && ICON="說"
[ "$STR" -ge 55 ] && ICON="罹"

curl www.google.com &>/dev/null || ICON=" " 

[ -z $SSID ] && SSID="off" && ICON="ﲁ " 

echo " ${SSID} ${ICON}"
