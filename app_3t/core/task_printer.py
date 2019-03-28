def task_printer(task):
    if task.price_task is None:
        print(
            f"user name(author name) == {task.user_name}\n"
            f"name of your task ==  {task.name}\ndescription == {task.description} \nstart time == {task.real_start_dt}\nending time == "
            f"{task.plan_end_dt}\nestimation == {task.estimation}\nyour salary per full task in UAH == {task.uah}\n"
            f"your salary per full task in EUR == {task.eur}\nyour salary per full task in USD == {task.usd}\n"
            f"real spent time == {task.total_w_time}\n status of {task.name} == {task.status}")
    elif task.price_hour is None:
        print(
            f"user name == {task.user_name}\n"
            f"name of your task ==  {task.name}\ndescription == {task.description} \nstart time == {task.real_start_dt}\nending time == "
            f"{task.plan_end_dt}\nestimation == {task.estimation}\nyour salary per hour in UAH == {task.uah}\n"
            f"your salary per hour in USD == {task.usd}\n"
            f"your salary per hour in EUR == {task.eur}\nreal spent time == {task.total_w_time}\n"
            f"status of {task.name} == {task.status}")
    else:
        print("PROBLEM IN task_printer.py ")
