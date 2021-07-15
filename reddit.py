#!/usr/bin/env python3
#
# Library file to implement accessing reddit via API and performing a variety of actions
#
# Copyright (C) 2021 B Tasker
# Released under GNU GPL V3, see LICENSE
#

import json
import requests


class Reddit(object):

    def __init__(self, user, passw, API_id, API_sec):
        self.passw = passw
        self.user = user
        self.api_id = API_id
        self.api_sec = API_sec
        self.token = False

    def get_token(self):
        '''
        
        derived from https://towardsdatascience.com/how-to-use-the-reddit-api-in-python-5e05ddfd1e5c
        '''
        auth = requests.auth.HTTPBasicAuth(self.api_id, self.api_sec)
        data = {'grant_type': 'password',
                'username': self.user,
                'password': self.passw}

        self.headers = {'User-Agent': 'AcctBootstrap/0.1'}
                
        # send our request for an OAuth token
        res = requests.post('https://www.reddit.com/api/v1/access_token',
                            auth=auth, data=data, headers=self.headers)

        #print(res.json())
        TOKEN = res.json()['access_token']

        # add authorization to our headers dictionary
        self.headers = {**self.headers, **{'Authorization': f"bearer {TOKEN}"}}


    def request_path(self, path):
        if not self.token:
            self.get_token()
            
        # while the token is valid (~2 hours) we just add headers=headers to our requests
        a=requests.get('https://oauth.reddit.com{}'.format(path), headers=self.headers)

        return a.json()


    def subscribe_to_sub(self, sub):
        ''' https://www.reddit.com/dev/api#POST_api_subscribe
        '''
        
        if not self.token:
           self.get_token()

        data = {"action" : "sub",
                "action_source": "o",
                "skip_initial_defaults": True,
                "sr_name" : sub
                    }
        res = requests.post('https://oauth.reddit.com/api/subscribe',
                                    data=data, headers=self.headers)
        
        #print(res.json())


    def unsubscribe_from_sub(self, sub):
        ''' https://www.reddit.com/dev/api#POST_api_subscribe
        '''
        
        if not self.token:
           self.get_token()

        data = {"action" : "unsub",
                "action_source": "o",
                "sr_name" : sub
                    }
        res = requests.post('https://oauth.reddit.com/api/subscribe',
                                    data=data, headers=self.headers)
        
        #print(res.json())


    def get_my_subs(self):
       ''' Generate and return a list of the user's subs
       '''

       if not self.token:
           self.get_token()

       subs = []

       # Place the first request
       res = self.request_path('/subreddits/mine/subscriber?sr_detail=false')

       # Pull out the sub names
       for sub in res['data']['children']:
            subs.append(sub['data']['url'])

       # Data is paginated, so we may need to fetch more
       while True:
            if "after" in res['data'] and res['data']['after']:
                 # Request the next page
                 res = self.request_path('/subreddits/mine/subscriber?sr_detail=false&after={}'.format(res['data']['after']))
                 for sub in res['data']['children']:
                     subs.append(sub['data']['url'])
            else:
                 break

       subs.sort()
       return subs

    def get_user_prefs(self):
       ''' /api/v1/me/prefs
       '''
       res = self.request_path('/api/v1/me/prefs')
       return res


    def set_user_prefs(self, prefs):
       ''' https://old.reddit.com/dev/api#GET_api_v1_me_prefs
       '''

       if not self.token:
           self.get_token()

       prefs['json'] = {"FOO": "bar"}
       self.headers['Content-Type'] = "application/json"
       res = requests.patch('https://oauth.reddit.com/api/v1/me/prefs',
                               headers=self.headers,
                               data=json.dumps(prefs))
