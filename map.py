# Created by: Shijin (Kevin) Yang
# Pygame GUI to display the university of waterloo, and the movement of disease

# Feb 26th, 2019 Metting
# sensitivity test required

import pygame as pg
import sys
from setup import *
from disease_source import *


class Map:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.font = pg.font.SysFont('Arial', 20)
        pg.key.set_repeat(500,100)
        self.load_data() 
        
    
    def draw_text(self):
        word_surface = self.font.render("BRH", 0, YELLOW)
        self.screen.blit(word_surface, (60,58))        
        word_surface = self.font.render("MKV", 0, YELLOW)
        self.screen.blit(word_surface, (60,305))  
        word_surface = self.font.render("TH", 0, YELLOW)
        self.screen.blit(word_surface, (50,340))   
        word_surface = self.font.render("REV", 0, YELLOW)
        self.screen.blit(word_surface, (5,348)) 
        word_surface = self.font.render("WFF", 0, YELLOW)
        self.screen.blit(word_surface, (168,168))        
        word_surface = self.font.render("CIF", 0, YELLOW)
        self.screen.blit(word_surface, (208,128))  
        word_surface = self.font.render("FED", 0, YELLOW)
        self.screen.blit(word_surface, (208,240))      
        word_surface = self.font.render("V1", 0, YELLOW)
        self.screen.blit(word_surface, (150,290))     
        word_surface = self.font.render("OPT", 0, YELLOW)
        self.screen.blit(word_surface, (357,128))   
        word_surface = self.font.render("AHS", 0, YELLOW)
        self.screen.blit(word_surface, (260,210))    
        word_surface = self.font.render("LHI", 0, YELLOW)
        self.screen.blit(word_surface, (265,230))  
        word_surface = self.font.render("BMH", 0, YELLOW)
        self.screen.blit(word_surface, (285,185))    
        word_surface = self.font.render("ERC", 0, YELLOW)
        self.screen.blit(word_surface, (330,195))   
        word_surface = self.font.render("CSB", 0, YELLOW)
        self.screen.blit(word_surface, (352,180))         
        word_surface = self.font.render("M3", 0, YELLOW)
        self.screen.blit(word_surface, (322,238))  
        word_surface = self.font.render("COM", 0, YELLOW)
        self.screen.blit(word_surface, (385,170))  
        word_surface = self.font.render("GSC", 0, YELLOW)
        self.screen.blit(word_surface, (385,210))
        word_surface = self.font.render("DC", 0, YELLOW)
        self.screen.blit(word_surface, (398,268))      
        word_surface = self.font.render("C2", 0, YELLOW)
        self.screen.blit(word_surface, (378,282)) 
        word_surface = self.font.render("MC", 0, YELLOW)
        self.screen.blit(word_surface, (345,275))         
        word_surface = self.font.render("UC", 0, YELLOW)
        self.screen.blit(word_surface, (260,250))        
        word_surface = self.font.render("PAC", 0, YELLOW)
        self.screen.blit(word_surface, (285,255))  
        word_surface = self.font.render("SLC", 0, YELLOW)
        self.screen.blit(word_surface, (305,287))        
        word_surface = self.font.render("QNC", 0, YELLOW)
        self.screen.blit(word_surface, (315,330)) 
        word_surface = self.font.render("B2", 0, YELLOW)
        self.screen.blit(word_surface, (325,350))
        word_surface = self.font.render("STC", 0, YELLOW)
        self.screen.blit(word_surface, (335,370)) 
        word_surface = self.font.render("B1", 0, YELLOW)
        self.screen.blit(word_surface, (392,360))      
        word_surface = self.font.render("ESC", 0, YELLOW)
        self.screen.blit(word_surface, (395,315))     
        word_surface = self.font.render("EIT", 0, YELLOW)
        self.screen.blit(word_surface, (430,315))      
        word_surface = self.font.render("E3", 0, YELLOW)
        self.screen.blit(word_surface, (470,315))         
        word_surface = self.font.render("NH", 0, YELLOW)
        self.screen.blit(word_surface, (327,405))  
        word_surface = self.font.render("PHY", 0, YELLOW)
        self.screen.blit(word_surface, (460,365))        
        word_surface = self.font.render("HS", 0, YELLOW)
        self.screen.blit(word_surface, (260,365))      
        word_surface = self.font.render("REN", 0, YELLOW)
        self.screen.blit(word_surface, (235,435)) 
        word_surface = self.font.render("STJ", 0, YELLOW)
        self.screen.blit(word_surface, (262,445)) 
        word_surface = self.font.render("STP", 0, YELLOW)
        self.screen.blit(word_surface, (275,490))
        word_surface = self.font.render("CGR", 0, YELLOW)
        self.screen.blit(word_surface, (275,530))        
        word_surface = self.font.render("EC3", 0, YELLOW)
        self.screen.blit(word_surface, (485,132))    
        word_surface = self.font.render("EC2", 0, YELLOW)
        self.screen.blit(word_surface, (490,187))        
        word_surface = self.font.render("EC1", 0, YELLOW)
        self.screen.blit(word_surface, (555,123))
        word_surface = self.font.render("EC5", 0, YELLOW)
        self.screen.blit(word_surface, (543,147))  
        word_surface = self.font.render("EC4", 0, YELLOW)
        self.screen.blit(word_surface, (555,187))     
        word_surface = self.font.render("E5", 0, YELLOW)
        self.screen.blit(word_surface, (500,268))        
        word_surface = self.font.render("E7", 0, YELLOW)
        self.screen.blit(word_surface, (530,305))
        word_surface = self.font.render("E6", 0, YELLOW)
        self.screen.blit(word_surface, (555,268))  
        word_surface = self.font.render("ECH", 0, YELLOW)
        self.screen.blit(word_surface, (595,260))       
        word_surface = self.font.render("EV3", 0, YELLOW)
        self.screen.blit(word_surface, (355,530)) 
        word_surface = self.font.render("EV2", 0, YELLOW)
        self.screen.blit(word_surface, (365,550)) 
        word_surface = self.font.render("EV1", 0, YELLOW)
        self.screen.blit(word_surface, (425,530))         
        word_surface = self.font.render("PAS", 0, YELLOW)
        self.screen.blit(word_surface, (385,580))    
        word_surface = self.font.render("HH", 0, YELLOW)
        self.screen.blit(word_surface, (427,550))     
        word_surface = self.font.render("LIB", 0, YELLOW)
        self.screen.blit(word_surface, (415,425)) 
        word_surface = self.font.render("AL", 0, YELLOW)
        self.screen.blit(word_surface, (425,475))        
        word_surface = self.font.render("TC", 0, YELLOW)
        self.screen.blit(word_surface, (455,475))        
        word_surface = self.font.render("ML", 0, YELLOW)
        self.screen.blit(word_surface, (365,475))
        word_surface = self.font.render("SCH", 0, YELLOW)
        self.screen.blit(word_surface, (510,475)) 
        word_surface = self.font.render("GH", 0, YELLOW)
        self.screen.blit(word_surface, (465,427))   
        word_surface = self.font.render("RCH", 0, YELLOW)
        self.screen.blit(word_surface, (485,403))        
        word_surface = self.font.render("E2", 0, YELLOW)
        self.screen.blit(word_surface, (525,375)) 
        word_surface = self.font.render("DWE", 0, YELLOW)
        self.screen.blit(word_surface, (540,460))   
        word_surface = self.font.render("SCH", 0, YELLOW)
        self.screen.blit(word_surface, (565,380))  
        word_surface = self.font.render("CPH", 0, YELLOW)
        self.screen.blit(word_surface, (668,420))  
        word_surface = self.font.render("UWP", 0, YELLOW)
        self.screen.blit(word_surface, (715,420))        
        
        
    def draw_campus_map(self):
        for x in range(10,11):
            for y in range(5,6):
                Building(self, x, y, "BRH", 0, {})
        for x in range(7,8):
            for y in range(40,41):
                Building(self, x, y, "MKV", 76, {})
        for x in range(6,7):
            for y in range(44,45):
                Building(self, x, y, "TH", 0, {})
        for x in range(0,1):
            for y in range(45,46):
                Building(self, x, y, "REV", 187, {}) 
        for x in range(18,19):
            for y in range(38,39):
                Building(self, x, y, "V1", 360, {})
        for x in range(28,29):
            for y in range(28,29):
                Building(self, x, y, "FED", 0, {})
        for x in range(19,20):
            for y in range(19,20):
                Building(self, x, y, "WFF", 0, {})
        for x in range(29,30):
            for y in range(15,16):
                Building(self, x, y, "CIF", 0, {})
        for x in range(32,33):
            for y in range(33,34):
                Building(self, x, y, "UC", 0, {})
        for x in range(36,37):
            for y in range(34,35):
                Building(self, x, y, "PAC", 61,
                         {"BET 100": 193, "GBDA 101": 57})
        for x in range(39,40):
            for y in range(38,39):
                Building(self, x, y, "SLC", 0, {})
        for x in range(43,44):
            for y in range(41,42):
                Building(self, x, y, "QNC", 144,
                         {"ARTS 140", 587})
        for x in range(44,45):
            for y in range(36,37):
                Building(self, x, y, "MC", 552,
                         {"CS 105": 224, "CS 137": 122, "EARTH 123": 125,
                          "MATH 128": 107, "MATH 135": 1500, "MATH 136": 179})
        for x in range(43,44):
            for y in range(29,30):
                Building(self, x, y, "M3", 613,
                         {"CHEM 120": 1909, "EARTH 121": 265,
                          "GEOG 101": 329})
        for x in range(42,43):
            for y in range(26,27):
                Building(self, x, y, "ERC", 0, {})
        for x in range(39,40):
            for y in range(25,26):
                Building(self, x, y, "BMH", 102,
                         {"HLTH 101": 417})
        for x in range(36,37):
            for y in range(26,27):
                Building(self, x, y, "AHS", 408,
                         {"AHS 107": 757, "CHEM 100":78, "KIN 104": 291,
                          "MATH 124": 293, "REC 100": 247})
        for x in range(36,37):
            for y in range(29,30):
                Building(self, x, y, "LHI", 0, {})
        for x in range(45,46):
            for y in range(25,26):
                Building(self, x, y, "CSB", 0, {})
        for x in range(48,49):
            for y in range(23,24):
                Building(self, x, y, "COM", 0, {})
        for x in range(48,49):
            for y in range(28,29):
                Building(self, x, y, "GSC", 0, {})
        for x in range(50,51):
            for y in range(35,36):
                Building(self, x, y, "DC", 235,
                         {"AFM 131":818, "GEOG 181": 143})
        for x in range(47,48):
            for y in range(37,38):
                Building(self, x, y, "C2", 0, {})
        for x in range(48,49):
            for y in range(41,42):
                Building(self, x, y, "ESC", 0, {})
        for x in range(53,54):
            for y in range(41,42):
                Building(self, x, y, "EIT", 300,
                         {"CIVE 104": 226, "MATH 116": 999})
        for x in range(47,48):
            for y in range(45,46):
                Building(self, x, y, "B1", 569,
                         {"MATH 137": 1560, "PHYS 111": 764})
        for x in range(45,46):
            for y in range(46,47):
                Building(self, x, y, "STC", 390,
                         {"BIOL 130": 1455, "REC 120": 139})
        for x in range(43,44):
            for y in range(44,45):
                Building(self, x, y, "B2", 0, {})
        for x in range(43,44):
            for y in range(50,51):
                Building(self, x, y, "NH", 0, {})
        for x in range(52,53):
            for y in range(55,56):
                Building(self, x, y, "LIB", 0, {})
        for x in range(48,49):
            for y in range(60,61):
                Building(self, x, y, "ML", 111,
                         {"ARTS 130": 433, "ENGL 191": 19})
        for x in range(51,52):
            for y in range(65,66):
                Building(self, x, y, "EV1", 0, {})
        for x in range(48,49):
            for y in range(66,67):
                Building(self, x, y, "EV3", 216,
                         {"ENBUS 102": 126, "ENGL 109": 550,
                          "ERS 100": 206})
        for x in range(49,50):
            for y in range(68,69):
                Building(self, x, y, "EV2", 21,
                         {"GEOG 100": 34, "INTEG 120": 52})
        for x in range(52,53):
            for y in range(73,74):
                Building(self, x, y, "PAS", 287,
                         {"PSYCH 101": 1173})
        for x in range(54,55):
            for y in range(61,62):
                Building(self, x, y, "AL", 108,
                         {"ARBUS 101": 403, "CLAS 104": 38})
        for x in range(57,58):
            for y in range(61,62):
                Building(self, x, y, "TC", 0, {})
        for x in range(56,57):
            for y in range(69,70):
                Building(self, x, y, "HH", 219, 
                         {"AFM 101": 789, "ENGL 193": 103})
        for x in range(61,62):
            for y in range(59,60):
                Building(self, x, y, "SCH", 0, {})
        for x in range(59,60):
            for y in range(55,56):
                Building(self, x, y, "GH", 0, {})
        for x in range(61,62):
            for y in range(52,53):
                Building(self, x, y, "RCH", 754,
                         {"CHE 100": 154, "ENVS 178": 245, "ENVS 195": 289,
                          "MATH 115": 1195, "PHYS 121": 543, "SPCOM 111": 64,
                          "SPCOM 223": 590})
        for x in range(67,68):
            for y in range(55,56):
                Building(self, x, y, "DWE", 252,
                         {"CHE 180": 64, "MATH 127": 964})
        for x in range(70,71):
            for y in range(50,51):
                Building(self, x, y, "CPH", 22,
                         {"ENVE 100": 88})
        for x in range(65,66):
            for y in range(49,50):
                Building(self, x, y, "E2", 223,
                         {"CS 135": 912})
        for x in range(57,58):
            for y in range(47,48):
                Building(self, x, y, "PHY", 208,
                         {"CS 115": 849})
        for x in range(58,59):
            for y in range(41,42):
                Building(self, x, y, "E3", 0, {})
        for x in range(65,66):
            for y in range(35,36):
                Building(self, x, y, "E5", 0, {})
        for x in range(67,68):
            for y in range(36,37):
                Building(self, x, y, "E7", 543,
                         {"CHE 102": 1121, "ECE 105": 499, "MATH 117": 596})
        for x in range(71,72):
            for y in range(35,36):
                Building(self, x, y, "E6", 0, {})
        for x in range(72,73):
            for y in range(32,33):
                Building(self, x, y, "ECH", 0, {})
        for x in range(71,72):
            for y in range(25,26):
                Building(self, x, y, "EC4", 0, {})
        for x in range(62,63):
            for y in range(25,26):
                Building(self, x, y, "EC2", 0, {})
        for x in range(61,62):
            for y in range(19,20):
                Building(self, x, y, "EC3", 0, {})
        for x in range(71,72):
            for y in range(17,18):
                Building(self, x, y, "EC1", 0, {})
        for x in range(69,70):
            for y in range(20,21):
                Building(self, x, y, "EC5", 0, {})
        for x in range(42,43):
            for y in range(14,15):
                Building(self, x, y, "OPT", 43,
                         {"REC 101": 175})
        for x in range(35,36):
            for y in range(47,48):
                Building(self, x, y, "HS", 0, {})
        for x in range(36,37):
            for y in range(55,56):
                Building(self, x, y, "STJ", 76, {})
        for x in range(29,30):
            for y in range(56,57):
                Building(self, x, y, "REN", 45, {})
        for x in range(32,33):
            for y in range(62,63):
                Building(self, x, y, "STP", 559,
                         {"ECON 101": 1934, "ENVS 105": 192,
                          "INDEV 100": 155})
        for x in range(36,37):
            for y in range(68,69):
                Building(self, x, y, "CGR", 0, {})
        for x in range(84,85):
            for y in range(54,55):
                Building(self, x, y, "CMH", 132)
        for x in range(87,88):
            for y in range(52,53):
                Building(self, x, y, "UWP", 428)                
                
    
    def load_data(self):
        pass
    
    def new(self):
        # initialize all variables and do all the setup for a new game
        self.all_sprites = pg.sprite.Group()
        self.buildings = pg.sprite.Group()
        self.disease = Disease(self)
        self.draw_campus_map()
    
    def run(self):
        # game loop - set self.playing = False to end the game
        self.playing = True
        while self.playing:
            #self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()
            
    def quit(self):
        pg.quit()
        sys.exit()
        
    def update(self):
        self.all_sprites.update()
        
    def draw_path(self):
        for i in range(len(self.disease.building_that_pass_through) - 1):
            head_building_index = self.disease.building_that_pass_through[i]
            tail_building_index = self.disease.building_that_pass_through[i+1]
            head_building = None
            tail_building = None
            for b_object in self.buildings:
                if head_building_index == b_object.name:
                    head_building = b_object
                if tail_building_index == b_object.name:
                    tail_building = b_object
            pg.draw.line(self.screen, RED, (head_building.x * TILESIZE, head_building.y * TILESIZE), 
                         (tail_building.x * TILESIZE, tail_building.y * TILESIZE), 2)
    
    # get the color for drawing the Map using:
    # print(self.screen.get_at((self.disease.x,self.disease.y)))
    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (0,y), (WIDTH, y))
            
    def draw(self):
        self.screen.fill(BGCOLOR)
        self.draw_grid()
        self.draw_text()
        self.draw_path()
        self.all_sprites.draw(self.screen)
        pg.display.flip()
        
    
    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()
                '''
                if event.key == pg.K_LEFT:
                    self.disease.move(dx=-1)
                if event.key == pg.K_RIGHT:
                    self.disease.move(dx=1)
                if event.key == pg.K_UP:
                    self.disease.move(dy=-1)
                if event.key == pg.K_DOWN:
                    self.disease.move(dy=1)   
                '''
                if event.key == pg.K_RETURN:
                    self.disease.disease_spreading()
    
    def show_start_screen(self):
        pass
    
    def show_go_screen(self):
        pass
    
g = Map()
g.show_start_screen()
while True:
    g.new()
    g.run()
    g.show_go_screen()
