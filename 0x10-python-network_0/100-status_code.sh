#!/bin/bash
# sends requests to URL passed as argument and displays only status code of response
curl -o -D -sL -w "%{http_code}" $1
