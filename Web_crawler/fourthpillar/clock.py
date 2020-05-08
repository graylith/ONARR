from datetime import datetime
from scrapy import cmdline as cmd

from apscheduler.schedulers.blocking import BlockingScheduler


def job_function():
    cmd.execute("scrapy crawl ndtv".split())

sched = BlockingScheduler()

# Schedule job_function to be called every two hours
sched.add_job(job_function, 'interval', minutes=1)

sched.start()
