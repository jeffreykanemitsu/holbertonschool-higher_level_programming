#!/bin/bash
# sends JSON POST to URL and displays body of the response
curl -s -X POST -H "Content-Type: application/json" -d @$2 $1
