#!/usr/bin/python3
'''
takes your Github credentials and uses Github API to display id
'''
import requests
from sys import argv


if __name__ == "__main__":
    user = argv[1]
    pw = argv[2]
    req = requests.get('https://api.github.com/user', auth=(user, pw))
    gid = dict(req.json())
    print(gid.get('id'))
