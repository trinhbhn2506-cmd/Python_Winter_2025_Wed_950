from datetime import datetime

class AccountTransaction:
    def __init__(self, account_id, type_name, amount, related_account_id = None):
        self.transaction_id = hash(datetime.now())
        self.account_id = account_id
        self.type = type_name
        self.amount = amount
        self.timestamp = datetime.now()
        self.related_account_id = related_account_id

    def __repr__(self):
        related_info = f" -> Acc[{self.related_account_id}]" if self.related_account_id else ""
        return (f"Txn[{self.account_id}, {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}]: "
                f"{self.type} {self.amount:,.2f}{related_info}")

class Customer:
    last_id = 0
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        Customer.last_id += 1
        self.id = Customer.last_id

    def __repr__(self):
        return f'Cust[{self.id}, {self.first_name}, {self.last_name}]'

class Account:
    last_id = 1000
    yearly_interest_rate = 0.02  # TODO - will be used to update the interest rate

    def __init__(self, customer):
        self.customer = customer
        Account.last_id += 1
        self.id = Account.last_id
        self._balance = 0
        self.transactions_history = []

    def _record_transaction(self, type_name, amount, related_id = None):
        txn = AccountTransaction(self.id, type_name, amount, related_id)
        self.transactions_history.append(txn)

    def deposit(self, amount, type_name = "Deposit",related_id = None):
        #TODO - as part of the home assignment please extend this method
        if not isinstance(amount, (int,float)):
            raise InvalidAmountException(f'Invalid amount type: {type(amount)}. Amount must be a number.')

        if amount <= 0:
            raise InvalidAmountException(f'Invalid amount: {amount}')
        else:
            self._balance += amount
            self._record_transaction(type_name, amount, related_id)

    def charge(self, amount, type_name = "Charge",related_id = None):
        #TODO - as part of the home assignment please extend this method
        if not isinstance(amount, (int,float)):
            raise InvalidAmountException(f'Invalid amount type: {type(amount)}. Amount must be a number.')

        if amount <= 0:
            raise InvalidAmountException(f'Invalid amount: {amount}')

        elif amount > self._balance:
            raise InsufficientFundsException(f'Insufficient funds: {amount}')
        else:
            self._balance -= amount
            self._record_transaction(type_name, -amount, related_id)

    def __repr__(self):
        return f'Acc[{self.id}, {self.customer.last_name}, {self._balance:.2f}]'

class Bank:
    def __init__(self, name):
        self.name = name
        self.customer_list = []
        self.account_list = []

    def _find_account(self, account_id):
        for account in self.account_list:
            if account.id == account_id:
                return account
        return None

    def create_customer(self, first_name, last_name):
        c = Customer(first_name, last_name)
        self.customer_list.append(c)
        return c

    def create_account(self, customer):
        a = Account(customer)
        self.account_list.append(a)
        return a

    def transfer_money(self, from_account_id, to_account_id, amount):
        # TODO - as part of the home assignment please implement this method - as names suggest the input parameters are
        # ids of the accounts to transfer money from and to and amount to transfer. You may need a helper method to find
        # those accounts based on their ids.
        from_account = self._find_account(from_account_id)
        to_account = self._find_account(to_account_id)

        if from_account is None:
            print(f"Transfer failed: Source account ID {from_account_id} is not found.")
            return False

        if to_account is None:
            print(f"Transfer failed: Destination account ID {to_account_id} is not found.")
            return False

        if from_account.id == to_account.id:
            print(f"Transfer failed: Can't transfer money to same account.")
            return False

        try:
            from_account.charge(amount, type_name = "Transfer OUT", related_id = to_account.id)
            to_account.deposit(amount, type_name = "Transfer IN", related_id = from_account.id)
            print('Transfer successful')
            return True
        except InvalidAmountException as iae:
            print(f"Transfer failed (Invalid amount): {iae}")
            return False
        except InsufficientFundsException as ife:
            print(f"Transfer failed (Insufficient funds): {ife}")
            return False

    def run_daily_interest_updater(self):
        # TODO - as part of the home assignment please implement this method
        daliy_rate = Account.yearly_interest_rate / 365

        for account in self.account_list:
            if account._balance > 0:
                interest_amount = account._balance * daliy_rate
                account.deposit(interest_amount, type_name = "Interest")
                print(f'Acc[{account.id}]: Interest added: {interest_amount:.4f}, New balance: {account._balance:.2f}')

    def generate_transaction_report(self, account_id):
        account = self._find_account(account_id)
        if account is None:
            print(f"Transaction report failed: Account ID {account_id} is not found.")
            return
        if not account.transactions_history:
            print("No transactions history.")
            return

        for txn in account.transactions_history:
            print(txn)

    def __repr__(self):
        return f'Bank[{self.name}: \n{self.customer_list}\n{self.account_list}]'

class BankException(Exception):
    pass

class InsufficientFundsException(BankException):
    pass

class InvalidAmountException(BankException):
    pass


if __name__ == '__main__':
    print("--- START DEMO---")
    bank = Bank('')

bank = Bank('SGH Bank')

c1 = bank.create_customer('John', 'Smith')
a1 = bank.create_account(c1)

c2 = bank.create_customer('Anne', 'Brown')
a2 = bank.create_account(c2)
try:
    a1.deposit(1000)
    print('Deposit successful')
except InvalidAmountException as iae:
    print(f"Deposit failed: {iae}")

try:
    a1.charge(500)
    print('Charge successful')
except BankException as e:
    print(f"Charge failed: {e}")

try:
    bank.transfer_money(a1.id, a2.id, 100)
except BankException as e:
    print(f"Transfer failed: {e}")

bank.run_daily_interest_updater()

print('\n---Bank State---')
print (bank)

print('\n---Transaction History for account a1---')
for t in a1.transactions_history:
    print(t)

print('\n---Transaction History for account a2---')
for t in a2.transactions_history:
    print(t)

print("\n--- END DEMO---")


#TODO:
# Add deposit and charge method to account - they should have a
# parameter: amount