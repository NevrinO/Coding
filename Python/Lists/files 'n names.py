# program that reads and writes names to a file
def readfile(fileName): #opens a file reads from it and turn it into a list object
	try:
		nameListFile = open(fileName,'r')
	except: # create a file with names in it
		nameListFile = open(fileName,'w')
		nameListFile.write("Jon Snow,Tyrion Lannister,Daenerys Targaryen,Arya Stark")
		nameListFile.close()
		nameListFile = open(fileName,'r')
	nameListStr = nameListFile.read() #reads a file object and turns it into a string
	namesList = nameListStr.split(",") #converts string into list where each list item is separated by a ',' 
	return namesList

def lAdd(element):# adds an element to the list
	namesList.append(element)
	print "successfully added", element
	
def lRemove(element):# removes an element from the list
		if lContains(element):
			namesList.remove(element)
			print "successfully removed", element
		else:
			if element.isdigit(): # Updated to allow removal by index if digit entered will remove an int if in list before removing by index
				#this list is intended to be filled with names not ints so know what data types you are using it for if intending on copying 
				try:
					tempPop = namesList.pop(int(element))
					print "successfully removed", tempPop
				except:
					print "there is no name located at that index. The list index starts at 0."
			else:
				print element, "is not in the list"
		
			
def lContains(element):# returns true if element in list
	if element in namesList:
		return True
	else: #this else is not needed. removing this and moving return False into its position will cause the same effect because of how 'return' works.
		#Left in to make easier to read for beginners
		return False

#-------------	
#Main Program
#-------------

print "This program reads from a file a list of names."
print "If no list exists then it creates one with a few names already in it"
print "You may then add or remove any names you want and may save it back to a file."
print ""
namesList = readfile("names.txt") # calls function that takes a file and returns a list
namesList = [s for s in namesList if s != ""] # removes empty list items generated ether by user or ',' at end of string
print namesList	# displays list to see what it contains
exit = False # bool for menu loop
while not exit: # this loop asks for input and performs whatever action is chosen until the exit command is given	
	print
	choice = -1 #resets choice to prevent endless loop or crash
	try: #trys to save string as int
		choice = int(raw_input("please make a choice(1:Add 2:Remove 3:Save 4:Print 0:Exit): "))
	except: #if not an int prints message instead of crashing
		print "You must enter an integer"
	if choice == 1: # if 1 is entered during choice then it asks for input to add to the list
		lAdd(raw_input("Enter Name To Add: "))
	elif choice == 2: # if 2 is entered during choice then it asks for a string or index to remove from the list
		lRemove(raw_input("Enter Name Or Index To Remove: "))
	elif choice == 3: # if 3 is entered during choice then it converts list into a string separating items by ',' and overwrites it file
		namesStr = "" #initializes variable for use in for loop
		for name in namesList:
			namesStr += str(name) + "," #concatenates current item on to string followed by a ','
		with open("names.txt", 'w') as namesFile: #opens file to be written too
			namesFile.write(namesStr) # writes string to file
	elif choice == 4: # if 4 is entered during choice then it prints the list
		print namesList
	elif choice == 0: #if 0 is entered during choice then it ends program
		exit = True
	else: # if anything other than 0-4 is chosen then this is entered
		print "please make a choice between 0 and 4"
raw_input("press enter to exit")
