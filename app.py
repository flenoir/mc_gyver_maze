
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
        self.char1_pos = char1_pos
        self.char2_pos = char2_pos
        self.char1_symbol = char1_symbol
        self.char2_symbol = char2_symbol
        # update of mac gyver's position
        self.MAP_ARRAY[char1_pos[0]][char1_pos[1]] = char1_symbol
        self.MAP_ARRAY[char2_pos[0]][char2_pos[1]] = char2_symbol
        # update of mac gyver's previous position
        self.position_log = position_log
        if len(position_log) > 1:
            print(position_log[-2])
            self.MAP_ARRAY[position_log[-2][0]][position_log[-2][1]] = '0'
        for item in self.MAP_ARRAY:
            print(item)


class Character:

    # create character
    def __init__(self, name, position, symbol, movable, bag_content):
        self.name = name
        self.position = position
        self.symbol = symbol
        self.movable = movable
        self.bag_content = bag_content
        

    # move character
    def move(self, position):
        if position == "s":
            print("down")


#### GAME START ####

print("Hi, welcome in Mac Gyver's Maze")
level_choice = input("Please select a level? 1 or 2 ? ")
print("Ok, let's go for level " + level_choice)


if int(level_choice) == 1:

    mac_gyver_position_log  = []

    #instanciation of level
    new_level = Level("maze_map.py")
    
    # instanciation of characters
    mac_gyver = Character("Mac Gyver", (0,1),"M",True, 0)
    guardian = Character("The Guardian", (2,14),"G", False, 0)

    end_game = 0

    #start game loop
    while end_game != 1:
        # log mac gyver position
        mac_gyver_position_log.append(mac_gyver.position)
        print(mac_gyver_position_log)

        # level display
        new_level.show_maze(mac_gyver.position, mac_gyver.symbol,guardian.position,guardian.symbol, mac_gyver_position_log)
          
        select_move = input("please select a new position (one number for line and one for position) for example 12 : ")
        
        # change of mac_gyver position regarding new input
        mac_gyver.position = (int(select_move[0:1]),int(select_move[1:2]))

        print(mac_gyver_position_log)
        


        
else:
    print("This level is not available yet")



# Pseudo code

# ask player to select a level
# create maze based on level
# display maze

#create a loop until game is finished
    # ask player to move mcgyver character (do not allow to move outside maze or on a wall)
    # reload maze with new mcgyver position

    #create condition inside loop
    # if mac gyver move on an item , he fills his bag
    # if mac Gyver faces guardian without all items he looses (game is finished)
    # else he wins (game is finished)


# objects

# maze (attribute is level, method create, method display) -> hint : diplay method should be called after each move
# character (attribute bag, method move)