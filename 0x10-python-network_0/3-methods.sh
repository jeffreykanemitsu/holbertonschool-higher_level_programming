#!/bin/bash
# takes in a URL and displays all HTTP methods server will accept
curl -sI $1 | grep Allow | cut -c 8-
