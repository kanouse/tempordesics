from datetime import date, datetime, timedelta

class TDate:

	gday0 	= datetime(1, 3, 19) # the day before day 1

	quarter_names 	= ['Boreal', 'Perigee', 'Austral', 'Apogee']
	day_names 		= ['Sunday', 'Monday', 'Tuesday', 'Wednesday',
						'Thursday', 'Friday', 'Saturday']

	year 	= 1
	quarter = 0
	week 	= 0
	day 	= 0

	def __init__(self, *args):	
		if len(args) == 4:
			self.year 		= args[0]
			self.quarter 	= args[1]
			self.week 		= args[2]
			self.day 		= args[3]
			self.validate()
		elif len(args) > 0:
			raise Exception("Invalid date values. Required: year, quarter, week, day.")


	def __str__(self):
		str_date = 	str(self.year) + '/'
		str_date += str(self.quarter) + '/'
		str_date += str(self.week) + '/'
		str_date += str(self.day)
		return str_date


	def day_of_year(self):
		"""Returns day number, including today
		"""
		days_into_year = 1 # new years day
		if not self.is_newyears_day():
			days_into_year += ((self.quarter - 1) * 91)
			days_into_year += ((self.week - 1) * 7)
			days_into_year += self.day
		return days_into_year


	def days_in_year(self):
		"""Returns number of days in current object year.
		Includes consideration for leap years.
		"""
		if self.is_leap_year(): 
			return 366
		else: 
			return 365


	def days_in_year_remaining(self):		
		days_remaining = 365 - self.day_of_year()
		if self.is_leap_year():
			days_remaining += 1
		return days_remaining


	def add_days(self, days):
		"""
		Currently only works for positive day values.
		"""

		# set days to represent total days from the previous NYD
		days += (self.day_of_year())

		# knock out the 400 year cycles first...
		while (days > 146097):
			self.year += 400
			days -= 146097

		# advance to the right year...		
		while (days > self.days_in_year()):	
			self.year += 1
			days -= self.days_in_year()

		# days into current year is the remainder
		if (days == 1):
			# it's new years day
			self.quarter 	= 0
			self.week 		= 0
			self.day 		= 0

		else:
			self.quarter 	= 1
			self.week 		= 1
			self.day 		= 1

			# we accounted for new years day above
			days -= 1 # days remaining
			
			# iterate through calendar
			while (days > 0):
				if (days > 91):
					self.quarter += 1
					days -= 91
				elif (days > 7):
					self.week += 1
					days -= 7
				else:
					self.day = days
					days = 0

		# adjust for if new year's day
		if (self.quarter == 5):
			self.quarter 	= 4
			self.week 		= 13
			self.day 		= 8
		pass


	def from_gdate(self, date):
		"""Returns TDate object with today's date.
		"""
		diff = date - self.gday0
		self.reset()
		self.add_days(diff.days) 
		return self


	def today(self):
		"""Returns TDate object with today's date.
		"""
		now = datetime.utcnow()
		diff = now - self.gday0
		self.reset()
		self.add_days(diff.days) 
		return self


	def verbose(self):
		"""Returns long form version of the date.
		"""
		vdate = self.quarter_names[self.quarter - 1] + ' ' + str(self.year) + ', '
		vdate += self.day_names[self.day - 1] + ' ' + str(self.week)
		return vdate


	def reset(self):
		"""Sets object date to Day One
		"""
		self.year 		= 1
		self.quarter 	= 0
		self.week 		= 0
		self.day 		= 0


	def quarter_name(self, quarter = None):
		if not quarter:
			quarter = self.quarter
		return self.quarter_names[quarter - 1]


	def is_leap_year(self, year = None):
		"""Determines if current object year is a leap year.
		"""
		eval_year = self.year
		if (year):
			eval_year = year

		if (eval_year % 400) == 0:
			return True
		elif (eval_year % 100) == 0:
			return False
		elif (eval_year % 4) == 0:
			return True
		else:
			return False

	def is_newyears_day(self):
		"""Detrmines if current object date is New Year's Day.
		"""
		return (self.quarter + self.week + self.day) == 0


	def validate(self):
		"""Detrmines if date parts are within valid date ranges for TDate type.
		"""
		if (self.quarter < 0) or (self.quarter > 4):
			raise Exception("Invalid value for Quarter")
		if (self.week < 0) or (self.week > 13):
			raise Exception("Invalid value for Week")
		if (self.day < 0) or (self.day > 7):
			if (self.day == 8) and (self.week == 13) and (self.quarter == 4):
				if not self.is_leap_year:
					raise Exception("Invalid value for Day")
			else:
				raise Exception("Invalid value for Day")
		if ((self.quarter * self.week * self.day) == 0) and ((self.quarter + self.week + self.day) != 0):
			raise Exception("Invalid tdate")



