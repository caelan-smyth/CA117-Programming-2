import sys

contacts = {}

def contact(filename):
	f = open(filename, "r")
	for line in f:
		lines = line.split()
		contacts[lines[0]] = lines[1]
	f.close()
	
def contactsearch(s):
	if s in contacts:
		print("Name: {}".format(s))
		print("Phone: {}".format(contacts[s]))
	
	else:
		print("Name: {}".format(s))
		print("No such contact")

def main():
	contact(sys.argv[1])
	for line in sys.stdin:
		(contactsearch(line.strip()))

if __name__ == '__main__':
	main()