#!/bin/bash

# Display date

echo "$(date +%x)   "

case $BLOCK_BUTTON in
    1) notify-send "$(cal)" ;;
    2) notify-send "AOSDKASD" ;;
esac
