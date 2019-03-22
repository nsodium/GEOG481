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
        self.screen.blit(word_surface, (397,360))      
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
        word_surface = self.font.render("RCG", 0, YELLOW)
        self.screen.blit(word_surface, (485,403))        
        word_surface = self.font.render("E2", 0, YELLOW)
        self.screen.blit(word_surface, (525,375)) 
        word_surface = self.font.render("DWE", 0, YELLOW)
        self.screen.blit(word_surface, (540,460))   
        word_surface = self.font.render("CPH", 0, YELLOW)
        self.screen.blit(word_surface, (565,380))  
        word_surface = self.font.render("CPH", 0, YELLOW)
        self.screen.blit(word_surface, (668,420))  
        word_surface = self.font.render("UWP", 0, YELLOW)
        self.screen.blit(word_surface, (715,420))        
        
        
    def draw_campus_map(self):
        for x in range(10,12):
            for y in range(5,7):
                Building(self, x, y, "BRH")
        for x in range(7,9):
            for y in range(40,42):
                Building(self, x, y, "MKV")
        for x in range(6,8):
            for y in range(44,46):
                Building(self, x, y, "TH")
        for x in range(0,2):
            for y in range(45,47):
                Building(self, x, y, "REV") 
        for x in range(18,20):
            for y in range(38,40):
                Building(self, x, y, "V1")
        for x in range(28,30):
            for y in range(28,30):
                Building(self, x, y, "FED")
        for x in range(19,21):
            for y in range(19,21):
                Building(self, x, y, "WFF")
        for x in range(29,31):
            for y in range(15,17):
                Building(self, x, y, "CIF")
        for x in range(32,34):
            for y in range(33,35):
                Building(self, x, y, "UC")
        for x in range(36,38):
            for y in range(34,36):
                Building(self, x, y, "PAC")
        for x in range(39,41):
            for y in range(38,40):
                Building(self, x, y, "SLC")
        for x in range(43,45):
            for y in range(41,43):
                Building(self, x, y, "QNC")
        for x in range(44,46):
            for y in range(36,38):
                Building(self, x, y, "MC")
        for x in range(43,45):
            for y in range(29,31):
                Building(self, x, y, "M3")
        for x in range(42,44):
            for y in range(26,28):
                Building(self, x, y, "ERC")
        for x in range(39,41):
            for y in range(25,27):
                Building(self, x, y, "BMH")
        for x in range(36,38):
            for y in range(26,28):
                Building(self, x, y, "AHS")
        for x in range(36,38):
            for y in range(29,31):
                Building(self, x, y, "LHI")
        for x in range(45,47):
            for y in range(25,27):
                Building(self, x, y, "CSB")
        for x in range(48,50):
            for y in range(23,25):
                Building(self, x, y, "COM")
        for x in range(48,50):
            for y in range(28,30):
                Building(self, x, y, "GSC")
        for x in range(50,52):
            for y in range(35,37):
                Building(self, x, y, "DC")
        for x in range(47,49):
            for y in range(37,39):
                Building(self, x, y, "C2")
        for x in range(48,50):
            for y in range(41,43):
                Building(self, x, y, "ESC")
        for x in range(53,55):
            for y in range(41,43):
                Building(self, x, y, "EIT")
        for x in range(47,49):
            for y in range(45,47):
                Building(self, x, y, "B1")
        for x in range(45,47):
            for y in range(46,48):
                Building(self, x, y, "STC")
        for x in range(43,45):
            for y in range(44,46):
                Building(self, x, y, "B2")
        for x in range(43,45):
            for y in range(50,52):
                Building(self, x, y, "NH")
        for x in range(52,54):
            for y in range(55,57):
                Building(self, x, y, "LIB")
        for x in range(48,50):
            for y in range(60,62):
                Building(self, x, y, "ML")
        for x in range(51,53):
            for y in range(65,67):
                Building(self, x, y, "EV1")
        for x in range(48,50):
            for y in range(66,68):
                Building(self, x, y, "EV3")
        for x in range(49,51):
            for y in range(68,70):
                Building(self, x, y, "EV2")
        for x in range(52,54):
            for y in range(73,75):
                Building(self, x, y, "PAS")
        for x in range(54,56):
            for y in range(61,63):
                Building(self, x, y, "AL")
        for x in range(57,59):
            for y in range(61,63):
                Building(self, x, y, "TC")
        for x in range(56,58):
            for y in range(69,71):
                Building(self, x, y, "HH")
        for x in range(61,63):
            for y in range(59,61):
                Building(self, x, y, "SCH")
        for x in range(59,61):
            for y in range(55,57):
                Building(self, x, y, "GH")
        for x in range(61,63):
            for y in range(52,54):
                Building(self, x, y, "RCH")
        for x in range(67,69):
            for y in range(55,57):
                Building(self, x, y, "DWE")
        for x in range(70,72):
            for y in range(50,52):
                Building(self, x, y, "CPH")
        for x in range(65,67):
            for y in range(49,51):
                Building(self, x, y, "E2")
        for x in range(57,59):
            for y in range(47,49):
                Building(self, x, y, "PHY")
        for x in range(58,60):
            for y in range(41,43):
                Building(self, x, y, "E3")
        for x in range(65,67):
            for y in range(35,37):
                Building(self, x, y, "E5")
        for x in range(67,69):
            for y in range(36,38):
                Building(self, x, y, "E7")
        for x in range(71,73):
            for y in range(35,37):
                Building(self, x, y, "E6")
        for x in range(72,74):
            for y in range(32,34):
                Building(self, x, y, "ECH")
        for x in range(71,73):
            for y in range(25,27):
                Building(self, x, y, "EC4")
        for x in range(62,64):
            for y in range(25,27):
                Building(self, x, y, "EC2")
        for x in range(61,63):
            for y in range(19,21):
                Building(self, x, y, "EC3")
        for x in range(71,73):
            for y in range(17,19):
                Building(self, x, y, "EC1")
        for x in range(69,71):
            for y in range(20,22):
                Building(self, x, y, "EC5")
        for x in range(42,44):
            for y in range(14,16):
                Building(self, x, y, "OPT")
        for x in range(35,37):
            for y in range(47,49):
                Building(self, x, y, "HS")
        for x in range(36,38):
            for y in range(55,57):
                Building(self, x, y, "STJ")
        for x in range(29,31):
            for y in range(56,58):
                Building(self, x, y, "REN")
        for x in range(32,34):
            for y in range(62,64):
                Building(self, x, y, "STP")
        for x in range(36,38):
            for y in range(68,70):
                Building(self, x, y, "CGR")
        for x in range(84,86):
            for y in range(54,56):
                Building(self, x, y, "CMH")
        for x in range(87,89):
            for y in range(52,54):
                Building(self, x, y, "UWP")
                
    def load_data(self):
        pass
    
    def new(self):
        # initialize all variables and do all the setup for a new game
        self.all_sprites = pg.sprite.Group()
        self.buildings = pg.sprite.Group()
        self.disease = Disease(self, 10, 10)
        self.draw_campus_map()
    
    def run(self):
        # game loop - set self.playing = False to end the game
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()
            
    def quit(self):
        pg.quit()
        sys.exit()
        
    def update(self):
        self.all_sprites.update()
    
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
        self.all_sprites.draw(self.screen)
        pg.display.flip()
        
    
    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()
                if event.key == pg.K_LEFT:
                    self.disease.move(dx=-1)
                if event.key == pg.K_RIGHT:
                    self.disease.move(dx=1)
                if event.key == pg.K_UP:
                    self.disease.move(dy=-1)
                if event.key == pg.K_DOWN:
                    self.disease.move(dy=1)       
    
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
