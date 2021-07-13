#!/usr/bin/env python3
#
#


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
        print(a.json())


    def subscribe_to_sub(self, sub):
        ''' https://www.reddit.com/dev/api#POST_api_subscribe
        '''
        
        data = {"action" : "sub",
                "action_source": "o",
                "skip_initial_defaults": True,
                "sr_name" : sub
                    }
        res = requests.post('https://oauth.reddit.com/api/subscribe',
                                    data=data, headers=self.headers)
        
        print(res.json())


    def unsubscribe_from_sub(self, sub):
        ''' https://www.reddit.com/dev/api#POST_api_subscribe
        '''
        
        data = {"action" : "unsub",
                "action_source": "o",
                "sr_name" : sub
                    }
        res = requests.post('https://oauth.reddit.com/api/subscribe',
                                    data=data, headers=self.headers)
        
        print(res.json())
