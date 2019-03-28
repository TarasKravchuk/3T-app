from app_3t.utils.class_helpers import *
import datetime
from app_3t.core.currency.currency import *
from app_3t.core.data_storage import *
from app_3t.core.currency.price_hour import *

class Task:
    """Класс описывающий задание пользователя, в данной версии класс содержит следующие атрибуты:
    - имя
    - описание
    - время начала задания
    - время окончания задания
    - разница времени между окончанием и началом выполнения
    - oценка рабочего времени в EUR, UAH и USD по курсу НБУ
    - текущий статус (finished / on_work)
    и следующие методы:
    - расчет времени выполнения задания
    - расчет стоимости задания  в EUR, UAH и USD по курсу НБУ, в случае если задана цена за час
    - расчет стоимости часа работы в EUR, UAH и USD по курсу НБУ, в случае если задана полная цена задания
    ВАЖНО в случае если пользователь самостоятельно вводит время начала выполнения и/или время завершения это вводиться
    СТРОГО в формате год месяц день час минуты. В противном случае программа не примет значение.
    """
    def __init__(self, user_name, name, description, real_start_dt, plan_end_dt, estimation, price_task, price_per_hour,
                        status, currency, _uah, _usd, _eur):
        self.user_name = user_name
        self.name = name
        self.description = description
        self.real_start_dt = real_start_dt
        self.plan_end_dt = plan_end_dt
        self.price_task = price_task
        self.price_hour = price_per_hour
        self.estimation = estimation
        self.price_per_hour = price_per_hour
        self.price_full_task = price_task
        Task.money_counter(self, self.estimation, price_task, price_per_hour)
        self.status = status
        self.currency = currency
        self.uah = _uah
        self.usd = _usd
        self.eur = _eur
        self.var = datetime.time(hour = 0, minute = 0, second=0)
        self.total_w_time = datetime.time(hour=0, minute=0, second=0)

    def new_total_w_time (self):
        timeList = [str(self.total_w_time), str(self.var)]
        sum = datetime.timedelta()
        for i in timeList:
            (h, m, s) = i.split(':')
            d = datetime.timedelta(hours=int(h), minutes=int(m), seconds=float(s))
            sum += d
        self.total_w_time = str(sum)
        return self.total_w_time


    @staticmethod
    def time_counter(plan_end_dt, real_start_dt):
        datetimeFormat = '%Y%m%d%H%M'
        estimation = datetime.datetime.strptime(plan_end_dt, datetimeFormat) - datetime.datetime.strptime(real_start_dt, datetimeFormat)
        return estimation

    @staticmethod
    def money_counter (self, estimation, price_task, price_hour):
        if price_hour is None:
            self.price_per_hour = round((float(price_task)/float(estimation.seconds)/(60*60)), 6)
            return self.price_per_hour
        elif price_task is None:
            self.price_full_task = round((float(estimation.seconds)/(60*60)*float(price_hour)), 6)
            return self.price_full_task

    @staticmethod
    def currency_counter(currency, var):
        if currency.upper() == "UAH":
            return uah(var)
        elif currency.upper() == "EUR":
            return eur(var)
        elif currency.upper() == "USD":
            return usd(var)

    @staticmethod
    def new_task(user_name):
        name = input("Input your Task name ")
        description = input("Input the description of your Task ")
        status = input(
            "Input status of the task, only 2 values ​​are accepted - input finished in case task are finised\n"
            "Input in_work in the process of implementation ")
        if status.lower() == "finished" or status.lower() == "finish":
            status = 'finished'
        elif status.lower() == "in_work" or status.lower() == 'on_work':
            status = 'on work'
        else:
            exit(print("Invalid status\nOlease try again"))
            return  Task.new_task(user_name)
        print("Input start date")
        real_start_dt = date_input()
        print("Input ending date")
        plan_end_dt = date_input()
        estimation = Task.time_counter(plan_end_dt, real_start_dt)
        h = hour_()
        if h[0] == '0' or h[0] == 'hour':
            price_per_hour = float(h[1])
            currency = h[2].upper()
            price_task = None
            rated = Task.currency_counter(currency, price_per_hour)
            _uah = rated[0]
            _eur = rated[1]
            _usd = rated[2]
            task = Task(user_name, name, description, real_start_dt, plan_end_dt, estimation, price_task, price_per_hour,
                        status, currency, _uah, _usd, _eur)
            saver(task, name)

        elif h[0] == '1' or h[0] == 'full':
            price_task = h[1]
            currency = h[2]
            price_per_hour = None
            rated = Task.currency_counter(currency, price_task)
            _uah = rated[0]
            _eur = rated[1]
            _usd = rated[2]
            task = Task(user_name, name, description, real_start_dt, plan_end_dt, estimation, price_task, price_per_hour,
                status,  currency, _uah, _usd, _eur)
            saver(task, name)
