import sys

def contact(filename):
	contacts = {}
	with open(filename, "r") as f:
		for line in f:
			name, phone, email = line.strip().split()
			contacts[name] = (phone, email)
	return contacts

def main():
	contacts = contact(sys.argv[1])
	for line in sys.stdin:
		name = line.strip()
		print("Name: {}".format(name))
		if name in contacts:
			print("Phone: {}".format(contacts[name][0]))
			print("Email: {}".format(contacts[name][1]))
		else:
			print("No such contact")
			#print("poo")

if __name__ == '__main__':
	main()