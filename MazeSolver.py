#Name: Mohammed Thamidur Rashid
#Student ID: 11280257
#NSID: mor867
#Lab: 06
#Course: CMPT 145
#Instructor: Michael Hosch


import gui as gui

def reachedEndPoint(currentPoint , endPoint):
    """
    Purpose: To check if the endPoint of the maze has been reached

    Pre-Conditions:
                currentPoint: a tuple contianing the current position of the maze
                endPoint: a tuple marking the end or destination point of the maze

    Post-Conditions: The MazeSolver function  returns True  if this condition is met

    :return: True if the we have reached the destination False otherwise
    """

    return currentPoint == endPoint


def reachedDeadEnd(maze, currentPoint):
    """
    Purpose:  To check if the deadEnd of the maze has been reached

    Pre-Conditions: currentPoint: a tuple contianing the current position of the maze

    Post-Conditions:
                    The MazeSolver function  returns False if this condition is met
    Return: True if we have reached the dead end of the map

    :return:
    """
    if currentPoint[0]<0 or  currentPoint[1] < 0 or currentPoint[0]==len(maze) or  currentPoint[1] == len(maze):
        return True



def MazeSolver(maze , startPoint, endPoint):
    """
    Purpose: To find a path recursively to the end of the maze

    Pre-Conditions:
            :param maze: The maze in a list of list form
            :param startPoint: the start point of the maze in (r, c) tuple
            :param endPoint: the end point of the maze in (r, c) tuple

    Post-Conditions:
            the maze path will be maked with 'P'

    :return: True if the path exists otherwise False

    """
    global iteration_count
    iteration_count = iteration_count + 1
    print("iteration number: ", iteration_count)

    for i in path:
        for j in i:
            print(j, end=' ', )
        print()


    # check if the maze has reached its destination
    if (reachedEndPoint(startPoint, endPoint)):
        #indication that we have reached the destination
        gui.call(maze, path, _startPoint, _endpoint)

        try:
            path[startPoint[0]][startPoint[1]] = 'P'
            return True
        except IndexError:
            return False

    try:
        maze[startPoint[0]][startPoint[1]] == 1
    except IndexError:
        return False

    if maze[startPoint[0]][startPoint[1]] == 1 or path[startPoint[0]][startPoint[1]] == 'P':
        # the start point is updated each time as the current point
        # startPoint = _startPoint
        return False

    if maze[startPoint[0]][startPoint[1]] == 0:

        gui.call(maze, path, _startPoint, _endpoint)

        path[startPoint[0]][startPoint[1]] = 'P'

        # To go right
        if startPoint[0] != width:
            if MazeSolver(maze, (startPoint[0] + 1, startPoint[1]), endPoint):
                return True

        # To go down
        if startPoint[1] != hieght:
            if MazeSolver(maze, (startPoint[0], startPoint[1] + 1), endPoint):
                return True

        # To go up
        if startPoint[1] != 0:
            if MazeSolver(maze, (startPoint[0], startPoint[1] - 1), endPoint):
                return True

        # To go left
        if startPoint[0] != 0:
            if MazeSolver(maze, (startPoint[0] - 1, startPoint[1]), endPoint):
                return True


        # backtracking
        path[startPoint[0]][startPoint[1]] = '0'

    return False

# the starting and the ending point
_startPoint = (0, 3)
_endpoint = (4,5)
# goal is to find a path to the end of the maze

mazeFile = open('Maze2.txt')

maze = []

for line in mazeFile:
    line = line.rstrip().split()
    line = [int(i) for i in line]
    # print(line)
    maze.append(line)

# print(maze)
hieght = len(maze)
width = len(maze[0])
# the path of the maze
path = []
for r in range(len(maze)):
    row = []
    for c in range(len(maze[r])):
        if maze[r][c] == 1:
            row.append(1)
        else:
                row.append(0)

    path.append(row)

# keeping a copy of the maze
mazeCopy = maze.copy()

# driver prints only if the maze is solve
# The given maze
print("\nThe given Maze\n")
for r in range(len(maze)):
    for c in range(len(maze[r])):
        print(maze[r][c], end=' ')
    print('')

iteration_count = 0

if MazeSolver(maze, _startPoint, _endpoint):
    print("\n The Solved Maze is: \n")
    # printing the solved maze
    for r in range(len(maze)):
        for c in range(len(maze[r])):
            if path[r][c] == 'P':
                print("P", end = ' ')
            else:
                print(maze[r][c], end = ' ')
        print('')
        path.append(row)

else:
    print("\nThe Maze couldn't be solved as the destination couldn't be reached!")

# # code for the visual representation
#
# class MazesolverClass:
#     def __init__(self):
#         self.MazeHieght = hieght
#         self.MazeWidth = width
#         self.Maze = maze

# gui.call(maze7)
