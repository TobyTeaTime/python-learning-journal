'''
[
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [1, 1, 1, 1, 0]
]

startpoint = [0][0]
endpoint = [rowlength][rownumber] ([4][4])
0 = free space
1 = wall
2 = visited
'''


# startpoint = [0]*[0]
# endpoint = rowlength * rownumber
my_array = [ # maze to be ran
    [0, 0, 1],
    [1, 0, 1],
    [1, 0, 0]
]

# starts runner position at [0][0]
i = 0 # value of x-position / place in row (which column)
j = 0 # value of y-position / which row

runnerPos = my_array[i][j] # returns position

rowLength = len(my_array[0]) # returns length of row 0
rowNumber = len(my_array) # returns how many rows there are (COLUMN HEIGHT)

def printArray(maze): # prints a 2d visualization of the maze
    for row in maze:
        for element in row:
            print (element, end=" ")
        print()
    print()

def edgeDetect(i, j): # reports if current position is out of bounds
    if i < 0 or i >= rowNumber:
        return False
    if j < 0 or j >= rowLength:
        return False

def breadCrumb(i, j): #changes value of current position to 2
    if runnerPos == 1:
        my_array[i][j] = 2

# ------------------------------------------------------------------------------------------------------- #

def look(i, j, dir): # looks in a direction, changes i, j to match
    if dir == "up":
        i = i - 1
        breadCrumb(i, j)
    elif dir == "down":
        i = i + 1
        breadCrumb(i, j)
    elif dir =="left":
        j = j - 1
        breadCrumb(i, j)
    elif dir =="right":
        j = j + 1
        breadCrumb(i, j)


def mazeRunner(maze, i, j): # runs the maze / main
    edgeDetect(i, j)

    if runnerPos == 0:
        my_array[i][j] = 2
        look(i, j, "right")
    else:
        print("next step")


printArray(my_array)
if mazeRunner(my_array, 0, 0):
    print ("path found")
else: 
    print ("path not found")
printArray(my_array)



