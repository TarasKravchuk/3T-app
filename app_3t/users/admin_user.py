from app_3t.core.data_storage import *
from app_3t.core.console_starter import *
from app_3t.core.password import *

class Admin_User:
    def __init__(self, password):
        self.class_user = 'admin_user'
        self.name_user = 'admin_user'
        self.password = password
        self.admin_information = (self.class_user, self.name_user, self.password)

    @staticmethod
    def existence_admin():
        path = os.path.join(os.path.join(os.path.abspath(os.curdir), "for_save", "admin_user"))
        try:
            with open(path, "rb") as file:
                admin_user = pickle.load(file)
                if admin_user.class_user != 'admin_user':
                    print("Admin User has been deleted or has not been created")
                    create_admin()
        except FileNotFoundError:
            print("Admin User has been deleted or has not been created")
            create_admin()

def create_admin():
    password = password_security()
    admin = Admin_User (password)
    saver(admin, admin.class_user)
