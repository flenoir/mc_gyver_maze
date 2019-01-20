from classes import Level, Character, Game, Player
import constants
import pygame
from pygame.locals import *


jeu = Game(constants.maze1, constants.wall )

mc = Player("Mac Gyver", (0, 1), "images/MacGyver.png", jeu, True, 0)
g = Player("The Guardian", (2, 14), "images/Gardien.png", jeu, False, 0)
jeu.show_maze(mc, g)

continuer = 1

while continuer:
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = 0
        if event.type == KEYDOWN:
            if event.key == K_DOWN:
                print("fleche bas")
    

# if __name__ == "__main__":

#     #### GAME START ####

#     print("Hi, welcome in Mac Gyver's Maze")
#     level_choice = input("Please select a level? 1 or 2 ? ")
#     print("Ok, let's go for level " + level_choice)


#     if int(level_choice) == 1:

#         # instanciation of level
#         new_level = Level("maze_map.py")

#         # instanciation of characters
#         mac_gyver = Character("Mac Gyver", (0, 1), "M", new_level, True, 0)
#         guardian = Character("The Guardian", (2, 14), "G", new_level, False, 0)

#         end_game = 0

#         # start game loop
#         while end_game == 0:

#             # level display
#             new_level.show_maze(mac_gyver, guardian)
            
#             select_move = input("please select a new position (one number for line, one for position) for example 1,2 : ")
            
#             tuplized_move = tuple(int(x) for x in select_move.split(","))
#             print("tuple is ", tuplized_move)

#             # change of mac_gyver position regarding new input
#             movment = mac_gyver.move(tuplized_move)
#             print("les movments  actual et previous sont " + str(movment[0]) + " et " + str(movment[1]))
#             # update new current position
#             mac_gyver.position = movment[0]
#             # update previous position to replace trace by "0"        
#             new_level.array[movment[1][0]][movment[1][1]] = "0"


#     else:
#         print("This level is not available yet")


# main()