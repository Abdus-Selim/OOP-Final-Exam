from Bank import Person
class User:
    def __init__(self, name, amount, person) -> None:
        self.name = name
        self.balance = amount
        self.user_name = None
        self.password = None
        self.transaction_history = []
        self.person = person

    def create_account(self, user_name, password):
        self.user_name = user_name
        self.password = password
        print("Account created successfully!")
        self.person.add_user(user_name, self)

    def login_account(self):
        user_name = input("Enter Username: ")
        password = input("Enter Password: ")
        user = self.person.get_user(user_name)
        if user and user.password == password:
            self.show_menu()
        else:
            print("Invalid Username or Password. Try again!")
            self.login_account()

    def show_menu(self):
        while True:
            print(
                "User Menu:\n"
                "1 -> Create an Account\n"
                "2 -> Login\n"
                "3 -> Deposit\n"
                "4 -> Withdraw\n"
                "5 -> Check Balance\n"
                "6 -> Transfer Amount\n"
                "7 -> Check Transaction History\n"
                "8 -> Take Loan\n"
                "9 -> Logout"
            )
            choice = input("Enter your choice: ")
            if choice == "1":
                self.check_account()
            elif choice == "2":
                self.login_account()
            elif choice == "3":
                self.deposit()
            elif choice == "4":
                self.withdraw()
            elif choice == "5":
                self.check_balance()
            elif choice == "6":
                self.transfer_amount()
            elif choice == "7":
                self.check_transaction_history()
            elif choice == "8":
                self.take_loan()
            elif choice == "9":
                print("Logged out successfully!")
                person = Person()
                person.user_or_admin()
                break
            else:
                print("Invalid choice. Please try again.")

    def deposit(self):
        amount = float(input("Enter amount to deposit: "))
        self.balance += amount
        self.transaction_history.append(f"Deposited {amount}")
        print(f"{amount} TK deposited Successfully!")
        self.show_menu()

    def withdraw(self):
        print(f"You have {self.balance} in your account")
        withd_amount = float(input("How much do you want to withdraw? "))
        if withd_amount <= self.balance:
            self.balance -= withd_amount
            self.transaction_history.append(f"Withdrew {withd_amount}")
            print("Successful Withdrawal!")
        else:
            print("Insufficient funds in the bank. Bankrupt!")

    def check_balance(self):
        print(f"Your current balance is: {self.balance}")

    def transfer_amount(self):
        recipient_name = input("Enter recipient's username: ")
        recipient = self.person.get_user(recipient_name)
        if recipient:
            amount = float(input("Enter amount to transfer: "))
            if amount <= self.balance:
                self.balance -= amount
                self.transaction_history.append(
                    f"Transferred {amount} to {recipient_name}"
                )
                recipient.balance += amount
                recipient.transaction_history.append(
                    f"Received {amount} from {self.user_name}"
                )
                print("Transfer successful.")
            else:
                print("Insufficient balance.")
        else:
            print("Recipient not found.")

    def check_transaction_history(self):
        print("Transaction History:")
        for transaction in self.transaction_history:
            print(transaction)

    def take_loan(self):
        if not self.loan_taken:
            loan_amount = self.balance * 2
            print(f"You are eligible for a loan of {loan_amount}.")
            confirm = input("Do you want to take the loan? (Yes/No): ")
            if confirm.lower() == "yes":
                self.balance += loan_amount
                self.transaction_history.append(f"Took a loan of {loan_amount}")
                self.loan_taken = True
                print("Loan taken successfully!")
            else:
                print("You declined the loan offer.")
        else:
            print("Sorry, you have already taken a loan.")

    def check_account(self):
        have_acc = input("Do you have an account?(Yes/ No) ")
        if have_acc.lower() == "yes":
            print("Login")
        elif have_acc.lower() == "no":
            print("Sign Up")
            self.create_account(
                input("Enter a user name: "), input("Enter a password: ")
            )
        else:
            print("Please write Yes/ No only!")
