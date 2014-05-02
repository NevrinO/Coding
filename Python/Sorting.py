# Sorting with Python
# This is a program that runs several types of sorting methods and times each
# Each of these sorting methods treat the lists as arrays
# So none of the sorts take advantage of any of pythons list characteristics
# I did this to maintain how they sort as they were intended to sort arrays 
#(the versions I wrote were intended for sorting arrays I just took my code from when I originally created them and adapted them to work in python)
# I also added list.sort() method just to show the difference
# I know that there are python versions of most (all?) of these sort methods 
# Maybe I will do a new sorting program that takes advantage of lists to see how much more efficient they are

import random #allows use of RNG
import time #used to get time

def initList(n, list): #fills a list with random integers
    random.seed() #generates a new seed for the RNG everytime this is called
    for i in range(n): #for each number in the range selected add a random int to list
        list.append(int(random.randrange(1,MAXRAND)))

#this just swaps the location of two integers. Made this a function because it gets used a lot in sorting and writing it once and calling it is easier on me.
def swap(list, From, To): 
    temp = list[From]
    list[From] = list[To]
    list[To] = temp

#exchange sort takes the first element and compares it against each subsequent element and swaps if necessary 
#this causes the list to sort from front to back 
#so after the first pass through the lowest number will be in the front and the others are still (most likely) out of order
#this method is slightly more efficient then bubble sort in most cases because it doesn't need a final pass to determine if it's finished
def exchangeSort(list):
    for i in range(len(list)):
        for j in range(i+1,len(list)):
            if (list[i] > list[j]):
                swap(list, i, j)

#bubble sort is usually one of the first sorts taught to new programming students because it is simple
#this takes the first two items and swaps them if necessary it then compares the second and third and swaps if necessary
#it continues to do this for each pair of adjacent elements tell it reaches the end
#it then goes back to the beginning and does it again until it has done it a number of times equal to one less than the size of the list
#this method fills from back to front meaning that the largest number will be in the last index after the first pass
def bubbleSort(list):
	for i in range(1,len(list)):
		for j in range(len(list)-1):
			if (list[j] > list[j+1]):
				swap(list, j, j+1)

#smart bubble sort works the same as bubble sort except after each pass it knows the highest elements are already at the end and so it doesn't recheck them
#this makes it slightly more efficient just by changing a 1 in the second for loop into the first for loop's variable
def smartBubbleSort(list):
	for i in range(1,len(list)):
		for j in range(len(list)-i):
			if (list[j] > list[j+1]):
				swap(list, j, j+1)

#merge sort is more complex then the exchange type sorts above
#it takes a list and cuts the list in half creating two sub lists
#it continues to do this until it has a list with only one item in it (a list of one is considered sorted)
#it then starts to combine the sub lists adding them together in order until there is only one list left
#this list is now sorted
#this method needs two functions one to continue to recursively call itself until the list is broken down into single elements
#and a second to merge the pieces back together
#while it seems like a lot of work to sort it is actually significantly more efficient then the sorts above
def mergeSort(list, low, high):
    if (low < high):
        mid = (low + high) / 2
        mergeSort(list, low, mid)
        mergeSort(list, mid+1, high)
        merge(list, low, mid, high)
		
def merge (list, low, mid, high):
    listB = [None] * len(list)
    i = low
    j = mid + 1
    k = low
	
    while (i <= mid and j <= high):
        if (list[i] < list[j]):
            listB[k] = list[i]
            i += 1
        else:
            listB[k] = list[j]
            j += 1
        k += 1
 
    while (i <= mid):
        listB[k] = list[i]
        i += 1
        k += 1
        

    while (j <= high):
        listB[k] = list[j]
        j += 1
        k += 1
    for k in range(low,high+1):
        list[k] = listB[k]

#quick sort is one of the fastest sorts and so it's popular
#this sort works by taking a list and creating a partition
#the partition then picks a value to create a pivot 
#it then moves all values lower then it to the left side
#and all values greater than it to the right
#it then creates sublists from each side of the partition and preforms the same operation on them until sorted
#while one of the most efficient it can be horribly inefficient if a poor pivot is chosen
#in the implementation I have made if this was used on an already sorted list it would be very inefficient
#there are many variations that can be done to remove this issue and as long as it is used on unsorted lists
#this version works fine
def quickSort(list, low, high):
    if (high > low):
        p = partition(list, low, high)
        quickSort(list, low, p-1)
        quickSort(list, p+1, high)
		
