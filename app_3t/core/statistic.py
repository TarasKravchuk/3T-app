import pickle
from app_3t.core.task import *
from app_3t.core.task_printer import *
import os
import os.path
path = os.path.join(os.getcwd(), 'for_save')
on_work_tasks = []
finished_tasks = []

def statistic_starter(user_name):
    path = os.path.join(os.getcwd(), 'for_save')
    on_work_tasks = []
    finished_tasks = []
    try:
        for file in os.listdir(path):
            with open(os.path.join(path, file), 'rb') as file:
                task = pickle.load(file)
    except pickle.UnpicklingError:
        print(f"No tasks for user {user_name}")
    else:
        if isinstance(task, Task):
            if task.name_user == user_name or task.name_user == 'admin_user':
                if task.status == 'on work':
                    on_work_tasks.append(task)
                elif task.status == 'finished':
                    finished_tasks.append(task)
                else:exit(print('Invalid task status!'))

    number_on_work_tasks = len(on_work_tasks)
    number_finished_tasks = len(finished_tasks)
    total_tasks = number_finished_tasks + number_on_work_tasks

    print(f'Totaly you have {total_tasks} task\n'
          f'{number_on_work_tasks} of it are on work:')
    for task in on_work_tasks:
        task_printer(task)
        # if task.price_task is None:
        #     print(
        #         f"user name == {user_name}\n name of your task ==  {task.name}\ndescription == {task.description} \nstart time == {task.real_start_dt}\nending time == "
        #         f"{task.plan_end_dt}\nestimation == {task.estimation}\nyour salary per full task == {task.price_full_task}\nstatus of {task.name} == {task.status}")
        # elif task.price_hour is None:
        #     print(
        #         f"user name == {user_name}\nname of your task ==  {task.name}\ndescription == {task.description} \nstart time == {task.real_start_dt}\nending time == "
        #         f"{task.plan_end_dt}\nestimation == {task.estimation}\nyour salary per hour == {task.price_per_hour}\nyour salary per minute == {task.price_min}"
        #         f"\nstatus of {task.name} == {task.status}")

    print(f'Totaly you have {total_tasks}\n'
          f'{number_finished_tasks} of it are finished:\n')

    for task in finished_tasks:
        task_printer(task)
    #     if task.price_task is None:
    #         print(f"name of your task ==  {task.name}\ndescription == {task.description} \nstart time == {task.real_start_dt}\nending time == "
    #           f"{task.plan_end_dt}\nestimation == {task.estimation}\nyour salary per full task == {task.price_full_task}\nstatus of {task.name} == {task.status}")
    #     elif task.price_hour is None:
    #         print(f"name of your task ==  {task.name}\ndescription == {task.description} \nstart time == {task.real_start_dt}\nending time == "
    #             f"{task.plan_end_dt}\nestimation == {task.estimation}\nyour salary per hour == {task.price_per_hour}\nyour salary per minute == {task.price_min}"
    #               f"\nstatus of {task.name} == {task.status}")
