# Towers of Hanoi program
# using lists treated as stacks and recursion
# this works with any positive number of rings and is a perfect example of recursion and it also shows how lists can be used as stacks

def recMove(ring, beginning, end, extra): #define a recursive function (number of the ring being moved, the tower the ring is being moved from, the tower the ring is being moved to, and the spare tower that is carried through for future recursions)
	if ring == 1: # base case for recursion function. without a base case recursion continues forever.
		end.append(beginning.pop()) #adds to the top of the current 'end' tower the top of the current 'beginning' tower while also removing it from 'beginning' tower
		print "moved ring 1" # describes what is happening in this step
		print "----------------"
		print "tower 1:",tower1 #update of what the tower has currently for rings
		print "tower 2:",tower2 #update of what the tower has currently for rings
		print "tower 3:",tower3 #update of what the tower has currently for rings
		print "----------------"
	else:
		print "add first recursive call for ring", ring - 1 # tells user that this is the first recursive call for the ring with the number one lower than the ring used in the active call
		recMove(ring - 1, beginning, extra, end) # this is the first call made during each non base recursive call. notice that 'end' and 'extra' have swapped.
		print "ended first recursion for ring", ring -1 # tells user that the first recursive call for the ring with the number one lower than the ring used in the active call has ended
		end.append(beginning.pop()) #adds to the top of the current 'end' tower the top of the current 'beginning' tower while also removing it from 'beginning' tower
		print "moved ring", ring # describes what is happening in this step
		print "----------------"
		print "tower 1:",tower1 #update of what the tower has currently for rings
		print "tower 2:",tower2 #update of what the tower has currently for rings
		print "tower 3:",tower3 #update of what the tower has currently for rings
		print "----------------"
		print "add second recursive call for ring", ring -1 # tells user that this is the second recursive call for the ring with the number one lower than the ring used in the active call
		recMove(ring - 1, extra, end, beginning) # this is the second call made during each non base recursive call. notice that 'beginning' and 'extra' have swapped.
		print "ended second recursion for ring", ring -1 # tells user that this is the second recursive call for the ring with the number one lower than the ring used in the active call has ended
	

tower1 = [] #create empty list
tower2 = [] #create empty list
tower3 = [] #create empty list

nRings = int(raw_input("enter the number of rings to use: ")) #user enters the number of rings they want to use

while nRings > 0: #this while loop adds the rings to the first list/tower
	tower1.append(nRings) #adds the number to top of list stack
	nRings = nRings - 1 #decrements counter
print "tower 1:",tower1 #update of what the tower has currently for rings
print "tower 2:",tower2 #update of what the tower has currently for rings
print "tower 3:",tower3 #update of what the tower has currently for rings
print
print "initial recursive call with", len(tower1), "rings" # prints start of recursion in program
recMove(len(tower1), tower1, tower3, tower2) #initial recursive call that starts the process that leads to all other recursive calls (using the size of tower1 which is the only list with any items in it ensures that it moves all rings, 'beginning' is tower1 because that is where all rings start, 'end' is tower3 because that is where I want all the rings to end up, 'extra' is tower2 because that is the only tower left)
print "finish recursive call for ring", len(tower3) # prints end of recursion in program
print
print "tower 1:",tower1 #update of what the tower has currently for rings
print "tower 2:",tower2 #update of what the tower has currently for rings
print "tower 3:",tower3 #update of what the tower has currently for rings
print
raw_input("press enter to exit") # Stops program from auto closing
