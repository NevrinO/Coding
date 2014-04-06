import datetime

print "Hello my closest, most dear and most revered friend"
print "Please, if you would be so kind, enter your birthday"
day = int(raw_input("enter day ")) # User input
valid = False #used to insure integers are within proper range
while not valid:
	if day < 1 or day > 31:
		print "You have entered an invalid answer"
		day = int(raw_input("enter day ")) # retry input of valid integer
	else:
		valid = True
month = int(raw_input("enter month "))
valid = False # reset for next while loop
while not valid:
	if month < 1 or month > 12:
		print "You have entered an invalid answer"
		month = int(raw_input("enter month ")) # retry input of valid integer
	else:
		valid = True
year = int(raw_input("enter year "))
valid = False # reset for final while loop
while not valid:
	if year < 1000 or year > 2013:
		print "You have entered an invalid answer"
		year = int(raw_input("enter year ")) # retry input of valid integer
	else:
		valid = True

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
raw_input("hit enter to continue")

