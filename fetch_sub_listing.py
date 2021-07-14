#!/usr/bin/env python3
#
# Fetch a list of subs that a user is currently subscribed to
import json
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
my_subs = red.get_my_subs()

# Write out to the subs file
fh = open("subs.txt","w")
fh.write('\n'.join(my_subs))
fh.close()

prefs = red.get_user_prefs()
fh = open("prefs.json","w")
fh.write(json.dumps(prefs))
fh.close()
