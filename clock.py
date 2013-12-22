from apscheduler.scheduler import Scheduler

sched = Scheduler()

@sched.interval_schedule(minutes=3)
def timed_job():
    print 'This job is run every three seconds.'

@sched.cron_schedule(day_of_week='mon-sun', hour=23)
def scheduled_job():
    print 'This job is run every weekday at 5pm.'

sched.start()

while True:
    pass
