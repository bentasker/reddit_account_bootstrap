Reddit Account Bootstrap
===========================


It's common wisdom that you should periodically burn your reddit handle, but once you've got your subs set up just right it's a pain setting a new account up.

This set of scripts is designed to aid in that - it allows you to dump out a list of subs, and to automatically configure a new user to subscribe to those subs

----

### Pre-Requisites

You'll need to have obtained an API key from reddit for any account that you want to use this against. The steps to do so are quite simple

1. Go to https://www.reddit.com/prefs/apps/
1. Click `Create another app`
1. Provide a name
1. Choose script
1. Enter a URL (any URL) into `redirect uri`
1. You'll then be provided with and ID (3rd line down) and a secret, make a note of both

----

### Fetching Sub-Reddits

To write out a list of subreddits, run

    ./fetch_sub_listing.py

You'll be prompted to provide login details and API token info.

Once complete, a list of subs will be written out to the file `subs.txt`. Your user's preferences will also be written to `prefs.json`

----

#### File format

`subs.txt` is simply a list of subreddits, with one sub per line:

    ben@optimus:~/Documents/src.old/reddit_account_bootstrap$ head -n3 subs.txt 
    /r/Art/
    /r/AskNetsec/
    /r/AskReddit/

You can trivially add or remove lines.

`prefs.json` is a JSON file, with the format as defined [here](https://old.reddit.com/dev/api#GET_api_v1_me_prefs)

----

### Bootstrapping an account

To configure an account, run

    ./bootstrap_account.py

You'll be prompted to provide login details and API token info.

The file `subs.txt` will be read, and your user will join each subreddit listed there

#### Options

    -d       Clear any existing subs before joining listed subs


----

## Utils

### `account_name_generator.py`

Generates user account name suggestions based on an input wordlist. If no wordlist is specified, then a default list is pulled from my site

    ./utils/account_name_generator.py [path to wordlist]

Will generate suggestions by merging 2 words from the wordlist, and mangling some chars.

The head of the script contains some basic configuration options

    options = {
        "manglechars" : "Random", # Should we replace some letters with numbers - values are True, False, Random
        "joinchar" : "Random", # Set to a single char, or Random
        "numwords" : 2, # how many words should we join
        "numsuggestions" : 5, # how many usernames should we suggest?
    }

The script will output a set of suggestions:

    $ ./utils/account_name_generator.py 
    ruching-outbr4g
    reeshie-entities
    cobby_b3cry
    1ngene-5qu4m4ted
    deluder_syc0narian


### `wordlist_seed.py`

Used to build the basis of a wordlist.

Fetches a wordlist from github and then strips words that wouldn't be suitable for use (due to length etc).

Will save the modified list out to `wordlist.txt` in the current working directory - you can then manually add/remove words as needed

    ./utils/wordlist_seed.py


