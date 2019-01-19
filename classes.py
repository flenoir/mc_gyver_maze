from random import randint


class Level:

    # create level
    def __init__(self, file):
        self.file = file
        self.array = []
        self.items = 3
        with open(self.file, "r") as map:            
            for line in map:
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