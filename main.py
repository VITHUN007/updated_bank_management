import datetime
from abc import ABC, abstractmethod
import random
import time
import re 

class Account(ABC):
    
    _next_account_id = 1000

    def __init__(self, initial_deposit: float = 0.0):
        self._account_id = str(Account._next_account_id)
        Account._next_account_id += 1
        self._balance = initial_deposit
        self._opened_date = datetime.date.today()
        self._transactions = []
        
        if initial_deposit > 0:
            self._record_transaction(
                amount=initial_deposit,
                trans_type="deposit",
                description="Initial Deposit"
            )

    def get_account_id(self):
        return self._account_id

    def get_balance(self) -> float:
        return self._balance

    def _record_transaction(self, amount: float, trans_type: str, description: str = ""):
        transaction = Transaction(
            account_id=self._account_id,
            amount=amount,
            trans_type=trans_type,
            description=description
        )
        transaction.execute(self)
        self._transactions.append(transaction)

    def deposit(self, amount: float):
        if amount > 0:
            self._balance += amount
            self._record_transaction(amount, "deposit", f"Deposit of {amount}")
            return True
        print("Error: Deposit amount must be positive.")
        return False

    @abstractmethod
    def withdraw(self, amount: float) -> bool:
        raise NotImplementedError("Subclass must implement abstract method 'withdraw'")

    @abstractmethod
    def calculate_interest(self) -> float:
        raise NotImplementedError("Subclass must implement abstract method 'calculate_interest'")

    def get_transaction_history(self) -> list:
        return self._transactions

class SavingAccount(Account):
    DEFAULT_INTEREST_RATE = 0.02

    def __init__(self, initial_deposit: float):
        self._interest_rate = SavingAccount.DEFAULT_INTEREST_RATE
        super().__init__(initial_deposit)

    def withdraw(self, amount: float) -> bool:
        if amount <= 0:
            print("Error: Withdrawal amount must be positive.")
            return False
        if self._balance >= amount:
            self._balance -= amount
            self._record_transaction(amount, "withdraw", f"Withdrawal of {amount}")
            return True
        else:
            print("Transaction Denied: Insufficient funds in Savings Account.")
            return False

    def calculate_interest(self) -> float:
        interest_amount = self._balance * self._interest_rate
        if interest_amount > 0:
            self._balance += interest_amount
            self._record_transaction(interest_amount, "interest", "Annual Interest Applied")
        return interest_amount

class CurrentAccount(Account):
    DEFAULT_OVERDRAFT_LIMIT = 500.0

    def __init__(self, initial_deposit: float):
        self._overdraft_limit = CurrentAccount.DEFAULT_OVERDRAFT_LIMIT
        super().__init__(initial_deposit)

    def withdraw(self, amount: float) -> bool:
        if amount <= 0:
            print("Error: Withdrawal amount must be positive.")
            return False

        max_allowed = self._balance + self._overdraft_limit

        if max_allowed >= amount:
            self._balance -= amount
            self._record_transaction(amount, "withdraw", f"Withdrawal of {amount}")
            return True
        else:
            print(f"Transaction Denied: Exceeds overdraft limit of ${self._overdraft_limit:.2f}.")
            return False

    def calculate_interest(self) -> float:
        interest_amount = 0.0
        if self._balance > 0:
            interest_amount = self._balance * 0.005
            self._balance += interest_amount
            self._record_transaction(interest_amount, "interest", "Small Interest Applied")
        return interest_amount

class Transaction:
    def __init__(self, account_id: str, amount: float, trans_type: str, description: str):
        self._transaction_id = str(random.randint(100000, 999999))
        self._account_id = account_id
        self._date = datetime.datetime.now()
        self._amount = amount
        self._type = trans_type
        self._description = description

    def execute(self, account: Account) -> bool:
        return True

    def __str__(self):
        return (f"[{self._date.strftime('%Y-%m-%d %H:%M:%S')}] "
                f"ID: {self._transaction_id} | Type: {self._type.upper()} | "
                f"Amount: ${self._amount:.2f} | Desc: {self._description}")

class User:
    def __init__(self, name: str):
        self._name = name
        self._accounts = {}

    def get_name(self):
        return self._name
        
    def open_account(self, account_type: str, initial_deposit: float = 0.0) -> str | None:
        account = None
        account_type = account_type.lower()
        
        try:
            if account_type == "saving":
                account = SavingAccount(initial_deposit)
            elif account_type == "current":
                account = CurrentAccount(initial_deposit)
            else:
                return None
            
        except ValueError:
             return None

        account_id = account.get_account_id()
        self._accounts[account_id] = account
        return account_id

    def get_account(self, account_id: str) -> Account | None:
        return self._accounts.get(account_id)

    def get_all_account_ids(self) -> list[str]:
        return list(self._accounts.keys())

