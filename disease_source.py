# version
import pygame as pg
from setup import *
import numpy as np
import pandas as pd

class Disease(pg.sprite.Sprite):
    def __init__(self, game):
        # basic properties of disease object
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(DARKGREY)
        self.rect = self.image.get_rect()
        # disease location - random initialization
        #x_range = WIDTH // TILESIZE // 2
        #y_range = HEIGHT // TILESIZE // 2
        #self.x = np.random.randint(1,x_range)
        #self.y = np.random.randint(1,y_range)
        
        # disease infection rate based on faculty
        #self.disease_source_faculty = np.random.choice(list(faculty.keys()))
        self.disease_source_faculty = "ENG 1"
        self.infection_rate = faculty[self.disease_source_faculty]
        print("faculty {} has infection rate {}\n".format(self.disease_source_faculty, self.infection_rate))
        self.building_that_pass_through = []
        # print("disease might start spreading from {}\n".format(faculty_to_building[self.disease_source_faculty]))
        # disease recovery rate - change based on the portion of susceptible people
        self.recovery_rate = [0, 0.05, 0.1, 0.2, 0.4, 0.6, 0.7, 0.8, 0.95]
        
    
    def move(self, dx=0, dy=0):  
        #if not self.touch_with_building(dx,dy):
        #self.disease_spreading()
        #self.x += dx
        #self.y += dy
        pass
    
    def calculate_infection_number(self, _infection_rate, population):
        return int(_infection_rate * population)
    
    def calculate_susceptible_number(self, ss_population, if_population):
        return int(ss_population - if_population)
    
    def disease_spreading(self):
        spread_tree = faculty_to_building[self.disease_source_faculty]
        print("disease might start spreading from {}\n".format(faculty_to_building[self.disease_source_faculty]))
        buildings_in_this_cycle = []
        for building in spread_tree:
            infec_range = len(building_to_faculty[building])
            temp_risk_buildings = faculty_to_building[building_to_faculty[building][np.random.choice(infec_range)]]
            for buil in temp_risk_buildings:
                buildings_in_this_cycle.append(buil)
        buildings_in_this_cycle = list(set(buildings_in_this_cycle))
        print("buildings that might be affected in this duration: ", buildings_in_this_cycle)
        
        # Assume there are 3 sections in a day, total 5 cycles in a week - 5 courses
        # because we don't know how the course is actually arranged
        
        _all_cycle_df = []
        _infection_rate_through_section = []
        _number_of_infection_section = []
        _number_of_susceptible_section = []
        infected_student_after_infected_this_section = 0
        susceptible_student_after_infected_this_section = 8244
        # control the number of week
        for week in range(0,2):
            cycle = 5
            while cycle > 0:
                _df = []
                sections = 4 # three or less buildings will be accessed
                while sections > 0:
                    risk_building = np.random.choice(buildings_in_this_cycle, 3)
                    risk_resident = np.random.choice(["MKV", "REN", "STJ", "UWP", "V1", "REV"])
                    risk_building = np.append(risk_building, risk_resident)
                    print("risk buildings: ", risk_building)
                    # get susceptible faculties in the risk buildings
                    susceptible_faculties = []
                    for building in risk_building:
                        self.building_that_pass_through.append(building)
                        temp_susceptible_faculties = building_to_faculty[building]
                        for _faculty in temp_susceptible_faculties:
                            susceptible_faculties.append(_faculty)
                        susceptible_faculties = list(set(susceptible_faculties))
                        print("in building ", building, "susceptible_faculties are ", susceptible_faculties)
                        faculty_infection_situ = {}
                        for _faculty in susceptible_faculties:
                            # for each susceptible faculty
                            # assume 0 - 5% of people in that faculty is being contacted by the source of disease
                            _chance = np.random.randint(0,5)
                            # convert to probability
                            _p = _chance / 100
                            #print("chance of contact: ", _p)
                            
                            # after calcualting all the possible infection in each faculty,
                            # get the summation of the number of infected student, store in that risk building
                            # based on the number of susceptible students in this building
                            
                            for game_building in self.game.buildings:
                                if game_building.name == building:
                                    # re-calculate number of infected student
                                    game_building.student_infected_at_this_time = \
                                        self.calculate_infection_number(_p, game_building.status_of_student_in_building['susceptible'])
                                    
                                    #print("student are infected at this time: ", game_building.student_infected_at_this_time)
                                    
                                    game_building.status_of_student_in_building['infected'] += game_building.student_infected_at_this_time
                                    
                                    #print("number of students were infected: "+\
                                    #      str(game_building.status_of_student_in_building['infected'])+"\n")  
                                    
                                    # re-calculate number of susceptible student
                                    
                                    game_building.change_building_status()
                                    
                                    game_building.status_of_student_in_building['susceptible'] = \
                                        self.calculate_susceptible_number(game_building.status_of_student_in_building['susceptible'],
                                                                     game_building.student_infected_at_this_time)
                                    
                                    #print("number of students were susceptible: "+\
                                    #      str(game_building.status_of_student_in_building['susceptible'])+"\n")    
                                    
                                    faculty_infection_situ[_faculty] = game_building.student_infected_at_this_time
                        faculty_infection_situ['building'] = building
                        print(faculty_infection_situ)
                        #_df.append(faculty_infection_situ)
                        _all_cycle_df.append(faculty_infection_situ)
                        # calculate portion of infected students at this section
                        infection_at_this_section = 0
                        
                        for situ in faculty_infection_situ.keys():
                            if type(faculty_infection_situ[situ]) == int:
                                infection_at_this_section += faculty_infection_situ[situ]
                        
                        susceptible_student_after_infected_this_section -= infection_at_this_section
                        infected_student_after_infected_this_section += infection_at_this_section
                            
                        print("number of infected students in this section: ", infection_at_this_section, "\n")
                        #calculate infection rate - total population 8244
                        infection_rate_at_this_section = infection_at_this_section / 8244
                        
                        #_number_of_infection_section.append(infection_at_this_section)
                        #_number_of_susceptible_section.append(susceptible_student_after_infected_this_section)  
                        
                        _infection_rate_through_section.append({"infection_rate": infection_rate_at_this_section,
                                                                "number_of_infection": infected_student_after_infected_this_section,
                                                                "number_of_susceptible": susceptible_student_after_infected_this_section,
                                                                "building": building})
                        
                        
                        sections -= 1
                       
            
                        
                #_all_cycle_df.append(_df)
                cycle -= 1
        #peak_infection_section = np.argmax(_infection_rate_through_section)
        #print("peak infection section: ", peak_infection_section + 1, "\n")
        #print("peak infection rate: ", _infection_rate_through_section[peak_infection_section], "\n") 
        '''
        for i in range(len(self.building_that_pass_through) - 1):
            head_building_index = self.building_that_pass_through[i]
            tail_building_index = self.building_that_pass_through[i+1]
            head_building = None
            tail_building = None
            for b_object in self.game.buildings:
                if head_building_index == b_object.name:
                    head_building = b_object
                if tail_building_index == b_object.name:
                    tail_building = b_object
            print(head_building,tail_building)
            pg.draw.line(self.game.screen, RED, (head_building.x * TILESIZE, head_building.y * TILESIZE), 
                         (tail_building.x * TILESIZE, tail_building.y * TILESIZE), 2)
        '''
        print("path: ", self.building_that_pass_through)
        _report = pd.DataFrame(_all_cycle_df)
        _report.to_csv(r'/Users/shijinyang/Desktop/disease_csv.csv', index=False)
        _report_rate = pd.DataFrame(_infection_rate_through_section)
        _report_rate.to_csv(r'/Users/shijinyang/Desktop/infection_rate.csv', index=False)
        '''
        _num_of_student_lst = {}
        for game_building in self.game.buildings:
            _num_of_student_lst[game_building.name] = [game_building.num_of_students]
        _num_student_df = pd.DataFrame.from_dict(_num_of_student_lst)
        _num_student_df.to_csv(r'/Users/shijinyang/Desktop/numstudent.csv', index=False)
        '''
        
    
    
    def update(self):
        #self.rect.x = self.x * TILESIZE
        #self.rect.y = self.y * TILESIZE
        pass
    
        
