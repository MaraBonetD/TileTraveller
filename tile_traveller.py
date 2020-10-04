#Print available travel locations
def printCurrentLocation(grid, location):
    print("You can travel: " + " or ".join(grid[location[0]][location[1]]) + ".")

#Get the directions you can travel to from the current location by means of a list
def getDirections(grid, location):
    dirs = []
    for i in grid[location[0]][location[1]]:
        dirs.append(i[1].lower())
    return dirs

#List of lists, one for each row of the grid // Directions you can travel
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

#Start location = (0,0) / loc[0] = x ; loc[1] = y
current_loc = [0,0]
while True:
    #Victory coordinates: (2,0)
    if current_loc[0] == 2 and current_loc[1] == 0:
        print("Victory!")
        break

    #Calling the function to find out where we can travel
    printCurrentLocation(grid, current_loc)

    #Read travel direction from user
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
