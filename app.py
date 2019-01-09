print("Hi, welcome in Mac Gyver's Maze")
level_choice = input("Please select a level? 1 or 2 ? ")
print("Ok, let's go for level " + level_choice)



class Level:
    #create level
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

    # show level
    def show_maze(self, result):
        self.result = result
        for item in self.result:
            print(item)


if int(level_choice) == 1:
    #instanciation of level
    new_level = Level()
    # level creation
    res = new_level.create_maze("maze_map.py")
    # level display
    new_level.show_maze(res)
else:
    print("This level is not available yet")