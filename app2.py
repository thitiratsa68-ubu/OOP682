from wk09.model.bankaccount import BankAccount


my_account = BankAccount(1000)
your_account = BankAccount(500)

our_account = my_account + your_account
print(our_account)