#!/bin/bash
# Write a Bash script that takes in a URL as an argument, sends a GET request to the URL, and displays the body of the response
# A header variable X-School-User-Id must be sent with the value 98
# You have to use curl

# The URL should be specified as the first argument to the script
URL="$1"

# Use curl to send a GET request to the URL with the custom header and display the response body
curl -s -H "X-School-User-Id: 98" "$URL"

