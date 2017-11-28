#!/usr/bin/python3
'''
takes in a URL, sends a request to the URL and displays the
body of the response
'''
import requests
from sys import argv


if __name__ == "__main__":
    url = 'https://swapi.co/api/people/?search={}'.format(argv[1])
    req = dict(requests.get(url).json())
    print('Number of results: {}'.format(req.get('count')))
    for n in req.get('results'):
        print(n.get('name'))
