import datetime, time

class TimeProcessing:
    def __init__(self, real_start_time, real_end_time):
        self.real_end_time = real_end_time
        self.real_start_time = real_start_time

    def time_difference_sec(self):
        self.estimation = time.mktime(self.real_end_time.timetuple()) - time.mktime(self.real_start_time.timetuple())
        if self.estimation < 0:
            self.estimation = 0
            print("time handling error, most likely you confused the start time and end time, please try again")
            return datetime.timedelta(self.estimation)
        elif self.estimation == 0:
            print("attention, your operationgo on 0 seconds")
            return datetime.timedelta(seconds=(self.estimation))
        else: return datetime.timedelta(seconds=(self.estimation))
