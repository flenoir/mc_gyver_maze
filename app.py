from classes import Game, Player
import constants
import pygame
from pygame.locals import *


jeu = Game(constants.maze1, constants.wall)

mc = Player("Mac Gyver", (0, 1), "images/MacGyver.png", jeu, True, 0)
g = Player("The Guardian", (2, 14), "images/Gardien.png", jeu, False, 0)


continuer = 1

while continuer:
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = 0
        else:
            jeu.show_maze(mc, g)
            mc.move(event, mc, g)
   