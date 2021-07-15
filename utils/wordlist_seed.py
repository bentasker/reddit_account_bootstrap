#!/bin/env python3
#
# Fetch a wordlist from github and process it to build a new wordlist
# of candidate words.
#
# Will write out to wordlist.txt
#
# Copyright (C) 2021 B Tasker
# Released under GNU GPL V3, see LICENSE
#


import requests

base_list = requests.get("https://github.com/dwyl/english-words/blob/master/words_alpha.txt?raw=true").text.split("\n")

''' iterate over an skip words that aren't suitable

    Reddit usernames must be >3 <20 chars long
    we'll be joining 2 words, so min length is 4.
    max length is 10 (20/2)
'''

words = []
for word in base_list:
    word = word.strip("\r")
    word_len = len(word)
    print("{}: {}".format(word, word_len))
    if word_len < 2 or word_len > 10:
        continue

    words.append(word)

fh = open("wordlist.txt", "w")
fh.write('\n'.join(words))
fh.close()
