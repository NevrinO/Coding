import datetime

print "Hello my closest, most dear and most revered friend"
print "Please, if you would be so kind, enter your birthday"
valid = False #We start with no value for 'day' at all, so that's certainly not valid
while not valid: #while we don't have a valid day:
	try:
		day = int(raw_input("enter the day: "))
		if day < 1 or day > 31:
			print "You have entered an invalid answer, please try again"
		else:
			valid = True
	except:
		print "You must enter an int"
	
 
valid = False # reset for next while loop
while not valid:
	try:
		month = int(raw_input("enter month ")) # retry input of valid integer
		if month < 1 or month > 12:
			print "You have entered an invalid answer"
		else:
			valid = True
 	except:
		print "You must enter an int"
		

valid = False # reset for final while loop
while not valid:
	try:
		year = int(raw_input("enter year ")) # retry input of valid integer
		if year < 1000 or year > 2013:
			print "You have entered an invalid answer"
		else:
			valid = True
	except:
		print "You must enter an int"


current = datetime.date.today() # gets current date from imported datetime 
print ("\nYour Birthday is: %s/%s/%s" % (day, month, year)) # prints info user entered
print ("\nThe Current date is: %s/%s/%s" % (current.day, current.month, current.year) )  # prints current date from datetime
raw_input("hit enter to continue")
weekday ={ # dictionary of days of week
	0: 'Monday',
	1: 'Tuesday',
	2: 'Wednesday',
	3: 'Thursday',
	4: 'Friday',
	5: 'Saturday',
	6: 'Sunday',
	}
bDate = datetime.date(year, month, day) # converts user data to datetime object
leapYear = int((current.year - bDate.year) / 4) # determine number of days added by leap years 
deltaDays = (current - bDate) # difference in days between current date and bDate
dStrip = str(deltaDays).split() # converts days into string format and splits off unnecessary data
daysLeft = int(dStrip[0]) # gathers just the days number and convert to int from sting
mYear = daysLeft / 365 # Calculate years alive
daysLeft = daysLeft - (mYear * 365) # removes year part of days
mMonth = daysLeft / 30 # calculate months alive
mDay = daysLeft - (mMonth * 30) - 7 # Calculate days alive
if mDay < 0: # fix small discrepancy created with certain date combos 
	mMonth = mMonth - 1
	if mMonth < 0:
		mMonth = 11 # Plan on changing entire calculating section because sometimes it is still a day or two off.
	mDay = mDay + 30
print "You were born on a %s: " % (weekday[bDate.weekday()])
print "you have been alive for about %s seconds" % (deltaDays.total_seconds())
print ("\nYou are %s years %s months %s days old" % (mYear, mMonth, mDay))
if mYear > 122:
	print "You should call Guinness World Records cause it looks like you can give Jeanne Louise Calment a run for her money, She was born on 21 February 1875."
	if year == 1875 and month == 02 and day == 21:
		print "Oh never mind it looks like you are Jeanne Louise Calment."
raw_input("hit enter to continue")

