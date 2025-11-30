#!/bin/bash
pactl set-source-mute @DEFAULT_SOURCE@ toggle
STATUS=$(pactl get-source-mute @DEFAULT_SOURCE@ | awk '{print $2}')
LED_FILE="/sys/class/leds/platform::micmute/brightness"
if [ "$STATUS" = "yes" ]; then
	brightnessctl --device='platform::micmute' set 1
else
	brightnessctl --device='platform::micmute' set 0
fi
