#!/usr/bin/python3
'''
takes in URL, sends requests to url, displays value of X-Request-Id
variable found in header of the response
'''
import urllib.request
import sys


if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        print(response.headers['X-Request-Id'])
