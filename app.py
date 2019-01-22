"""Main app."""
from classes import Maze, Character
import constants
import pygame
from pygame.locals import *


jeu = Maze(constants.maze1, constants.wall)

mc = Character("Mac Gyver", (0, 1), "images/MacGyver.png", jeu, True, 0)
g = Character("The Guardian", (2, 14), "images/Gardien.png", jeu, False, 0)


continuer = 1

while continuer:
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = 0
        else:
            jeu.show_maze(mc, g)
            mc.move(event, mc, g)