def display_menu(user_name: str):

    print("\n" + "="*40)
    print(f"      {user_name}'s Banking Menu")
    print("="*40)
    print("1: Create New Account")
    print("2: Deposit Funds")
    print("3: Withdraw Funds")
    print("4: View Account Balance")
    print("5: View Transaction History")
    print("6: Apply Interest/Fees")
    print("7: Exit")
    print("="*40)

def handle_account_creation(user: User):
    print("\n--- 1. Create New Account ---")
    
    while True:
        acc_type = input("Enter account type (Saving/Current): ").lower()
        if acc_type in ['saving', 'current']:
            break
        print("Invalid type. Please enter 'Saving' or 'Current'.")

    while True:
        try:
            initial_deposit = float(input("Enter initial deposit amount (e.g., 100.00): $"))
            if initial_deposit >= 0:
                break
            print("Deposit must be a non-negative number.")
        except ValueError:
            print("Invalid input. Please enter a numerical value.")

    new_id = user.open_account(acc_type, initial_deposit)

    if new_id:
        print(f"\n SUCCESS! {user.get_name()} opened a {acc_type.capitalize()} Account.")
        print(f"   Your New Account ID is: {new_id}")
    else:
        print(" ACCOUNT CREATION FAILED. Please try again.")

def get_account_choice(user: User) -> Account | None:
    if not user.get_all_account_ids():
        print(" No accounts found. Please create an account first (Option 1).")
        return None

    print(f"Available Account IDs: {', '.join(user.get_all_account_ids())}")
    account_id = input("Enter the Account ID: ")
    account = user.get_account(account_id)
    
    if not account:
        print(f" Error: Account ID '{account_id}' not found.")
        return None
    return account

def handle_deposit(user: User):
    print("\n--- 2. Deposit Funds ---")
    account = get_account_choice(user)
    if not account: return

    while True:
        try:
            amount = float(input("Enter deposit amount: $"))
            if amount > 0:
                break
            print("Deposit amount must be positive.")
        except ValueError:
            print("Invalid input. Please enter a numerical value.")
    
    if account.deposit(amount):
        print(f" Deposit successful. New Balance: ${account.get_balance():.2f}")
    else:
        print(" Deposit failed.")

def handle_withdrawal(user: User):
    print("\n--- 3. Withdraw Funds ---")
    account = get_account_choice(user)
    if not account: return

    print(f"Current Balance for {account.get_account_id()}: ${account.get_balance():.2f}")

    while True:
        try:
            amount = float(input("Enter withdrawal amount: $"))
            if amount > 0:
                break
            print("Withdrawal amount must be positive.")
        except ValueError:
            print("Invalid input. Please enter a numerical value.")

    if account.withdraw(amount):
        print(f" Withdrawal successful. New Balance: ${account.get_balance():.2f}")
    else:
        print(" Withdrawal failed.")
        
def handle_view_balance(user: User):
    print("\n--- 4. View Account Balance ---")
    account = get_account_choice(user)
    if not account: return

    print(f" Account ID {account.get_account_id()} Balance: ${account.get_balance():.2f}")

def handle_view_transactions(user: User):
    print("\n--- 5. View Transaction History ---")
    account = get_account_choice(user)
    if not account: return

    history = account.get_transaction_history()
    if history:
        print(f"\n--- History for Account {account.get_account_id()} ---")
        for t in history:
            print(t)
    else:
        print("No transactions recorded for this account.")

def handle_calculate_interest(user: User):
    print("\n--- 6. Apply Interest/Fees (Run Month-End) ---")
    account = get_account_choice(user)
    if not account: return
    
    initial_balance = account.get_balance()
    interest_amount = account.calculate_interest() 

    if interest_amount > 0:
        print(f" Successfully applied ${interest_amount:.2f} in interest/fees.")
    elif interest_amount == 0 and initial_balance > 0:
        print(" No interest applied (Current Account balance was positive but no interest accrued).")
    else:
        print(" No interest or fees applied.")

    print(f"Current Balance: ${account.get_balance():.2f}")

def create_user_with_validation() -> User:
    print("Welcome to the Interactive Bank Management System!")
    
    while True:
        name = input("Please enter your full name (only letters and spaces allowed): ").strip()
        
        if re.fullmatch(r"[A-Za-z\s]+", name) and name:
            return User(name)
        else:
            print(" Invalid Name. Name must contain only letters and spaces. Please try again.")

def main_menu():
    client = create_user_with_validation()
    
    print(f"\nWelcome, {client.get_name()}! Let's start managing your finances.")

    while True:
        display_menu(client.get_name())
        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            handle_account_creation(client)
        elif choice == '2':
            handle_deposit(client)
        elif choice == '3':
            handle_withdrawal(client)
        elif choice == '4':
            handle_view_balance(client)
        elif choice == '5':
            handle_view_transactions(client)
        elif choice == '6':
            handle_calculate_interest(client)
        elif choice == '7':
            print(f"\nThank you, {client.get_name()}, for using the Bank System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")
        
        time.sleep(1)

if __name__ == "__main__":
    main_menu()
