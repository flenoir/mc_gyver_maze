from random import randint
import pygame
from pygame.locals import *


class Level:

    # create level
    def __init__(self, file):
        self.file = file
        self.array = []
        self.items = 3
        with open(self.file, "r") as maze_map:            
            for line in maze_map:
                line_array = []
                for el in line.strip():                    
                    line_array.append(el)
                self.array.append(line_array)

        #  display randomly items
        while self.items != 0:
            val1, val2 = randint(0, 14), randint(0, 14)

            if self.array[val1][val2] == "0":
                self.array[val1][val2] = "I"
                self.items -= 1
            # else:
            #     val1, val2 = randint(0, 14), randint(0, 14)

    # show maze
    def show_maze(self, char1, char2):        
        # update of mac gyver's position
        self.array[char1.position[0]][char1.position[1]] = char1.symbol
        self.array[char2.position[0]][char2.position[1]] = char2.symbol
        # parse array and print maze level
        for item in self.array:
            print(item)
        return 0


class Character:

    # create character
    def __init__(self, name, position, symbol, maze_level, movable, bag_content):
        self.name = name
        self.position = position
        self.symbol = symbol
        self.maze_level = maze_level
        self.movable = movable
        self.bag_content = bag_content
        self.position_log = [position]
       
    # move character
    def move(self, new_position):
        print("character position is ", self.position)
        # print(maze)
        if self.maze_level.array[new_position[0]][new_position[1]] == "X":
            print("You cannot move into walls")
            print("after walls ", self.position)
            return self.position
        elif self.maze_level.array[new_position[0]][new_position[1]] == "0":
            self.position = new_position
            print("character new position is ", self.position)
            self.position_log.append(self.position)
            print("position log array", self.position_log)
            return self.position, self.position_log[-2]
        elif self.maze_level.array[new_position[0]][new_position[1]] == "I":
            self.bag_content += 1
            self.position = new_position
            print("character new position is after picking item ", self.position)
            self.position_log.append(self.position)
            print("position log array", self.position_log)
            return self.position, self.position_log[-2]
        elif self.maze_level.array[new_position[0]][new_position[1]] == "G":
            self.position = new_position
            self.position_log.append(self.position)
            print("Mac Gyver's bag contains {} items".format(self.bag_content))
            if self.bag_content != 3:
                print("Mac Gyver looses")
                return self.position, self.position_log[-2]
            else:
                print("mac Gyvers won")
                return self.position, self.position_log[-2]
        else:
            print("other movment")


class Game:
    def __init__(self, maze, wall):
        # print(maze)
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
    def show_maze(self, movment, symbol, log):

        pygame.init()
        self.area = pygame.display.set_mode((self.width, self.height))

        background = pygame.image.load(self.background).convert()
        self.area.blit(background, (0, 0))

        wall_block = pygame.image.load(self.wall).convert()
        
        for item in self.array:
            # print(item[0][0])
            for i, w in enumerate(item):
                print(i)
                if item[i][0] == "X":
                    self.area.blit(wall_block, (int(item[i][2])*45, int(item[i][1])*45))
                                
        # return 0

        # # first display of characters position
        macgyver = pygame.image.load(symbol).convert()
        if len(log) > 1:
            macgyver_position = macgyver.get_rect(topleft=(log[1][-2], log[0][-2])) #=> previous position
        else: 
            macgyver_position = macgyver.get_rect(topleft=(0, 0))
   
        macgyver_position = macgyver_position.move(movment[1]*45, movment[0]*45)
        self.area.blit(macgyver, macgyver_position)

    
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
    
    def move(self, event):
        if event.type == KEYDOWN:
            if event.key == K_DOWN:
                print("fleche bas")
                print(self.position)
                self.position = self.position[0], self.position[1]+1
                print(self.position)
                self.position_log.append(self.position)
                print(self.position_log)
                # self.pos.move(self.position[0]*45, self.position[0]*45)
                # self.maze_level.area.blit(self.icon, self.pos)
                
                # print("maze_level", self.maze_level.array[self.position[0]][self.position[1]])
                # return self.position
                self.maze_level.show_maze(self.position, self.symbol, self.position_log)
