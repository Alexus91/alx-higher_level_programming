#!/bin/bash
# Send a GET request to the URL with a specific header and display
curl -s -H "X-School-User-Id: 98" "$1"
