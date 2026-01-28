#!/bin/bash

get_title_cmd="sh -c 'hyprctl -j activewindow | jq -r \".title\"'"

zscroll -l 40 \
    --delay 0.3 \
    --match-command "${get_title_cmd}" \
    --update-check true "${get_title_cmd}" &

wait
