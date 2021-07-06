# A Maze Searching program for CS440
# Authors: Brian Albert

# Import libraries
import numpy as np

# Breadth-first search algorithm
def BFS(startStateList, goalStateList, maze, size):
    # Initialize the frontier and set it equal to the start state
    frontier = []
    frontier.append(startStateList)

    maze[startStateList[0]][startStateList[1]] = 2

    closed = []
    candidates = []
    expandArray = []
    node = []
    i = 0

    # Loop until a solution is found or a fail
    while len(frontier) != 0: 
        print(np.matrix(maze)) 

        node = frontier.pop(0)
        
        if node == goalStateList:
            x = goalStateList[0]
            y = goalStateList[1]
            path = []
            pathList = []
            cost = 0

            pathList.append(x)
            pathList.append(y)
            path.append(pathList.copy())
            pathList.clear()

            while maze[x][y] != 2:
                # Check if path goes left
                if x != size and y-1 != size and x != -1 and y-1 != -1:
                    if maze[x][y-1] == i-1:
                        pathList.append(x)
                        pathList.append(y-1)
                        path.append(pathList.copy())
                        cost += 1
                        y -= 1

                # Check if path goes right
                if x != size and y+1 != size and x != -1 and y+1 != -1:
                    if maze[x][y+1] == i-1:
                        pathList.append(x)
                        pathList.append(y+1)
                        path.append(pathList.copy())
                        cost += 1
                        y += 1

                # Check if path goes up
                if x-1 != size and y != size and x-1 != -1 and y != -1:
                    if maze[x-1][y] == i-1:
                        pathList.append(x-1)
                        pathList.append(y)
                        path.append(pathList.copy())
                        cost += 2
                        x -= 1

                # Check if path goes down
                if x+1 != size and y != size and x+1 != -1 and y != -1:
                    if maze[x+1][y] == i-1:
                        pathList.append(x+1)
                        pathList.append(y)
                        path.append(pathList.copy())
                        cost += 2
                        x += 1

                i -= 1
                pathList.clear()

            path.reverse()
            print("Path: ")
            print(path)

            print("Cost: ")
            print(cost)

            return 1
        
        closed.append(node.copy)

        i = maze[node[0]][node[1]] + 1

        # Expand the current node
        # Check left
        if node[0] != size and node[1]-1 != size and node[0] != -1 and node[1]-1 != -1:
            if maze[node[0]][node[1]-1] == 0:
                expandArray.append(node[0])
                expandArray.append(node[1]-1)
                candidates.append(expandArray.copy())
                maze[expandArray[0]][expandArray[1]] = i
                expandArray.clear() 

        # Check right
        if node[0] != size and node[1]+1 != size and node[0] != -1 and node[1]+1 != -1:
            if maze[node[0]][node[1]+1] == 0:
                expandArray.append(node[0])
                expandArray.append(node[1]+1)
                candidates.append(expandArray.copy())
                maze[expandArray[0]][expandArray[1]] = i
                expandArray.clear()

        # Check up
        if node[0]-1 != size and node[1] != size and node[0]-1 != -1 and node[1] != -1:
            if maze[node[0]-1][node[1]] == 0:
                expandArray.append(node[0]-1)
                expandArray.append(node[1])
                candidates.append(expandArray.copy())
                maze[expandArray[0]][expandArray[1]] = i
                expandArray.clear()

        # Check down
        if node[0]+1 != size and node[1] != size and node[0]+1 != -1 and node[1] != -1:
            if maze[node[0]+1][node[1]] == 0:
                expandArray.append(node[0]+1)
                expandArray.append(node[1])
                candidates.append(expandArray.copy())
                maze[expandArray[0]][expandArray[1]] = i
                expandArray.clear()

        for c in candidates:
            if c not in closed and c not in frontier:
                frontier.append(c.copy())

    return -1
 
# Depth-limited search algorithm
def DLS():
    return "one"
 
# A* algorithm using h
def A1():
    return "two"

# A* algorithm using h
def A2():
    return "three"

# A* algorithm using h
def A3():
    return "four"
 
# Method to run the correct algorithm
def runMaze(algorithm, ssl, gsl, maze, size):
    switcher = {
        0: BFS,
        1: DLS,
        2: A1,
        3: A2,
        4: A3
    }

    # Get the function from switcher dictionary
    func = switcher.get(algorithm, "nothing")
    # Execute the function
    return func(ssl, gsl, maze, size)

# Method for creating the given maze
def createMaze(size, mazeFile):
    # Initialize array with all zeros
    maze = [[0 for x in range(size)] for y in range(size)] 
    i = 0

    # Fill in the maze
    while i != size:
        j = 0
        while j != size:
            if j == 0 and i != 0:
                line = prev
            else:
                line = mazeFile.readline()
            lineList = line.split()
            spot = int(lineList[2])
            maze[i][j] = spot
            j += 1

        x = i
        while i == x and x != size-1:
            line = mazeFile.readline()
            lineList = line.split()
            x = int(lineList[0])
            prev = line

        i += 1

    return maze


# Driver Method
if __name__ == "__main__":
    # Open problem.txt and save information
    problemFile = open("a1/problem.txt", "r")

    mazeSize = int(problemFile.readline())
    startState = problemFile.readline()
    goalState = problemFile.readline()
    algorithm = problemFile.readline()
    mazeNum = problemFile.readline()

    startStateList = startState.split()
    startStateList[0] = int(startStateList[0])
    startStateList[1] = int(startStateList[1])

    goalStateList = goalState.split()
    goalStateList[0] = int(goalStateList[0])
    goalStateList[1] = int(goalStateList[1])

    # Open maze file
    mazeNum = mazeNum.rstrip('\n')
    mazeFileLocation = "a1/mazes/maze_" + mazeNum + ".txt"
    mazeFile = open(mazeFileLocation)

    # Create the maze
    maze = createMaze(mazeSize, mazeFile)
    #print(np.matrix(maze))

    # Run the selected algorithm
    print(runMaze(int(algorithm), startStateList, goalStateList, maze, mazeSize))