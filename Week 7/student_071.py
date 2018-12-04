class Student(object):

	def __init__(self, surname, forename, sid, modlist = []):
		self.surname = surname
		self.forename = forename
		self.sid = sid
		self.modlist = modlist

	def add_module(self, mod):
		if mod not in self.modlist:
			self.modlist.append(mod)

	def del_module(self, mod):
		if mod in self.modlist:
			self.modlist.remove(mod)

	def print_details(self):
		print("ID: {}".format(self.sid))
		print("Surname: {}".format(self.surname))
		print("Forename: {}".format(self.forename))
		print("Modules: {}".format(" ".join(self.modlist)))