#!/bin/bash

pactl subscribe | grep --line-buffered "Event 'change' on sink" | while read -r line; do
    pkill -RTMIN+1 waybar
done
