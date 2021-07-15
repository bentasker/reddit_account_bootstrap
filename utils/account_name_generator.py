#!/usr/bin/env python3
#
# Generate reddit usernames based on a word list
#
# If no wordlist is provided, a default will be fetched with HTTP
#
# Copyright (C) 2021 B Tasker
# Released under GNU GPL V3, see LICENSE
#

import os
import random
import sys


options = {
    "manglechars" : "Random", # Should we replace some letters with numbers - values are True, False, Random
    "joinchar" : "Random", # Set to a single char, or Random
    "numwords" : 2, # how many words should we join
    "numsuggestions" : 5, # how many usernames should we suggest?
}


def pick_word(wordlist):
    ''' Pick a word from the wordlist
    '''
    max = len(wordlist) - 1
    choice = random.randint(0,max)
    return wordlist[choice].strip("\n")


def gen_username(wordlist, options):
   ''' Pick n words to generate a username
   '''

   # Pick the words
   individs = [ pick_word(wordlist) for i in range(options['numwords']) ]

   # What char are we using to join the words?
   join_char = get_join_char(options)

   # Join into a single string
   uname_str = join_char.join(individs)

   # Mangle chars
   uname = mangle(uname_str, options)

   # We have a username suggestion, return it
   return uname


def mangle(userstr, options):
    ''' Replace chars with numbers if mangle is enabled
    '''

    # Is mangling enabled?
    if options['manglechars'] == False:
        return userstr
    elif options['manglechars'] == "Random" and random.randint(0,1) == 1:
        # Random mode enabled and we've chosen not to
        return userstr

    # Otherwise, do some mangling
    chars = [
              ["e", 3],
              ["a", 4],
              ["i", 1],
              ["o", 0],
              ["b", 8],
              ["s", 5],
              ["t", 7]
             ]

    # How many chars do we screw with?
    attempts = random.randint(0, len(chars) - 1)
    for i in range(attempts):
        pos = random.randint(0, len(chars) - 1)
        ch = chars[pos][0]
        nm = chars[pos][1]
        userstr = userstr.replace(ch, str(nm))

    # Return the mangled string
    return userstr

def get_join_char(options):
    ''' Names are going to be joined, but what char should we use?
    '''

    # Had the user configured a specific joinchar?
    if type(options["joinchar"]) == str and len(options["joinchar"]) < 2:
         return options["joinchar"]

    # Otherwise, we pick one at random
    chars = ["-","","_"]
    pos = random.randint(0,len(chars) - 1)
    return chars[pos]



if len(sys.argv) > 1:
    # load the specified wordlist
    fh = open(sys.argv[1], "r")
    wordlist = fh.readlines()
    fh.close()
else:
   if not os.path.exists("wordlist.default.txt"):
      # Pull and load the default wordlist
      import requests
      r = requests.get("https://projects.bentasker.co.uk/static/wordlist.default.txt")
      wordlist = r.text.split("\n")

      # Save a copy of the file
      fh = open("wordlist.default.txt", "w")
      fh.write(r.text)
      fh.close()

   else:
      fh = open("wordlist.default.txt", "r")
      wordlist = fh.readlines()
      fh.close()


for i in range(options["numsuggestions"]):
    print(gen_username(wordlist, options))


