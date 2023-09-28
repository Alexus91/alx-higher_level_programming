#!/bin/bash
# Send a JSON POST request with the contents of a JSON file and display
curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1"
