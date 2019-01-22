from random import randint
import pygame
from pygame.locals import *


class Game:
    def __init__(self, maze, wall):
        self.width = maze['x_size']
        self.height = maze['y_size']
        self.background = maze['background']
        self.wall = wall
        self.maze_file = maze['maze_file']
        self.array = []
        self.area = pygame.display.set_mode((self.width, self.height))

        with open(self.maze_file, "r") as maze_map:
            for i, line in enumerate(maze_map):
                line_array = []
                for index, el in enumerate(line.strip()):
                    line_array.append((el, i, index))                    
                self.array.append(line_array)


    
    # show maze
    def show_maze(self, char1, char2):

        pygame.init()
        self.area = pygame.display.set_mode((self.width, self.height))

        # load background
        background = pygame.image.load(self.background).convert()
        self.area.blit(background, (0, 0))

        # load wall and display walls  on maze_level
        wall_block = pygame.image.load(self.wall).convert()
        for item in self.array:
            # print(item[0][0])
            for i, w in enumerate(item):
                # print(i)
                if item[i][0] == "X":
                    self.area.blit(wall_block, (int(item[i][2])*45, int(item[i][1])*45))


        # # first display of characters position (to be refactored)
        
        macgyver = pygame.image.load(char1.symbol).convert()
        guardian = pygame.image.load(char2.symbol).convert()

        macgyver_position = macgyver.get_rect(topleft=(0, 0))
        guardian_position = guardian.get_rect(topleft=(0, 0))

        macgyver_position = macgyver_position.move(char1.position[1] * 45, char1.position[0] * 45)
        guardian_position = guardian_position.move(char2.position[1] * 45, char2.position[0] * 45)
        self.area.blit(macgyver, macgyver_position)
        self.area.blit(guardian, guardian_position)

        pygame.display.flip()




class Player:
    # create character
    def __init__(self, name, position, symbol, maze_level, movable, bag_content):
        self.name = name
        self.position = position
        self.symbol = symbol
        self.maze_level = maze_level
        self.movable = movable
        self.bag_content = bag_content
        self.position_log = [position]
        self.icon = pygame.image.load(symbol).convert()
        self.pos = self.icon.get_rect(topleft=(int(position[1])*45, int(position[0])*45))
        self.maze_level.area.blit(self.icon, self.pos)
    
    def move(self, event, char1, char2):
        if event.type == KEYDOWN:
            if event.key == K_DOWN and self.maze_level.array[self.position[0]+1][self.position[1]][0] != "X":
                print("fleche bas")
                print(self.position)
                print("in array, position is : ", self.maze_level.array[self.position[0]][self.position[1]][0])
                # update of mac_gyver's position
                self.position = self.position[0]+1, self.position[1]
                print(self.position)
                # log new position in log array
                self.position_log.append(self.position)
                # display postion on maze level
                self.maze_level.show_maze(char1, char2)
            elif event.key == K_RIGHT and self.maze_level.array[self.position[0]][self.position[1]+1][0] != "X":
                self.position = self.position[0], self.position[1]+1                
                self.position_log.append(self.position)
                self.maze_level.show_maze(char1, char2)
            elif event.key == K_LEFT and self.maze_level.array[self.position[0]][self.position[1]-1][0] != "X":
                self.position = self.position[0], self.position[1]-1                
                self.position_log.append(self.position)
                self.maze_level.show_maze(char1, char2)
            elif event.key == K_UP and self.maze_level.array[self.position[0]-1][self.position[1]][0] != "X":
                self.position = self.position[0]-1, self.position[1]                
                self.position_log.append(self.position)
                self.maze_level.show_maze(char1, char2)

            else:
                print("you cannot go through walls !")