def partition(list, low, high):
    pivot = list[low]
    j = low

    for i in range(low + 1, high + 1):
        if (list[i] < pivot):
            j += 1
            swap(list, i, j)

    swap(list, low, j)
    return j

#heap sort is one of the most complex search algorithms there are
#it works by first turning the list into a heap where the largest number is on top
#it then moves the root element (the one that is on top) to the end of the list
#it then finds the next largest number and makes that the new root
#it is able to do this so efficiently because a heap is a type of binary tree
#where each element connected below the element above it is smaller then the element that is above it
#in a heap they are often called parents and children and because it is a binary tree each parent has a maximum of two children
def heapSort(list, length):
    for i in range(length):
        reheapUp(list, i)
    for j in range(length):
        swap(list, 0, length-1-j)
        reheapDown(list, 0, length-2-j)

def reheapUp(list, i):
    if (i > 0):
        parent = (i - 1) / 2
        if (list[i] > list[parent]):
            swap(list, i, parent)
            reheapUp(list, parent)

def reheapDown(list, i, lastIndex):
    leftChild = 2 * i + 1
    rightChild = 2 * i + 2
    if (rightChild <= lastIndex):
        if (list[leftChild] > list[rightChild] and list[leftChild] > list[i]):
            swap(list, i, leftChild)
            reheapDown(list, leftChild, lastIndex)
        elif (list[leftChild] <= list[rightChild] and list[rightChild] > list[i]):
            swap(list, i, rightChild)
            reheapDown(list, rightChild, lastIndex)
    elif (leftChild <= lastIndex):
        if (list[leftChild] > list[i]):
            swap(list, i, leftChild)
            reheapDown(list, leftChild, lastIndex)

#############################################################
#################### MAIN PROGRAM ###########################
#############################################################

INITIAL_SIZE = 2 #size of list that program starts with
SIZE_MULTIPLIER = 2 #size multiplied by this each time through main while loop
PRINT_MAX = 16 #maximum size of list that is prints the values for 
SIZE_MAX = 10000000 #maximum size of list used to prevent program from taking too long
MAXRAND = 1000000 #maximum size of random integer
SORT_TIMEOUT = 4 #number of seconds sort must exceed before stopping sort
print "welcome to my sorting speed test program"
print "This program will sort a list using several sorting methods and time them."
raw_input("press enter to begin") #pause to allow time to read
do_bubbleSort = True
do_exchangeSort = True
do_heapSort = True
do_mergeSort = True
do_pythonSort = True
do_quickSort = True
do_smartBubbleSort = True
size = INITIAL_SIZE #initializes size
totalClock = time.clock() #starts clock for total run time

