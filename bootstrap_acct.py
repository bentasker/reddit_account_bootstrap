#!/usr/bin/env python3
#
#
import requests
import reddit
import getpass


def get_info():
    ''' Get information used to authenticate with the API
    '''
    
    USER = input("Username: ")
    PASSW = getpass.getpass(prompt="Password: ")
    ID = input("API ID: ")
    SEC = input("API Secret: ")
    return USER, PASSW, ID, SEC

USER, PASSW, ID, SEC = get_info()
red = reddit.Reddit(USER, PASSW, ID, SEC)
red.request_path("/api/v1/me")
print()
print(red.subscribe_to_sub('/r/supportlol'))
print(red.unsubscribe_from_sub('/r/supportlol'))

# This means that we can now iterate over a list of subs and sub to them
subs = [] # TODO: Fetch these from an input file

for sub in subs:
    red.subscribe_to_sub("/r/{}".format(sub))
    