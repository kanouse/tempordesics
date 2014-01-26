# Tempordesics

## The Tempordesic Calendar

Use the same calendar for every year. Simplify addition and subtraction of dates. 

### Notation
Format for representing Tempordesic Dates is: **[_Year_]/[_Quarter_]/[_Week_]/[_Day_]** which could also be represented in string formatting terms as **_y/q/w/d_**  

### Annual period division
- Each year is divided into four (4) even quarters:
	1. Begins on the Spring Equinox, first day: y/1/1/1
	2. Begins on the Summer Solstice, first day: y/2/1/1
	3. Begins on the Autumn Equinox, first day: y/3/1/1
	4. Begins on the Winter Solstice, first day: y/4/1/1  
- Each quarter is divided into thirteen (13) even weeks
- Each week is divided into seven (7) days
- Every year begins with a "New Year Day" which is does not fall into a week. Notation for New Year Day is y/0/0/0 (In a civil context this could be viewed as an additional day of respite between Saturday and Sunday.)
- There are leap years which add an additional day to the end of the calendar. (More below.)

### Point of reference with the Gregorian Calendar 
New Year Day (y/0/0/0) is the Spring Equinox and roughly corresponds to March 20. Year 1, day 1 of the Tempordesic Calendar (1/0/0/0) corresponds toMarch 20, 1916, which is also the day that Albert Einstein published his _General Theory of Relativity_.

### Sync Days / Leap Years
Earth orbits the Sun once every 365 + 0.2425 days. The 0.2425 add up, so we need synchronization days to maintain seasonal alignment. Traditional leap year rules apply to the Tempordesic Calendar, the leap day is added at the end of the last week of the last quarter (y/4/13/8). Sample code for leap year calculation:

	def is_leap_year(year):
		if (year % 400) == 0:
			return True
		elif (year % 100) == 0:
			return False
		elif (year % 4) == 0:
			return True
		else:
			return False


## 1.0.0.0

This happened on 1.1.1.1: [Tiempo Antico](http://victor.library.ucsb.edu/index.php/matrix/detail/700002370/C-17343-Tiempo_antico "Tiempo Antico") (meaning "Olden Times") recorded as written and performed by Enrico Caruso.