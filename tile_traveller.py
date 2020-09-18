def printCurrentLocation(grid, location):
    print("You can travel: " + " or ".join(grid[location[0]][location[1]]) + ".")

def getDirections(grid, location):
    dirs = []
    for i in grid[location[0]][location[1]]:
        dirs.append(i[1].lower())
    return dirs

grid = [[],[],[]]
grid[0].append(["(N)orth"])
grid[0].append(["(N)orth","(E)ast", "(S)outh"])
grid[0].append(["(E)ast", "(S)outh"])
grid[1].append(["(N)orth"])
grid[1].append(["(S)outh", "(W)est"])
grid[1].append(["(E)ast", "(W)est"])
grid[2].append(["(N)orth"])
grid[2].append(["(N)orth","(S)outh"])
grid[2].append(["(S)outh", "(W)est"])

current_loc = [0,0]
while True:
    if current_loc[0] == 2 and current_loc[1] == 0:
        print("Victory!")
        break
    printCurrentLocation(grid, current_loc)
    travel_dir = input("Direction: ").lower()
    if travel_dir in getDirections(grid, current_loc):
        if travel_dir == "n":
            current_loc[1] += 1
        if travel_dir == "e":
            current_loc[0] += 1
        if travel_dir == "s":
            current_loc[1] -= 1
        if travel_dir == "w":
            current_loc[0] -= 1
    else:
        print("Not a valid direction!")
