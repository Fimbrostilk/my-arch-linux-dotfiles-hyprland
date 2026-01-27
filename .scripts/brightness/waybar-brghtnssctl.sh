#!/bin/bash

brightness=$(brightnessctl -c backlight g)

if [ $brightness -lt 3750 ]
then
	brightnessctl s 50% || true
	ddcutil setvcp 10 50 || true
elif [ $brightness -lt 7500 ]
then
	brightnessctl s 100% || true
	ddcutil setvcp 10 100 || true
else
	brightnessctl s 1% || true
	ddcutil setvcp 10 0 || true
fi
