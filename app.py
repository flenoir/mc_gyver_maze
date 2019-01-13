class Level:

    # create level
    def __init__(self, file):
        self.file = file
        self.array = []
        with open(self.file, "r") as map:            
            for line in map:
                line_array = []
                for el in line.strip():                    
                    line_array.append(el)
                self.array.append(line_array)

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
    def __init__(self, name, position, symbol, movable, bag_content):
        self.name = name
        self.position = position
        self.symbol = symbol
        self.movable = movable
        self.bag_content = bag_content
        self.position_log = [position]
        
    # move character
    def move(self, new_position, maze):
        print("character position is ", self.position)
        # print(maze)
        if maze[new_position[0]][new_position[1]] != "X":
            self.position = new_position
            print("character new position is ", self.position)
            self.position_log.append(self.position)
            print("position log array", self.position_log)
            return self.position, self.position_log[-2]
        elif maze[new_position[0]][new_position[1]] == "I":
            self.bag_content += 1
            self.position = new_position
            print("character new position is ", self.position)
            self.position_log.append(self.position)
            print("position log array", self.position_log)
            return self.position, self.position_log[-2]
        else:
            print("You cannot move into walls")
            print("after walls ", self.position)
            return self.position
            


#### GAME START ####

print("Hi, welcome in Mac Gyver's Maze")
level_choice = input("Please select a level? 1 or 2 ? ")
print("Ok, let's go for level " + level_choice)


if int(level_choice) == 1:

    # instanciation of level
    new_level = Level("maze_map.py")

    # instanciation of characters
    mac_gyver = Character("Mac Gyver", (0, 1), "M", True, 0)
    guardian = Character("The Guardian", (2, 14), "G", False, 0)

    end_game = 0

    # start game loop
    while end_game == 0:

        # level display
        new_level.show_maze(mac_gyver, guardian)
        
        select_move = input("please select a new position (one number for line, one for position) for example 1,2 : ")
        
        tuplized_move = tuple(int(x) for x in select_move.split(","))
        print("tuple is ", tuplized_move)

        # change of mac_gyver position regarding new input
        movment = mac_gyver.move(tuplized_move, new_level.array)
        print("les movments  actual et previous sont " + str(movment[0]) + " et " + str(movment[1]))
        # update new current position
        mac_gyver.position = movment[0]
        # update previous position to replace trace by "0"        
        new_level.array[movment[1][0]][movment[1][1]] = "0"


else:
    print("This level is not available yet")
