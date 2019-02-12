class Student:
    def __init__ (self, faculty, schedule, residence, status, infectionRate, infectRoom):
        self.faculty = faculty
        #Schedule used to determine what building Student is in
        self.schedule = schedule
        self.residence = residence
        #Status is infected status
        self.status = status
        #infectionRate is % chance of infecting current room
        self.infectionRate = infectionRate
        #infectRoom is a flag set if current room has been infected
        self.infectRoom = infectRoom

    #Determine population of room, length of class in hours,
    #Attempt to infect room for each hour of class (random chance based
    #on infectionRate) or until infectRoom flag is tripped.
    #If an infection occurs, infect a random amonut of students in the room
    def infect (room):
        #Random check for infection
        if (random.random() <= self.infectionRate):
            #Infect a random number of students from 0 to the room's pop'n
            #TODO: Replace room.population with real field name
            for i in range(0, random.uniform(0, room.population)):
                #TODO: Create new infected student object, will share a faculty
                #with the current student but random schedule and residence

