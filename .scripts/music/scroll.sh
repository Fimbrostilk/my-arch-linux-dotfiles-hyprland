#!/bin/bash
zscroll -l 30 \
        --delay 0.3 \
        --match-command "playerctl metadata --format '{{title}}'" \
        --update-check true "playerctl metadata --format '{{title}} - {{artist}}'" &
wait
