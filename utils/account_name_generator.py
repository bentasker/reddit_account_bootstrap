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


def gen_username(wordlist, options):
   ''' Pick 2 words to generate a username
   '''

   individs = [ pick_word(wordlist) for i in range(options['numwords']) ]

   join_char = get_join_char(options)

   uname_str = join_char.join(individs)
   uname = mangle(uname_str, options)

   return uname


def mangle(userstr, options):
    ''' Replace chars with numbers if mangle is enabled
    '''
    if options['manglechars'] == False:
        return userstr
    elif options['manglechars'] == "Random" and random.randint(0,1) == 1:
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

    return userstr

def get_join_char(options):
    ''' Names are going to be joined, but what char should we use?
    '''

    if len(options["joinchar"]) == 1:
         return options["joinchar"]

    # Otherwise, we pick one at random
    chars = ["-","","_"]
    pos = random.randint(0,len(chars) - 1)
    return chars[pos]



options = {
    "manglechars" : "Random", # Should we replace some letters with numbers - values are True, False, Random
    "joinchar" : "Random", # Set to a single char, or Random
    "numwords" : 2 # how many words should we join
}


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

print(gen_username(wordlist, options))


