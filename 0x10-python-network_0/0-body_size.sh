#!/usr/bin/env bash
# takes in a URL, sends a request to URL, display size of body of response
curl -sI $1 | grep Content-Length | awk '{print $2}'
