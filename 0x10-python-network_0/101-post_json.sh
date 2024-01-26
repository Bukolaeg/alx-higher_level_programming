#!/bin/bash
# Sends a JSON POST request to a URL and displays the body of the response
curl -s -X POST -H "Content-Type: application/json" --data @"$2" "$1"

