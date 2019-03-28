import datetime
datetimeFormat = '%Y %m %d %H %M %S %f'

class countdown:
    """Funcotor stopwatch"""

    def __call__(self, *args):
        self.start_time = None
        self.stop_time = None

    def countdown (self, start_time, stop_time):
        result = datetime.datetime.strptime(stop_time, datetimeFormat) - datetime.datetime.strptime(start_time, datetimeFormat)
        return print(f"time difference == {result}")
