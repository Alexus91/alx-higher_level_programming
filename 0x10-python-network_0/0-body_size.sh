#!/bin/bash

# Check if the user provided a URL as an argument
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Get the URL from the command line argument
url="$1"

# Use curl to send a request to the URL and save the response to a temporary file
response_file=$(mktemp)
curl -s -o "$response_file" "$url"

# Check if the request was successful
if [ $? -ne 0 ]; then
    echo "Failed to retrieve the URL: $url"
    exit 1
fi

# Get the size of the response body in bytes
size=$(wc -c < "$response_file")

# Display the size of the response body
echo "$size"

rm -f "$response_file"

