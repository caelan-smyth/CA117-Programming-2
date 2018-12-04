class BankAccount(object):
	next_account_number = 16555232
	total_lodgements = 0
	interest_rate = 0.043

	def __init__(self, forename, surname, balance=0):
		self.name = "{} {}".format(forename, surname)
		self.balance = balance
		self.account = BankAccount.next_account_number

		BankAccount.next_account_number += 1
		BankAccount.total_lodgements += 1

	def __iadd__(self, amount):
		self.balance += int(amount)
		return self

	def __str__(self):
		accinfo = []
		accinfo.append("Name: {}".format(self.name))
		accinfo.append("Account number: {}".format(self.account))
		accinfo.append("Balance: {:.2f}".format(self.balance))

		return "\n".join(accinfo)

	def lodge(self, amount):
		self.balance += int(amount)
		BankAccount.total_lodgements += 1

	def apply_interest(self):
		self.balance *= (1 + self.interest_rate)