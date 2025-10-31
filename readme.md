#  Interactive Bank Management System (Python OOP)

This is a console-based bank management system implemented in Python, demonstrating key **Object-Oriented Programming (OOP)** principles such as Abstraction, Encapsulation, Inheritance, and Polymorphism.

## FEATURES

* **User Management:** Prompts the user for a name with input validation.
* **Account Creation:** Supports opening two types of accounts:
    * **Savings Account:** Subject to interest and has strict insufficient funds checks.
    * **Current Account:** Allows withdrawals up to a defined **overdraft limit**.
* **Transaction Handling:** Allows for deposits and withdrawals with real-time balance updates.
* **Interest/Fees Calculation:** A dedicated function to apply month-end interest/fees, demonstrating polymorphism.
* **Transaction History:** Logs all transactions (deposits, withdrawals, interest) with timestamps and unique transaction IDs.

## CONCEPT DEFINITION
OOP Concept used definition
* **Encapsulation** : bundling data and method  into single unit

* **Inheritance**:child class allow to uses parentclass

* **Polymorphism** : object to take multiple form depending upon the context used

* **Abstraction** :showing necessary information hiding internal information

##  PROJECT STRUCTURE(OOP Concepts)

| Class | Type | OOP Concept Demonstrated | Description |
| :--- | :--- | :--- | :--- |
| `Account` | **Abstract Base Class (ABC)** | **Abstraction, Encapsulation** | Defines the generic interface (`deposit`, `withdraw`, `calculate_interest`). Handles core data like `_balance` and `_transactions`. |
| `SavingAccount` | Concrete Subclass | **Inheritance, Polymorphism** | Inherits from `Account`. Implements `withdraw` with strict balance check. Implements `calculate_interest` with a 2% rate. |
| `CurrentAccount` | Concrete Subclass | **Inheritance, Polymorphism** | Inherits from `Account`. Implements `withdraw` allowing overdraft. Implements `calculate_interest` with a small 0.5% rate. |
| `Transaction` | Utility Class | **Encapsulation** | Stores details for each financial activity (timestamp, amount, type). |
| `User` | Manager Class | **Composition, Encapsulation** | Manages a user's collection of `Account` objects. |

---

##  HOW TOO RUN

### Prerequisites

ensure python is installed     
* Python --version

 Clone or Download this project folder:

* git clone :  https://github.com/VITHUN007/updated_bank_management.git

## EXECUTION

1.  Save the provided code as a Python file (e.g., `main.py`).
2.  Open your terminal or command prompt.
3.  Navigate to the directory where you saved the file.
4.  Run the script using the Python interpreter:

    ```bash
    python main.py
    ```

5.  Follow the on-screen prompts. The system will first ask for your name and then present the main banking menu.

---

## SAMPLE OUTPUT
### benjamin's Banking Menu ###

#### 1: Create New Account ####
#### 2: Deposit Funds ####
#### 3: Withdraw Funds ####
#### 4: View Account Balance ####
#### 5: View Transaction History ####
#### 6: Apply Interest/Fees ####
#### 7: Exit ####
---

Enter your choice (1-7): 1

--- 1. Create New Account ---
Enter account type (Saving/Current): saving
Enter initial deposit amount (e.g., 100.00): $1000

 SUCCESS! benjamin opened a Saving Account.
   Your New Account ID is: 1000
   

   ___

### benjamin's Banking Menu ###

#### 1: Create New Account ####
#### 2: Deposit Funds ####
#### 3: Withdraw Funds ####
#### 4: View Account Balance ####
#### 5: View Transaction History ####
#### 6: Apply Interest/Fees ####
#### 7: Exit ####

---

Enter your choice (1-7): 2

--- 2. Deposit Funds ---
Available Account IDs: 1000
Enter the Account ID: 1000
Enter deposit amount: $1000
 Deposit successful. New Balance: $2000.00

 ----


### benjamin's Banking Menu ###

#### 1: Create New Account ####
#### 2: Deposit Funds ####
#### 3: Withdraw Funds ####
#### 4: View Account Balance ####
#### 5: View Transaction History ####
#### 6: Apply Interest/Fees ####
#### 7: Exit ####

---

Enter your choice (1-7): 3

--- 3. Withdraw Funds ---
Available Account IDs: 1000
Enter the Account ID: 1000
Current Balance for 1000: $2000.00
Enter withdrawal amount: $1200
 Withdrawal successful. New Balance: $800.00

 ___


### benjamin's Banking Menu ###

#### 1: Create New Account ####
#### 2: Deposit Funds ####
#### 3: Withdraw Funds ####
#### 4: View Account Balance ####
#### 5: View Transaction History ####
#### 6: Apply Interest/Fees ####
#### 7: Exit ####

---

Enter your choice (1-7): 4

--- 4. View Account Balance ---
Available Account IDs: 1000
Enter the Account ID: 1000
 Account ID 1000 Balance: $800.00

 ___


### benjamin's Banking Menu ###

#### 1: Create New Account ####
#### 2: Deposit Funds ####
#### 3: Withdraw Funds ####
#### 4: View Account Balance ####
#### 5: View Transaction History ####
#### 6: Apply Interest/Fees ####
#### 7: Exit ####

---

Enter your choice (1-7): 5

--- 5. View Transaction History ---

Available Account IDs: 1000

Enter the Account ID: 1000

--- History for Account 1000 ---
[2025-10-31 09:22:22] ID: 838993 | Type: DEPOSIT | Amount: $1000.00 | Desc: Initial Deposit

[2025-10-31 09:22:32] ID: 494626 | Type: DEPOSIT | Amount: $1000.00 | Desc: Deposit of 1000.0

[2025-10-31 09:22:46] ID: 129145 | Type: WITHDRAW | Amount: $1200.00 | Desc: Withdrawal of 1200.0

___


### benjamin's Banking Menu ###

#### 1: Create New Account ####
#### 2: Deposit Funds ####
#### 3: Withdraw Funds ####
#### 4: View Account Balance ####
#### 5: View Transaction History ####
#### 6: Apply Interest/Fees ####
#### 7: Exit ####

---

Enter your choice (1-7): 6

--- 6. Apply Interest/Fees (Run Month-End) ---
Available Account IDs: 1000
Enter the Account ID: 1000
 Successfully applied $16.00 in interest/fees.
Current Balance: $816.00

___


### benjamin's Banking Menu ###

#### 1: Create New Account ####
#### 2: Deposit Funds ####
#### 3: Withdraw Funds ####
#### 4: View Account Balance ####
#### 5: View Transaction History ####
#### 6: Apply Interest/Fees ####
#### 7: Exit ####

---

Enter your choice (1-7): 7

Thank you, benjamin, for using the Bank System. Goodbye! 

---