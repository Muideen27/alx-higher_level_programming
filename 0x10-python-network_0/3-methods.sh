#!/bin/bash
# A Bash script that takes in a URL and displays all HTTP methods the server will accept.
curl -s -i -X OPTIONS "$URL" | awk '/Allow/ {print $2}'
