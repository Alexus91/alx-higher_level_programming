#!/bin/bash
# Send a request to the URL and display only the status code
curl -so /dev/null -w "%{http_code}" "$1"
