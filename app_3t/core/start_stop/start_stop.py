from app_3t.core.task_extension import *
import datetime
from core.task import *

from core.console_starter import *

class StartStop:
    def __init__(self, user_name, task_name, start_time, end_time):
        self.user_name = user_name
        self.task_name = task_name
        self.var = 'var'
        self.start_time = start_time
        self.end_time = end_time
        #self.estimation = self.end_time - self.start_time

    def time_pause_1(self):
        change_task(self.user_name, self.task_name, self.var)
        task_name.new_total_w_time()

def inlet (*args):
    pause = input("Input pause to make a pause ")
    for element in args:
        if pause != element:
            print(f"unknown command {pause}, please try again")
            return inlet (*args)
    else: return pause


def time_count (start_time, end_time):
    timeList = [str(start_time), str(end_time)]
    sum = datetime.timedelta()
    for i in timeList:
        (h, m, s) = i.split(':')
        d = datetime.timedelta(hours=int(h), minutes=int(m), seconds=float(s))
        sum += d
    return sum

