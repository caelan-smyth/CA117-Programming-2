class Employee(object):

	def __init__(self, name, number):
		self.name = name
		self.number = number

	def wages(self):
		return 0

	def __str__(self):
		string = []
		string.append("Name: {}".format(self.name))
		string.append("Number: {}".format(self.number))
		string.append("Wages: {:.2f}".format(self.wages()))

		return "\n".join(string)

class Manager(Employee):

	def __init__(self, name, number, salary):
		super().__init__(name, number)
		self.salary = float(salary)

	def wages(self):
		return self.salary / 52

class AssemblyWorker(Employee):

	def __init__(self, name, number, hourly_rate, hours):
		super().__init__(name, number)
		self.hourly_rate = float(hourly_rate)
		self.hours = int(hours)

	def wages(self):
		return self.hourly_rate * self.hours
