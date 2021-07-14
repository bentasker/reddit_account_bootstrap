Reddit Account Bootstrap
===========================


It's common wisdom that you should periodically burn your reddit handle, but once you've got your subs set up just right it's a pain setting a new account up.

This set of scripts is designed to aid in that - it allows you to dump out a list of subs, and to automatically configure a new user to subscribe to those subs


### Pre-Requisites

You'll need to have obtained an API key from reddit for any account that you want to use this against. The steps to do so are quite simple

1. Go to https://www.reddit.com/prefs/apps/
1. Click `Create another app`
1. Provide a name
1. Choose script
1. Enter a URL (any URL) into `redirect uri`
1. You'll then be provided with and ID (3rd line down) and a secret, make a note of both


### Fetching Sub-Reddits

To write out a list of subreddits, run

    ./fetch_sub_listing.py

You'll be prompted to provide login details and API token info.

Once complete, a list of subs will be written out to the file `subs.txt`

#### File format

`subs.txt` is simply a list of subreddits, with one sub per line:

    ben@optimus:~/Documents/src.old/reddit_account_bootstrap$ head -n3 subs.txt 
    /r/Art/
    /r/AskNetsec/
    /r/AskReddit/

You can trivially add or remove lines.


### Bootstrapping an account

To configure an account, run

    ./bootstrap_account.py

You'll be prompted to provie login details and API token info.

The file `subs.txt` will be read, and your user will join each subreddit listed there

