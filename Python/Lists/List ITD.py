# This is an interactive test driver

def lAdd(element):# adds an element to the list
	thisList.append(element)
	print "successfully added", element
def lRemove(element):# removes an element from the list
	if lContains(element):
		thisList.remove(element)
		print "successfully removed", element
	else:
		print element, "is not in the list"
def lFind(element):# returns an element in list, 
	for value in thisList:
		if value == element:
			return value
def lContains(element):# returns true if element in list
	if lFind(element) == element:
		return True
	else:
		return False
def lSize():# returns the size of the list
	return len(thisList)
def ltoString():# returns a string of the element
	print thisList
def lInsert(element, location):# adds an element at the location chosen
	try:
		thisList.insert(int(location), element)
		print "successfully inserted", element, "in index", location
	except:
		print "not a valid index"
def lSort(): #Sorts the list
	print "Before: ", ltoString()
	thisList.sort()
	print "After: ", ltoString()
def lIndex(element): # prints the name of the element and its location if in the list
	if lContains(element):
		print element, "is located at index",thisList.index(element)
	else:
		print element, "is not in the list"
def lReverse(): # reverses the order of the elements in the list
	print "Before: ", ltoString()
	thisList.reverse()
	print "After: ", ltoString()

def showMenu(): # displays the menu of commands
	print "1: Add"
	print "2: Remove"
	print "3: Find"
	print "4: Sort"
	print "5: Size"
	print "6: Insert"
	print "7: Reverse"
	print "8: Print List"
	print "9: Clear List"
	print "0: Exit"


############################
#Start of Main ITD         #
############################

thisList = list() # creates a blank list
exit = False
name = raw_input("Hello, Please enter your name: ")
print "Thank you", name + ",", "this is an interactive test driver."
print "I have created this one for you to test the list data structure in python, enjoy"
while not exit: # this loop asks for input and performs whatever action is chosen from the showMenu function until the exit command is given
	print
	showMenu()
	print
	choice = -1
	try:
		choice = int(raw_input("please make a choice: "))
	except:
		print "You must enter an integer"
	if choice == 1:
		lAdd(raw_input("Enter Data: "))
	elif choice == 2:
		lRemove(raw_input("Enter Data To Remove: "))
	elif choice == 3:
		lIndex(raw_input("Enter Data To Find: "))
	elif choice == 4:
		lSort()
	elif choice == 5:
		print "there are", lSize(), "items in this list" 
	elif choice == 6:
		lInsert(raw_input("Enter Data: "), raw_input("Enter Index: "))
	elif choice == 7:
		lReverse()
	elif choice == 8:
		ltoString()
	elif choice == 9:
		thisList = []
	elif choice == 0:
		exit = True
	else:
		print "please make a choice between 1 and 9"

print "Come Back Soon!!"
raw_input("press enter to exit")