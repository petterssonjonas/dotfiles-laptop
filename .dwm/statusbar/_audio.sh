#!/bin/bash

# Volume state output
VOL="$(amixer get Master | awk 'NR==6 {print $5}' | sed 's/\[//;s/\]//;s/%//')"
MUTE="$(amixer get Master | awk 'NR==6 {print $6}' | sed 's/[^a-z]//g')"

[ $VOL 5 ] && VOLSTATE="ﱝ"
[ $VOL 30 ] && VOLSTATE="奄"
[ $VOL 30 ] && [ $VOL 70 ] && VOLSTATE="奔"
[ $VOL 70 ] && VOLSTATE="墳"

[ $MUTE == 'off' ] && VOLSTATE="婢"

echo " ${VOL}% ${VOLSTATE}  "
