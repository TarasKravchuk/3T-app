import pickle
import os
import os.path

class Serialization:
    def __call__(self, task_status, task_id):
        file_name = str(task_id)
        dir_name = "for_save"
        if not os.path.exists(os.path.join(os.path.abspath(os.curdir), dir_name)):
            os.makedirs(os.path.join(os.path.abspath(os.curdir), dir_name))
            full_path = os.path.join(os.path.abspath(os.curdir), dir_name)
        else:
            full_path = os.path.join(os.path.abspath(os.curdir), dir_name)
        full_path = os.path.join(full_path, file_name)
        print(full_path)
        with open(full_path, "wb") as file:
            file.write(pickle.dumps(task_status))

saver = Serialization()

class UnSerialization:
    def __call__(self, task_id):
        self.task_id = task_id
        path = os.path.join(os.path.join(os.path.abspath(os.curdir), "for_save"), task_id)
        with open(path, "rb") as file:
            task = pickle.load(file)
            return task

read_from_memory = UnSerialization()
