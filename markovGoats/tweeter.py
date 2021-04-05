from MarkovGoats import *
from twitterPublishing import *

import datetime
import time
from apscheduler.scheduler import Scheduler

# Start the scheduler
sched = Scheduler()
sched.daemonic = False
sched.start()

def getChainAndPublish():
    tweetContent = getChain()
    tweet(tweetContent)

# Schedules job_function to be run once each minute
sched.add_cron_job(job_function,  minute='0-59')
