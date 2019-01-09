print("Hi, welcome in Mac Gyver's Maze")
level_choice = input("Please select a level? 1 or 2 ? ")
print("Ok, let's go for level " + level_choice)



class Level:
    #create level -> methode de classe ? 
    def create_maze(self, file):
        self.file = file
        with open(self.file,"r") as map:
            map_array = []
            for line in map:
                line_array = []
                for el in line.strip():                    
                    line_array.append(el)
                map_array.append(line_array)
            return map_array

    def update_maze(self, level, char1_pos, char1_symbol, char2_pos, char2_symbol):
        self.level = level
        self.char1_pos = char1_pos
        self.char2_pos = char2_pos
        self.char1_symbol = char1_symbol
        self.char2_symbol = char2_symbol
        self.level[char1_pos[0]][char1_pos[1]] = char1_symbol
        self.level[char2_pos[0]][char2_pos[1]] = char2_symbol
        # return self.level
        for item in self.level:
            print(item)



    # show level
    def show_maze(self, level):
        self.level = level
        for item in self.level:
            print(item)


class Character:

    def __init__(self, name, position, symbol, movable, bag_content):
        self.name = name
        self.position = position
        self.symbol = symbol
        self.movable = movable
        self.bag_content = bag_content

    def move(self, position):
        if position == "s":
            print("down")


if int(level_choice) == 1:
    #instanciation of level
    new_level = Level()
    # instanciation of characters
    mac_gyver = Character("Mac Gyver", (0,1),"M",True, 0)
    guardian = Character("The Guardian", (2,14),"G", False, 0)
    # level creation
    res = new_level.create_maze("maze_map.py")
    # level display
    new_level.update_maze(res,mac_gyver.position, mac_gyver.symbol,guardian.position,guardian.symbol)
    # new_level.show_maze(res)
    
    select_move = input("please select a new tuple line,letter : ")
   
    mac_gyver.position = (int(select_move[0:1]),int(select_move[1:2]))
    new_level.update_maze(res,mac_gyver.position, mac_gyver.symbol,guardian.position,guardian.symbol)
    # new_level.show_maze(update) # => il faut resoumettre cette position sur le labyrinthe vide pour ne pas avoir l ancienne postion affichée
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