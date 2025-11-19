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
    last_id = 0
    def __init__(self, customer):
        self.customer = customer
        Account.last_id += 1
        self.id = Account.last_id
        self._balance = 0

    def __repr__(self):
        return f'Ac[{self.id}, {self.customer.last_name}, {self.customer._balance}]'

class Bank:
    def __init__(self):
        self.name = name
        self.customer_list = []
        self.account_list = []

    def create_customer(self, first_name, last_name):
        c = Customer(first_name, last_name)
        self.customer_list.append(c)
        return c

    def create_account(self, customer):
        a = Account(customer)
        self.account_list.append(a)
        return a

    def __repr__(self):
        return f'Bank[{self.name}: \n{self.customer_list}\n {self.account_list}]'

bank = Bank('SGH Bank')

c1 = bank.create_customer('John', 'Smith')
a1 = bank.create_account(c1)
a2 = bank.create_account(c1)
print(bank)
c2 = bank.create_customer('Anne', 'Brown')
a3 = bank.create_account(c2)
print('--------------')
print(bank)
