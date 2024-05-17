from User import User
from Bank import Person


class Admin:
    def __init__(self):
        self.bank = Person()

    def create_account(self, user_name, password, initial_balance):
        new_user = User(user_name, initial_balance, self.bank)
        new_user.create_account(user_name, password)
        print("Account created successfully!")

    def check_total_balance(self):
        total_balance = sum(user.balance for user in self.bank.users.values())
        print(f"Total available balance in the bank: {total_balance}")

    def check_total_loan_amount(self):
        total_loan_amount = sum(
            user.balance * 2
            for user in self.bank.users.values()
            if hasattr(user, "loan_taken") and user.loan_taken
        )
        print(f"Total loan amount in the bank: {total_loan_amount}")

    def toggle_loan_feature(self, enable_loan):
        for user in self.bank.users.values():
            user.loan_taken = enable_loan
        if enable_loan:
            print("Loan feature is now enabled.")
        else:
            print("Loan feature is now disabled.")

    def show_menu(self):
        while True:
            print(
                "Admin Menu:\n"
                "1 -> Create Account\n"
                "2 -> Check Total Balance\n"
                "3 -> Check Total Loan Amount\n"
                "4 -> Toggle Loan Feature\n"
                "5 -> Exit"
            )
            choice = input("Enter your choice: ")
            if choice == "1":
                user_name = input("Enter user name: ")
                password = input("Enter password: ")
                initial_balance = float(input("Enter initial balance: "))
                self.create_account(user_name, password, initial_balance)
            elif choice == "2":
                self.check_total_balance()
            elif choice == "3":
                self.check_total_loan_amount()
            elif choice == "4":
                enable_loan = input("Enable loan feature? (Yes/No): ").lower() == "yes"
                self.toggle_loan_feature(enable_loan)
            elif choice == "5":
                print("Exiting Admin menu.")
                person = Person()  
                person.user_or_admin()  
                break  
            else:
                print("Invalid choice. Please try again.")
