"""Main app."""
from classes import Maze, Character, Screen
import constants
import pygame
from pygame.locals import *

game_screen = Screen(constants.START) 

jeu = Maze(constants.MAZE1, constants.WALL, constants.ITEMS)

mc = Character("Mac Gyver", (0, 1), "images/MacGyver.png", jeu, 0)
g = Character("The Guardian", (2, 14), "images/Gardien.png", jeu, 0)


go_on = True

def gaming():
    turn = True
    while turn:
        for event in pygame.event.get(): 
            if event.type == QUIT:
                turn = False
            else:
                jeu.show_maze(mc, g)
                val = mc.move(event, mc, g)
                turn_modifier = jeu.end_game(val)
                turn = turn_modifier
                

while go_on:
    for event in pygame.event.get(): 
        if event.type == QUIT:
            go_on = False
        else:
            game_screen.display_screen()
            if event.type == KEYDOWN and event.key == K_s:
                gaming()
                go_on = False


                
