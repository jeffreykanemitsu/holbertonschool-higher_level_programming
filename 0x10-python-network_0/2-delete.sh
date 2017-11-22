#!/bin/bash
# sends a DELETE request to URL and displays body of response
curl -s $1 -X DELETE -H $1
