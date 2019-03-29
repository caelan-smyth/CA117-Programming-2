class BankAccount(object):
	next_account_number = 16555232
	account_type = "General"

	def __init__(self, fore, sur, balance):
		self.name = "{} {}".format(fore, sur)
		self.balance = float(balance)
		self.number = int(BankAccount.next_account_number)
		BankAccount.next_account_number += 1

	def lodge(self, number):
		self.balance += int(number)

	def withdraw(self, number):
		if self.balance >= int(number):
			self.balance -= int(number)
		else:
			print("Insufficient funds available")

	def __str__(self):
		string = []
		string.append("Name: {}".format(self.name))
		string.append("Account number: {}".format(self.number))
		string.append("Account type: {}".format(self.account_type))
		string.append("Balance: {:.2f}".format(self.balance))
		return "\n".join(string)

class CurrentAccount(BankAccount):
	overdraft = float(-1000)
	account_type = "Current"

	def withdraw(self, number):
		if self.balance - int(number) >= -1000:
			self.balance -= int(number)
		else:
			print("Insufficient funds available")

	def __str__(self):
		string = []
		string.append(super().__str__())
		string.append("Overdraft: {:.2f}".format(self.overdraft))
		return "\n".join(string)

class SavingsAccount(BankAccount):
	interest_rate = float(0.01)
	account_type = "Savings"

	def apply_interest(self):
		self.balance *= (1 + self.interest_rate)

	def __str__(self):
		string = []
		string.append(super().__str__())
		string.append("Interest rate: {:.2f}".format(self.interest_rate))
		return "\n".join(string)