class Building(pg.sprite.Sprite):
    def __init__(self, game, x, y, name, num_of_students, class_hold_in_building={}):
        # basic properties of buildings
        self.groups = game.all_sprites, game.buildings
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        # name of the building
        self.name = name
        # building size on the map
        self.image = pg.Surface((TILESIZE, TILESIZE))
        # status of student in the building
        self.num_of_students = num_of_students        
        # building color
        if self.num_of_students != 0:
            self.image.fill(GREEN)
        else:
            self.image.fill(WHITE)
        
        # building rectangle object
        self.rect = self.image.get_rect()
        # building location
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
        
        # store infection rate
        self.student_infected_at_this_time = 0
        
        # the dictionary include class as key, and num_student_in_class as val
        self.class_hold_in_building = class_hold_in_building
        # the status of students in the buildings
        # key - status
        # val - the number of students
        self.status_of_student_in_building = {"susceptible": self.num_of_students,
                                              "infected": 0,
                                              "recovered": 0}
        
        # calculate infection rate in the building
    def cal_infection_portion(self):
        infection_portion = 0
        if self.num_of_students != 0:
            infection_portion = self.status_of_student_in_building['infected'] / self.num_of_students
            #print("portion of infection: {}".format(infection_portion))
        return infection_portion
        
    def cal_susceptible_portion(self):
        susceptible_portion = 0
        if self.num_of_students != 0:
            susceptible_portion = self.status_of_student_in_building['susceptible'] / self.num_of_students
        return susceptible_portion
        
    def change_building_status(self):
        portion = self.cal_infection_portion()
        if portion < 0.2:
            self.image.fill(GREEN)
        elif 0.2 <= portion < 0.5:
            self.image.fill(DARK_YELLOW)
        elif 0.5 <= portion < 0.8:
            self.image.fill(ORANGE)
        elif portion >= 0.8:
            self.image.fill(RED)
                
                
                
            
        
        

        