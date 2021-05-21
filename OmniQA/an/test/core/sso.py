import requests


class SSOClient(object):
    def __init__(self, track_url, sso_url):
        self.track_url = track_url
        self.sso_url = sso_url
        self.session_id = None

    def login(self, username, password):
        # get new session ID from SSO (which uses MS SQL to store sessions)
        url = self.sso_url+'ssoapiexec'
        params = { 'verb': 'post', 'func': 'user/login/'+username }
        data = { 'p': password }
        try:
            resp = requests.post(url, params=params, json=data)
        except Exception as e:
            raise Exception("connection to '%s' failed: %s" % (url, e))
        resp.raise_for_status()
        try:
            json = resp.json()
        except Exception as e:
            raise Exception("invalid JSON response: %s" % e)
        # get new session ID from the JSON response
        self.session_id = json['sid']
        # store new session ID in the ADE session cache (which uses MySQL)
        url = self.track_url + 'session'

        params = { 'ANsid': self.session_id }
        try:
            resp = requests.get(url, params=params)
        except Exception as e:
            raise Exception("connection to '%s' failed: %s" % (url, e))
        resp.raise_for_status()
        # try:
        #     json = resp.json()
        # except Exception as e:
        #     raise Exception("invalid JSON response: %s" % e)

        return self.session_id
