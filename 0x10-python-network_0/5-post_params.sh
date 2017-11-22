#!/bin/bash
# takes in URL, sends POST request to URL, displays body of response
curl -s $1 -X POST -d "email=hr@holbertonschool.com&subject=I%20will%20always%20be%20here%20for%20PLD"
