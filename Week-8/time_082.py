class Time(object):

	def __init__(self, hour=0, minute=0, second=0):
		self.hour = hour
		self.minute = minute
		self.second = second

	def __eq__(self, other):
		return (self.hour, self.minute, self.second) == (other.hour, other.minute, other.second)

	def __gt__(self, other):
		return (self.time_to_seconds() > other.time_to_seconds())

	def __add__(self, other):
		time_add = (self.time_to_seconds() + other.time_to_seconds())
		return Time.seconds_to_time(time_add)


	def __iadd__(self, other):
		time_add = self.time_to_seconds() + other.time_to_seconds()
		z = Time.seconds_to_time(time_add)
		self.hour, self.minute, self.second = z.hour, z.minute, z.second
		return self

	def __str__(self):
		return ("The time is {:02d}:{:02d}:{:02d}".format(self.hour, self.minute, self.second))

	def time_to_seconds(self):
		return ((self.hour * 3600) + (self.minute * 60) + self.second)

	def seconds_to_time(seconds):
		minutes, seconds = divmod(int(seconds), 60)
		hours, minutes = divmod(minutes, 60)
		hours = hours % 24
		
		return Time(hours, minutes, seconds)