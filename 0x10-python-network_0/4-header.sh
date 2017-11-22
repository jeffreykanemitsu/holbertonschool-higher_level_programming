#!/bin/bash
# takes in URL as argument, sends GET request, displays body of response
curl -s $1 -X GET -H 'X-HolbertonSchool-User-Id: 98'
