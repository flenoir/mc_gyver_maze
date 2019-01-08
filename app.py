

with open("maze_map.py","r") as map:
    map_array = []
    for line in map:
        line_array = []
        for el in line.strip():
            print(el)
            line_array.append(el)
        map_array.append(line_array)

# print(map_array)
for item in map_array:
    print(item)