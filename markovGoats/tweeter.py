from MarkovGoats import *
from twitterPublishing import *

def getChainAndPublish():
    tweetContent = getChain()
    tweet(tweetContent)

getChainAndPublish()
