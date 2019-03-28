#!usr/bin/env python3.6
# -*- coding: utf-8 -*-

import sys
import os
import datetime
from app_3t.core.occurrence import *
from app_3t.core.task import *
from app_3t.core.data_storage import *
from app_3t.core.task_printer import *
from app_3t.core.statistic import *
from app_3t.core.countdown import *
from app_3t.core.password import *
from app_3t.users.usual_user import *
from app_3t.users.admin_user import *
from app_3t.core.task_extension import *
from app_3t.core.start_stop.start_stop import *

if __name__ == '__main__':
    Admin_User.existence_admin()

    first_arg = sys.argv[1]
    print(first_arg)
    if first_arg == "new_user".lower():
        name_user = input("Input name of new user ")
        password = password_security()
        user = Usual_User(name_user, password)
        saver(user, name_user)

    user_name = occurrence()

    if first_arg.lower() == "new_task":
        Task.new_task(user_name)

    elif first_arg.lower() == "start_time":
        task_name = input("Input task name, you will work ")
        task = (os.path.join(os.getcwd(), "for_save", task_name))
        with open(task, 'rb') as task:
            task = pickle.load(task)
            if task.user_name != user_name:
                exit(print(f"No task {task_name} for user {user_name}"))
        start_time = datetime.datetime.now().time()
        print("Please input pause to make pause ")
        pause = inlet("pause")
        if pause.lower() == 'pause':
            end_time = datetime.datetime.now().time()
            change_task(user_name, task_name, 'var', time_count(start_time, end_time ))
            task.new_total_w_time()
            saver(task, task.name)

    elif first_arg.lower() == "change_task":
        task_name = input('Input na   me of the task you want to change')
        attr_change = input("Input name of attribute to changed ")
        task_name = task_name.lower()
        change_task(user_name, task_name, attr_change)

    elif first_arg == "task_status":
        task_name = input("input name of your task")
        task_status(user_name, task_name)

    elif first_arg.lower() == "countdown":
        print("stopwatch mode\ninput start to start the countdown\ninput stop to stop the countdown")
        start_time = input("input start time ")
        if start_time == "start":
            start_time = datetime.datetime.now()
            start_time = datetime.datetime.strftime(start_time, datetimeFormat)
            print(f"starting time == {start_time}")
        stop_time = input("input stop time ")

        if stop_time == "stop":
            stop_time = datetime.datetime.now()
            stop_time = datetime.datetime.strftime(stop_time, datetimeFormat)
            print(f"stoping time  == {stop_time}")
            countdown().countdown(start_time, stop_time)

    elif first_arg == "statistic":
        statistic_starter(user_name)