while (do_exchangeSort or do_bubbleSort or do_smartBubbleSort or do_mergeSort or do_quickSort or do_heapSort or do_pythonSort):
	
	arrayList = []
	initList(size, arrayList)
	listCopy = list(arrayList) #copies items in list to backup list to compare sort and reinitialize list
	print "\ncurrent size of list is:", size
	print "----------------------------------"
	
	#exchangeSort
	if do_exchangeSort: #if true do this sort
		beforeClock = time.clock() #sets time to start timer
		exchangeSort(arrayList)
		afterClock = time.clock() #sets time to end timer
		print("\nexchange sort: %.3f seconds" % (afterClock - beforeClock)) #prints time sort took
		if size <= PRINT_MAX: #will print small list to prove that it is sorting
			print "Original: %s \nSorted: %s" % (listCopy, arrayList)
		if afterClock - beforeClock > SORT_TIMEOUT: #if sort takes too long will prevent sort from running again
			do_exchangeSort = False
		arrayList = list(listCopy) #reinitialize list
	#bubbleSort
	if do_bubbleSort: #if true do this sort
		beforeClock = time.clock() #sets time to start timer
		bubbleSort(arrayList)
		afterClock = time.clock() #sets time to end timer
		print("\nbubble sort: %.3f seconds" % (afterClock - beforeClock)) #prints time sort took
		if size <= PRINT_MAX: #will print small list to prove that it is sorting
			print "Original: %s \nSorted: %s" % (listCopy, arrayList)
		if afterClock - beforeClock > SORT_TIMEOUT: #if sort takes too long will prevent sort from running again
			do_bubbleSort = False
		arrayList = list(listCopy) #reinitialize list
	#smartBubbleSort
	if do_smartBubbleSort: #if true do this sort
		beforeClock = time.clock() #sets time to start timer
		smartBubbleSort(arrayList)
		afterClock = time.clock() #sets time to end timer
		print("\nsmart bubble sort: %.3f seconds" % (afterClock - beforeClock)) #prints time sort took
		if size <= PRINT_MAX: #will print small list to prove that it is sorting
			print "Original: %s \nSorted: %s" % (listCopy, arrayList)
		if afterClock - beforeClock > SORT_TIMEOUT: #if sort takes too long will prevent sort from running again
			do_smartBubbleSort = False
		arrayList = list(listCopy) #reinitialize list
	#mergeSort
	if do_mergeSort: #if true do this sort
		beforeClock = time.clock() #sets time to start timer
		mergeSort(arrayList,0,len(arrayList)-1)
		afterClock = time.clock() #sets time to end timer
		print("\nmerge sort: %.3f seconds" % (afterClock - beforeClock)) #prints time sort took
		if size <= PRINT_MAX: #will print small list to prove that it is sorting
			print "Original: %s \nSorted: %s" % (listCopy, arrayList)
		if afterClock - beforeClock > SORT_TIMEOUT: #if sort takes too long will prevent sort from running again
			do_mergeSort = False
		arrayList = list(listCopy) #reinitialize list
	#quickSort
	if do_quickSort: #if true do this sort
		beforeClock = time.clock() #sets time to start timer
		quickSort(arrayList,0,len(arrayList)-1)
		afterClock = time.clock() #sets time to end timer
		print("\nquick sort: %.3f seconds" % (afterClock - beforeClock)) #prints time sort took
		if size <= PRINT_MAX: #will print small list to prove that it is sorting
			print "Original: %s \nSorted: %s" % (listCopy, arrayList)
		if afterClock - beforeClock > SORT_TIMEOUT: #if sort takes too long will prevent sort from running again
			do_quickSort = False
		arrayList = list(listCopy) #reinitialize list
	#heapSort
	if do_heapSort: #if true do this sort
		beforeClock = time.clock() #sets time to start timer
		heapSort(arrayList,len(arrayList))
		afterClock = time.clock() #sets time to end timer
		print("\nheap sort: %.3f seconds" % (afterClock - beforeClock)) #prints time sort took
		if size <= PRINT_MAX: #will print small list to prove that it is sorting
			print "Original: %s \nSorted: %s" % (listCopy, arrayList)
		if afterClock - beforeClock > SORT_TIMEOUT: #if sort takes too long will prevent sort from running again
			do_heapSort = False
		arrayList = list(listCopy) #reinitialize list
	#pythonSort
	if do_pythonSort: #if true do this sort
		beforeClock = time.clock() #sets time to start timer
		arrayList.sort()
		afterClock = time.clock() #sets time to end timer
		print("\npython sort: %.3f seconds" % (afterClock - beforeClock)) #prints time sort took
		if size <= PRINT_MAX: #will print small list to prove that it is sorting
			print "Original: %s \nSorted: %s" % (listCopy, arrayList)
		if afterClock - beforeClock > SORT_TIMEOUT: #if sort takes too long will prevent sort from running again
			do_pythonSort = False
		arrayList = list(listCopy) #reinitialize list
	
	if size >= SIZE_MAX: #ends while loop if list gets too large
		break
	size = size * SIZE_MULTIPLIER #increase list size
print "\ntotal time: %.3f seconds" %(time.clock()-totalClock) #prints total time sort took
raw_input("Press enter to exit") #pauses before exit