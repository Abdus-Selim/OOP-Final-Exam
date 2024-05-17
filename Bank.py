class Person:
    def __init__(self) -> None:
        self.users = {}

    def add_user(self, name, user_object):
        self.users[name] = user_object

    def get_user(self, name):
        return self.users.get(name)

    def user_or_admin(self):
        ask = input("Are you a user? Yes/No \n")
        if ask.lower() == "yes":
            from User import User

            user_name = input("Enter username: ")
            password = input("Enter password: ")
            user = User(user_name, 1000, self)  
            user.create_account(user_name, password)
            user.show_menu()

        else:
            from admin import Admin

            admin = Admin()
            admin.show_menu()
