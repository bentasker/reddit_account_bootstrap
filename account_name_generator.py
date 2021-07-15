#!/usr/bin/env python3
#
# Generate reddit usernames based on a word list
#
# If not wordlist is provided, a default will be fetched with HTTP

import random
import sys


def pick_word(wordlist):
    ''' Use a wordlist to generate a username
    '''
    max = len(wordlist) - 1
    choice = random.randint(0,max)
    return wordlist[choice].strip("\n")


def gen_username(wordlist):
   ''' Pick 2 words to generate a username
   '''
   return "{}{}".format(
                             pick_word(wordlist),
                             pick_word(wordlist)
                            )


if len(sys.argv) > 1:
    # load the specified wordlist
    fh = open(sys.argv[1], "r")
    wordlist = fh.readlines()
    fh.close()
else:
    # Pull and load the default wordlist
    import requests
    r = requests.get("https://projects.bentasker.co.uk/static/wordlist.txt")
    wordlist = r.text.split("\n")

print(gen_username(wordlist))


