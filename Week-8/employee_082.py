class Employee(object):
	next_employee_number = 0

	def __init__(self, name, hours_worked=0, hourly_rate = 9.25):
		self.name = name
		self.id = Employee.next_employee_number
		self.hours = hours_worked
		self.rate = hourly_rate

		Employee.next_employee_number += 1

	def __str__(self):
		employee_info = []
		employee_info.append("Name: {}".format(self.name))
		employee_info.append("ID: {}".format(self.id))
		employee_info.append("Hours: {:.2f}".format(self.hours))
		employee_info.append("Rate: {:.2f}".format(self.rate))
		employee_info.append("Wages: {:.2f}".format(self.hours * self.rate))
		return "\n".join(employee_info)

	def add_hours(self, n):
		self.hours += n