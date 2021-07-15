#!/usr/bin/env python3
#
#
import os
import json
import requests
import reddit
import sys
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

if "-d" in sys.argv:
    # Clear out any existing subs
    subs = red.get_my_subs()
    sub_str = ','.join(subs)
    red.unsubscribe_from_sub(sub_str)


if not os.file_exists("subs.txt"):
    print("Error: subs.txt doesn't exist")
    sys.exit(1)

# Read in the list of subs to sub to
fh = open("subs.txt","r")
subs = fh.readlines()

# The API accepts a comma seperated list, so collapse down
sub_line = ','.join(subs)
red.subscribe_to_sub(sub_line)
fh.close()

# Set prefs if the file exists
if os.file_exists("prefs.json"):
    fh = open("prefs.json", "r")
    prefs = json.loads(''.join(fh.readlines()))
    red.set_user_prefs(prefs)
