"""Main app."""
from classes import Maze, Character, Screen
import constants
import pygame
from pygame.locals import *

game_screen = Screen(constants.start) 

jeu = Maze(constants.maze1, constants.wall, constants.items)

mc = Character("Mac Gyver", (0, 1), "images/MacGyver.png", jeu, 0)
g = Character("The Guardian", (2, 14), "images/Gardien.png", jeu, 0)


continuer = 1

def gaming():
    turn = 1
    while turn:
        for event in pygame.event.get(): 
            if event.type == QUIT:
                turn = 0
            else:
                jeu.show_maze(mc, g)
                val = mc.move(event, mc, g)
                print("la valeur de mouvement est : ", val)


while continuer:
    for event in pygame.event.get(): 
        if event.type == QUIT:
            continuer = 0
        else:
            game_screen.display_screen()
            if event.type == KEYDOWN and event.key == K_s:
                gaming()
                continuer = 0 


                
