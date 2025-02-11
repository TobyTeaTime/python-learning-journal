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

my_array = [ # maze to be ran
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [1, 1, 1, 1, 0]
]

rowLength = len(my_array[0]) # returns length of row 0
rowNumber = len(my_array) # returns how many rows there are (COLUMN HEIGHT)

def printArray(maze): # prints a 2d visualization of the maze
    for row in maze:
        for element in row:
            print (element, end=" ")
        print()
    print()

def mazeRunner(maze, i, j): # passes the array along with the coordinates for the current space
    if i < 0 or i >= rowNumber or j < 0 or j >= rowLength:
        return False  # out of bounds of the maze, 
    if maze[i][j] == 1 or maze[i][j] == 2:
        return False # either a wall or previously visited space
    if i == rowNumber - 1 and j == rowLength - 1:
        maze[i][j] = 2
        return True # reached the endpoint / bottom right of the maze
    
    # ^^^base case^^^ if current space is also the space in the furthest down and right, the maze is solved.  
    
    maze[i][j] = 2 # marks the current cell as visited

    if mazeRunner(maze, i, j + 1): #right
        return True
    if mazeRunner(maze, i + 1, j): #down
        return True
    if mazeRunner(maze, i, j - 1): #left
        return True
    if mazeRunner(maze, i - 1, j): #up
        return True
    
    # ^^^recursive case^^^ uses recursion to set the coordinates of the space to be used in the function

    maze[i][j] = 0 # unmarks current cell
    return False

    # ^^^if it finds a dead end, it unmarks the space

printArray(my_array)
if mazeRunner(my_array, 0, 0):
    print ("path found")
else: 
    print ("path not found")
printArray(my_array)



