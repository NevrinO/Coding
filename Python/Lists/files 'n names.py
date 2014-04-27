# program that reads and writes names to a file
def readfile(fileName):
	try:
		nameListFile = open(fileName,'r')
	except:
		nameListFile = open(fileName,'w')
		nameListFile.write("Jon Snow,Tyrion Lannister,Daenerys Targaryen,Arya Stark")
		nameListFile.close()
		nameListFile = open(fileName,'r')
	nameListStr = nameListFile.read()
	nameList = nameListStr.split(",")
	return nameList

def lAdd(element):# adds an element to the list
	namesList.append(element)
	print "successfully added", element
	
def lRemove(element):# removes an element from the list
		if lContains(element):
			namesList.remove(element)
			print "successfully removed", element
		else:
			if element.isdigit(): # Updated to allow removal by index if digit entered will remove an int if in list before removing by index
				try:
					print "successfully removed", namesList.pop(int(element))
				except:
					print "there is no name located at that index. The list index starts at 0."
			else:
				print element, "is not in the list"
		
def lFind(element):# returns an element in list, 
	for value in namesList:
		if value == element:
			return value
			
def lContains(element):# returns true if element in list
	if lFind(element) == element:
		return True
	else:
		return False

#-------------	
#Main Program
#-------------

print "This program reads from a file a list of names."
print "If no list exists then it creates one with a few names already in it"
print "You may then add or remove any names you want and may save it back to a file."
print ""
namesList = readfile("names.txt")
while lContains(""):
	namesList.remove("")
print namesList
exit = False
while not exit: # this loop asks for input and performs whatever action is chosen until the exit command is given	
	print
	choice = -1
	try:
		choice = int(raw_input("please make a choice(1:Add 2:Remove 3:Save 4:Print 0:Exit): "))
	except:
		print "You must enter an integer"
	if choice == 1:
		lAdd(raw_input("Enter Name To Add: "))
	elif choice == 2:
		lRemove(raw_input("Enter Name Or Index To Remove: "))
	elif choice == 3:
		namesStr = ""
		for name in namesList:
			namesStr += str(name) + ","
		with open("names.txt", 'w') as namesFile:
			namesFile.write(namesStr)
	elif choice == 4:
		print namesList
	elif choice == 0:
		exit = True
	else:
		print "please make a choice between 0 and 4"
raw_input("press enter to exit")