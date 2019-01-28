"""Classes file."""
from random import randint
import pygame
from pygame.locals import *


class Screen:
    """ Creation of start screen of game"""

    def __init__(self, maze):
        self.width = maze['x_size']
        self.height = maze['y_size']
        self.background = maze['background']

    def display_screen(self):
        # initalisation of screen
        pygame.init()
        # load area
        self.screen = pygame.display.set_mode((self.width, self.height))
        
        # load background
        self.back = pygame.image.load(self.background).convert()

        # pin background on area
        self.screen.blit(self.back, (0, 0))

        # draw box to click and start game
        pygame.draw.rect(self.screen, (93, 188, 210), pygame.Rect((50, 140), (180, 25)))
        font = pygame.font.SysFont('Arial', 20, bold=True)
        self.screen.blit(font.render("Press 's' to start", True, (0, 0, 26)), (60, 140))

        pygame.display.flip()


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
        self.items = {
            'J': items_pictures[0],
            'K': items_pictures[1],
            'L': items_pictures[2]
        }
        self.items_pictures = items_pictures
        self.items_pos = []

        # initalisation of Maze level area
        # pygame.init()
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
            x, y = randint(0, 14), randint(0, 14)
            random_tuple = self.array[x][y][1], self.array[x][y][2]            

            if self.array[x][y][0] != 'X':
                # avoid position of item on characters position
                if random_tuple != (0, 1) and random_tuple != (2, 14):
                    item = self.items.popitem()
                    self.array[x][y][0] = item[0]
                    item_tuple = self.array[x][y], item[1]
                    self.items_pos.append(item_tuple)

        # pin background on area
        self.area.blit(self.back, (0, 0))

    def char_position(self, characters):
        """Characters display."""
        for c in characters:
            c.name = pygame.image.load(c.symbol).convert_alpha()
            character_pos = c.name.get_rect(topleft=(0, 0))
            character_pos = character_pos.move(c.position[1] * 45, c.position[0] * 45)
            self.area.blit(c.name, character_pos)

    def show_maze(self, char1, char2):
        """Maze display."""

        # update display form screen start resolution
        self.area = pygame.display.set_mode((self.width, self.height))
        # pin background on area
        self.area.blit(self.back, (0, 0))
        
        # load wall and display/pin walls on maze_level
        wall_block = pygame.image.load(self.wall).convert()
        for item in self.array:            
            for i, w in enumerate(item):                
                if item[i][0] == "X":
                    self.area.blit(wall_block, (int(item[i][2])*45, int(item[i][1])*45))

        # display of items
        for i, v in enumerate(self.items_pos):
            picture = self.items_pos[i][1]
            i = pygame.image.load(picture).convert_alpha()            
            self.area.blit(i, (v[0][2]*45, v[0][1]*45))

        # display of characters position (to be refactored)
        characters = [char1, char2]       
        self.char_position(characters)

        # draw counter and display collected items
        pygame.draw.rect(self.area, (93, 188, 210), pygame.Rect((0, 675), (675, 25)))
        font = pygame.font.SysFont('Arial', 20, bold=True)
        self.area.blit(font.render('Items in bag : {}'.format(char1.bag_content), True, (0,0,26)), (5, 675))
        
        pygame.display.flip()

    def end_game(self, val):
        """Check end game."""
        if val == (20, 20):
            # # draw box to click and start game
            pygame.draw.rect(self.area, (93, 188, 210), pygame.Rect((250, 250), (200, 40)))
            font = pygame.font.SysFont('Arial', 20, bold=True)
            self.area.blit(font.render("Mac Gyver looses", True, (0, 0, 26)), (265, 260))
            pygame.display.update()
            pygame.time.wait(5000)
            return False
        elif val == (30, 30):
             # # draw box to click and start game
            pygame.draw.rect(self.area, (93, 188, 210), pygame.Rect((250, 250), (200, 40)))
            font = pygame.font.SysFont('Arial', 20, bold=True)
            self.area.blit(font.render("Mac Gyver won !", True, (0, 0, 26)), (265, 260))
            pygame.display.update()
            pygame.time.wait(5000)
            return False
        else:
            return True
            

    
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
            checked_move = char1.check_move(self.position, event, char2)            
            self.position = checked_move[0], checked_move[1]            
            return checked_move

    def check_move(self, pos, event, char2):
        """Check move legality."""
        # create dictionnary of possible keys (K.DOWN, K_UP, etc...)
        keystroke = {
            274: (0, 1),
            273: (0, -1),
            275: (1, 0),
            276: (-1, 0),
            115: (0, 0)  # to avoid stop on s key press
        }

        if event.key in keystroke:          
            x = keystroke[event.key][0]
            y = keystroke[event.key][1]
            sorted_letter = self.maze_level.array[pos[0]+y][pos[1]+x][0]

            if sorted_letter != "X":
                # if J, K, L found remove item
                for j in self.maze_level.items_pos:                
                    if j[0][0] == sorted_letter:
                        son = pygame.mixer.Sound("sons/item_pick.wav")
                        son.set_volume(0.2)
                        son.play()                   
                        self.maze_level.items_pos.remove(j)
                        self.bag_content += 1
                
                new_move = (self.maze_level.array[pos[0]+y][pos[1]+x][1],  self.maze_level.array[pos[0]+y][pos[1]+x][2])
                
                if new_move == char2.position and self.bag_content < 3:                    
                    # print("mac Gyvers looses")
                    return 20,20
                elif new_move == char2.position and self.bag_content == 3:
                    # print("mac Gyvers won")
                    return 30,30
                
                return new_move
            else:
                new_move = (self.maze_level.array[pos[0]][pos[1]][1], self.maze_level.array[pos[0]][pos[1]][2])
                return new_move
    
        else:
            print("you cannot use this key")
            return pos