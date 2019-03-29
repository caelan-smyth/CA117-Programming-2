class Customer(object):
	discount = 0

	def __init__(self, name, balance, addr_line1, addr_line2, addr_line3):
		self.name = name
		self.balance = balance
		self.address = addr_line1
		self.town = addr_line2
		self.county = addr_line3

	def __str__(self):
		custinfo = []
		custinfo.append(self.name)
		custinfo.append(self.address)
		custinfo.append(self.town)
		custinfo.append(self.county)
		custinfo.append("Balance: {:.2f}".format(self.balance))
		custinfo.append("Discount: {}%".format(self.discount))
		custinfo.append("Amount due: {:.2f}".format(self.owes()))

		return "\n".join(custinfo)

	def owes(self):
		return self.balance * ((100 - self.discount) / 100)

class ValuedCustomer(Customer):
	discount = 10