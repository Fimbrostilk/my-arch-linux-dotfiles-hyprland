#!/bin/bash

# Obtener el nombre del sink predeterminado
sink=$(pactl info | grep 'Default Sink' | cut -d ':' -f2 | xargs)

# Obtener volumen en dB de ese sink
output=$(pactl list sinks | awk '/Name: '"$sink"'/ { found = 1 }
found == 1 && /Volume:/ { print $7; found = 0 }')

echo $output'dB'
