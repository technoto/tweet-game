#!/usr/bin/python
from urllib2 import urlopen, HTTPError, build_opener
import time, json

o = build_opener()
o.addheaders = [('User-agent', 'Python bot by ooowo')]
API_BASE = 'http://api.reddit.com'
def parse(url):
    try:
        r = urlopen(url).read().decode()
        data = json.loads(r)
        return data

    except HTTPError:
        time.sleep(1)
        parse(url)

def worstPost():
    url = API_BASE + '/r/all/top.json?t=all&before=t3_14ymyf&t=day&limit=1'
    data = parse(url)
    title = data['data']['children'][0]['data']['title']
    return title
    
def bestPost():
    pass

class FrontPage(object):
    def __init__(self, sort='hot', limit=25):
        self.sort = sort
        self.limit = limit
        self.endpoint = API_BASE + '/%s.json?limit=%d' % (self.sort, self.limit)

    def getPosts(self):
        '''returns a list of posts'''
        data = parse(self.endpoint)
        while data == None:
            data = parse(self.endpoint)
        posts = [post['data'] for post in data['data']['children']]
        return posts
