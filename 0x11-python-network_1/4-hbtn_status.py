#!/usr/bin/python3
'''
fetches url
'''
import requests


if __name__ == "__main__":
    url = 'https://intranet.hbtn.io/status'
    req = requests.get(url).text
    print('Body response:')
    print('\t- type: {}'.format(type(req)))
    print('\t- content: {}'.format(req))
