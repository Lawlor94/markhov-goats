import tweepy

# Consumer keys and access tokens, used for OAuth
CONSUMER_KEY = 'QgiSO3BejOvVTNjkNB9yuMXeA'
CONSUMER_SECRET = 'o4cInKcfAy8nMbBMhtXleIKXJEpgj9qropc85DMGT9rf2IpFVt'
ACCESS_KEY = '1379176481939685380-TeLtyeM6vvmFvHxu7D2a5rPtVbpss9'
ACCESS_SECRET = '5cX7yyvGPSs1uYHxp8QrbzjXZxhLfMtIzzgeZ0P2lJo7p'

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

# Creation of the actual interface, using authentication
api = tweepy.API(auth)

# Sample method, used to update a status, you can write message whatever you want to post in twitter

def tweet(tweetContent):
    api.update_status(tweetContent)