class Student:
	def __init__ (self, faculty, schedule, residence, infected, infectionRate, infectRoom):
		self.faculty = faculty
		#Schedule used to determine what building Student is in, TBD based on information
		#from Waterloo API
		self.schedule = schedule
		self.residence = residence
		#Infected status (true = infected, false = clean)
		self.infected = infected
		#infectionRate is % chance of infecting current room
		self.infectionRate = infectionRate
		#infectRoom is a flag set if current room has been infected
		self.infectRoom = infectRoom
	
	def infect (room):
		#Determine population of room, length of class, 
		#Attempt to infect room each hour of class (random chance based on infectionRate)
		#or until infectRoom flag is tripped
		#If an infection occurs, infect a random amount of students in the room
		if (random.random() <= self.infectionRate):
			for i in range(0, random.uniform(1, PLACEHOLDER.roomPopulation)):
				#Create new infected student object that shares a faculty
				#with the current student, but random schedule and residence
				#REPLACE PLACEHOLDER VARIABLES WITH REAL VARIABLE NAMES LATER
				Student(self.faculty, PLACEHOLDER.schedule, PLACEHOLDER.residence,
				true, self.infectionRate, false)
			self.infectRoom = true
			
