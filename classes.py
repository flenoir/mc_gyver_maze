"""Classes file."""
from random import randint
import pygame
from pygame.locals import *


class Maze:
    """Creation and display of Maze."""

    def __init__(self, maze, wall, items_pictures):
        """Maze constructor."""
        self.width = maze['x_size']
        self.height = maze['y_size']
        self.background = maze['background']
        self.wall = wall
        self.maze_file = maze['maze_file']
        self.array = []
        self.items = ['J', 'K', 'L']
        self.items_pictures = items_pictures
        self.items_pos =[]

        # initalisation of Maze level area
        pygame.init()
        # load area
        self.area = pygame.display.set_mode((self.width, self.height))
        # load background
        self.back = pygame.image.load(self.background).convert()

        with open(self.maze_file, "r") as maze_map:
            for i, line in enumerate(maze_map):
                line_array = []
                for index, el in enumerate(line.strip()):
                    line_array.append([el, i, index])                    
                self.array.append(line_array)
        
        # generate random display of items
        
        while len(self.items) > 0:
            x,y = randint(0, 14), randint(0, 14)

            if self.array[x][y][0] != 'X':
                item = self.items.pop()
                self.array[x][y][0] = item
                self.items_pos.append(self.array[x][y])

            # pin background on area
        self.area.blit(self.back, (0, 0))

    def show_maze(self, char1, char2):
        """Maze display."""

        # pin background on area
        self.area.blit(self.back, (0, 0))

        # load wall and display/pin walls on maze_level
        wall_block = pygame.image.load(self.wall).convert()
        for item in self.array:
            # print(item[0][0])
            for i, w in enumerate(item):
                # print(i)
                if item[i][0] == "X":
                    self.area.blit(wall_block, (int(item[i][2])*45, int(item[i][1])*45))

        for i, v in enumerate(self.items_pos):
            print("les positions des items sont ", i, v)
            i = pygame.image.load(self.items_pictures[i]).convert()
            print(i)
            self.area.blit(i, (v[2]*45,v[1]*45))

        # first display of characters position (to be refactored)       
        macgyver = pygame.image.load(char1.symbol).convert()
        guardian = pygame.image.load(char2.symbol).convert()

        macgyver_position = macgyver.get_rect(topleft=(0, 0))
        guardian_position = guardian.get_rect(topleft=(0, 0))

        print("log mac gyver", char1.position_log)

        macgyver_position = macgyver_position.move(char1.position[1] * 45, char1.position[0] * 45)
        guardian_position = guardian_position.move(char2.position[1] * 45, char2.position[0] * 45)
        self.area.blit(macgyver, macgyver_position)
        self.area.blit(guardian, guardian_position)

        pygame.display.flip()

    
class Character:
    """Creation and movment of Character."""

    def __init__(self, name, position, symbol, maze_level, bag_content):
        """Character constructor."""
        self.name = name
        self.position = position
        self.symbol = symbol
        self.maze_level = maze_level
        self.bag_content = bag_content
        self.position_log = [position]
        self.icon = pygame.image.load(symbol).convert()
        self.pos = self.icon.get_rect(topleft=(int(position[1])*45, int(position[0])*45))
        self.maze_level.area.blit(self.icon, self.pos)

    def move(self, event, char1, char2):
        """Character movment."""
        if event.type == KEYDOWN:
            checked_move = char1.check_move(self.position, event)
            print("le mouvement checké est", checked_move)
            self.position = checked_move[0], checked_move[1]

    def check_move(self, pos, event):
        """Check move legality."""
        # create dictionnary of possible keys (K.DOWN, K_UP, etc...)
        keystroke = {
            274: (0, 1),
            273: (0, -1),
            275: (1, 0),
            276: (-1, 0)
        }

        x = keystroke[event.key][0]
        y = keystroke[event.key][1]
        
        if self.maze_level.array[pos[0]+y][pos[1]+x][0] != "X":
            new_move = (self.maze_level.array[pos[0]+y][pos[1]+x][1],  self.maze_level.array[pos[0]+y][pos[1]+x][2])
            return new_move
        else:
            new_move = (self.maze_level.array[pos[0]][pos[1]][1],  self.maze_level.array[pos[0]][pos[1]][2])
            return new_move
    