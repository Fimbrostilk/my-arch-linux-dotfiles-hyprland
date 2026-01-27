#!/bin/bash

brightness=$(brightnessctl -c backlight g)

if [ $brightness -lt 3750 ]
then
	echo "󰃞"
elif [ $brightness -lt 7500 ]
then
	echo "󰃟"
else
	echo "󰃠"
fi
