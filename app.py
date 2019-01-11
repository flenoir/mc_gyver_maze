class Level:

    MAP_ARRAY = []

    # create level
    def __init__(self, file):
        self.file = file        
        with open(self.file,"r") as map:            
            for line in map:
                line_array = []
                for el in line.strip():                    
                    line_array.append(el)
                self.MAP_ARRAY.append(line_array)

    # show maze
    def show_maze(self, char1_pos, char1_symbol, char2_pos, char2_symbol, position_log):        
        # self.char1_pos = char1_pos
        # self.char2_pos = char2_pos
        # self.char1_symbol = char1_symbol
        # self.char2_symbol = char2_symbol
        if self.MAP_ARRAY[char1_pos[0]][char1_pos[1]] == "X":
            print("you cannot go through walls")
            # remove last mac gyver position in log array
            mac_gyver_position_log.pop()
            return 0
           
        elif self.MAP_ARRAY[char1_pos[0]][char1_pos[1]] == "G" and mac_gyver.bag_content == 3:
            print(" Mac Gyver won !")
            return 1
            
        elif self.MAP_ARRAY[char1_pos[0]][char1_pos[1]] == "G" and mac_gyver.bag_content < 3:
            print(" Mac Gyver looses !")
            return 1
             
        else:
            if self.MAP_ARRAY[char1_pos[0]][char1_pos[1]] == "I":
                print("Mac gyver found an item and added it to his bag")
                mac_gyver.bag_content +=1
                 # update of mac gyver's position
                self.MAP_ARRAY[char1_pos[0]][char1_pos[1]] = char1_symbol
                self.MAP_ARRAY[char2_pos[0]][char2_pos[1]] = char2_symbol
                # update of mac gyver's previous position
                self.position_log = position_log
                if len(position_log) > 1:
                    self.MAP_ARRAY[self.position_log[-2][0]][self.position_log[-2][1]] = '0'
                for item in self.MAP_ARRAY:
                    print(item)
                return 0
            else:    
                # update of mac gyver's position
                self.MAP_ARRAY[char1_pos[0]][char1_pos[1]] = char1_symbol
                self.MAP_ARRAY[char2_pos[0]][char2_pos[1]] = char2_symbol
                # update of mac gyver's previous position
                self.position_log = position_log
                if len(position_log) > 1:
                    self.MAP_ARRAY[self.position_log[-2][0]][self.position_log[-2][1]] = '0'
                for item in self.MAP_ARRAY:
                    print(item)
                return 0
                


class Character:

    # create character
    def __init__(self, name, position, symbol, movable, bag_content):
        self.name = name
        self.position = position
        self.symbol = symbol
        self.movable = movable
        self.bag_content = bag_content
        

    # move character
    def move(self, new_position):
        print("character position is ",self.position)
        self.position = new_position
        print("character new position is ",self.position)



#### GAME START ####

print("Hi, welcome in Mac Gyver's Maze")
level_choice = input("Please select a level? 1 or 2 ? ")
print("Ok, let's go for level " + level_choice)


if int(level_choice) == 1:

    mac_gyver_position_log  = []

    #instanciation of level
    new_level = Level("maze_map.py")
    
    # instanciation of characters
    mac_gyver = Character("Mac Gyver", (0, 1), "M", True, 0)
    guardian = Character("The Guardian", (2, 14), "G", False, 0)



    end_game = 0

    #start game loop
    while end_game == 0:
        # log mac gyver position
        mac_gyver_position_log.append(mac_gyver.position)

        # level display
        new_level.show_maze(mac_gyver.position, mac_gyver.symbol,guardian.position,guardian.symbol, mac_gyver_position_log)
        
        # print(mac_gyver.move())

        select_move = input("please select a new position (one number for line and one for position) for example 12 : ")
        
        
        # change of mac_gyver position regarding new input
        # mac_gyver.position = (int(select_move[0:1]),int(select_move[1:3]))
        print(mac_gyver.move((int(select_move[0:1]), int(select_move[1:3]))))
       


        
else:
    print("This level is not available yet")

