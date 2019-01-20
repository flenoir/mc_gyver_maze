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

        with open(self.maze_file, "r") as maze_map:
            for i, line in enumerate(maze_map):
                line_array = []
                for index, el in enumerate(line.strip()):
                    line_array.append((el, i, index))
                    # print("index {} et el {} et i {}".format(index, el, i))
                self.array.append(line_array)
    
     # show maze
    def show_maze(self):

        pygame.init()
        area = pygame.display.set_mode((self.width, self.height))

        background = pygame.image.load(self.background).convert()
        area.blit(background, (0, 0))

        wall_block = pygame.image.load(self.wall).convert()
        
        for item in self.array:
            # print(item[0][0])
            for i, w in enumerate(item):
                print(i)
                if item[i][0] == "X":
                    area.blit(wall_block, (int(item[i][2])*45, int(item[i][1])*45))
                                
        # return 0

        pygame.display.flip()

        # # update of mac gyver's position
        # self.array[char1.position[0]][char1.position[1]] = char1.symbol
        # self.array[char2.position[0]][char2.position[1]] = char2.symbol
        # # parse array and print maze level
      


