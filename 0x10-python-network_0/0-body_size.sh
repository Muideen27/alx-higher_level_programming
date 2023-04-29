#!/bin/bash

# takes in a URL, sends a request to that URL, and 
# displays the size of the body of the response

# checking if any aurgument received
if [ $# -eq 0 ]; then
	  echo "Please provide a URL as an argument"
	    exit 1
fi

# variable url
url=$1
response=$(curl -sI $url)
content_length=$(echo "$response" | awk '/Content-Length/ {print $2}' | tr -d '\r')

if [ -z "$content_length" ]; then
	  echo "Unable to determine size of response body"
  else
	    echo "Size of response body: $content_length bytes"
fi
