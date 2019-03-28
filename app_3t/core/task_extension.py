import os
from app_3t.core.data_storage import *
from app_3t.core.task import *
from app_3t.core.task_printer import *


def change_task(user_name, task_name, attr_change, new_value = None):
    default_old_message = 'old value was {}'
    default_new_message = 'please enter new {}'

    attr_mapping = {
        'name': ('name', default_old_message, default_new_message),
        'description': ('description', default_old_message, default_new_message),
        'starting_time': ('real_start_dt', default_old_message, default_new_message),
        'end_time': ('real_end_date', default_old_message, default_new_message),
        'price_per_hour': ('price_per_hour', default_old_message, default_new_message),
        'price_task': ('price_task', default_old_message, default_new_message),
        'status': ('status', default_old_message, default_new_message),
        'var' : ('var', default_old_message, default_new_message),
    }

    attr_change = attr_change.lower()
    attr_config = attr_mapping.get(attr_change)
    if not attr_config:
        print(f'invalid attribute {attr_change}')
        return

    task = (os.path.join(os.getcwd(), "for_save", task_name))
    with open(task, 'rb') as task:
         task = pickle.load(task)
         if task.user_name != user_name:
            exit(print(f"No task {task_name} for user {user_name}"))

    attr_name, old_message, new_message = attr_config
    old_value = getattr(task, attr_name)
    print(old_message.format(old_value))

    if new_value is None:
        new_value = input(new_message.format(attr_name))
    setattr(task, attr_name, new_value)
    saver(task, task.name)
    print('information successfully stored ')
    return None


def task_status(user_name, task_name):
    task = (os.path.join(os.getcwd(), "for_save", task_name))
    with open(task, 'rb') as task:
        task = pickle.load(task)
        if task.user_name == user_name:
            task_printer(task)
    return None
