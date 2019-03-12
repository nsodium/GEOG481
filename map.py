# Created by: Shijin (Kevin) Yang
# Pygame GUI to display the university of waterloo, and the movement of disease

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
        pg.key.set_repeat(500,100)
        self.load_data()

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
        for x in range(14,17):
            for y in range(24,27):
                Building(self, x, y, "REV")
        for x in range(36, 40):
            for y in range(24, 28):
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
        for x in range(60,66):
            for y in range(28,32):
                Building(self, x, y, "PAC")
        for x in range(63,66):
            for y in range(37,40):
                Building(self, x, y, "SLC")
        for x in range(43,45):
            for y in range(41,43):
                Building(self, x, y, "QNC")
        for x in range(74,77):
            for y in range(35,40):
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
        for x in range(79,83):
            for y in range(39,41):
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
        for x in range(67,70):
            for y in range(54,57):
                Building(self, x, y, "NH")
        for x in range(74,76):
            for y in range(57,60):
                Building(self, x, y, "LIB")
        for x in range(67,70):
            for y in range(62,63):
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
        for x in range(73,75):
            for y in range(65,67):
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
        for x in range(54,56):
            for y in range(54,57):
                Building(self, x, y, "STJ")
        for x in range(40,43):
            for y in range(54,56):
                Building(self, x, y, "REN")
        for x in range(45, 47):
            for y in range(64,66):
                Building(self, x, y, "STP")
        for x in range(44, 46):
            for y in range(72,74):
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

    def colour_update(self):
        print(self.background_image.get_at((self.disease.x, self.disease.y)))
        pass

    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, WHITE, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen, WHITE, (0,y), (WIDTH, y))

    def draw(self):
        self.screen.fill(BGCOLOR)
        background_image = pg.image.load("webmap.gif").convert()
        background_image = pg.transform.scale(background_image, (1024, 768))
        self.screen.blit(background_image, [0, 0])
        self.draw_grid()
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
