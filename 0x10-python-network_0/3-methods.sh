#!/bin/bash
# Send an OPTIONS request to the URL and display
curl -sI -X OPTIONS "$1" | grep -i "allow" | awk -F ': ' '{print $2}'
