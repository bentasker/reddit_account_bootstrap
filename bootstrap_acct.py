#!/usr/bin/env python3
#
#
import json
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

#red.request_path("/api/v1/me")
#print()
#print(red.subscribe_to_sub('/r/supportlol'))
#print(red.unsubscribe_from_sub('/r/supportlol'))

fh = open("subs.txt","r")
subs = fh.readlines()

# The API accepts a comma seperated list, so collapse down
sub_line = ','.join(subs)
red.subscribe_to_sub(sub_line)
fh.close()

# TODO: Check if file exists
fh = open("prefs.json", "r")
prefs = json.loads(''.join(fh.readlines()))
red.set_user_prefs(prefs)
