# A Maze Searching program for CS440
# Authors: Brian Albert

# Import libraries
import numpy as np

# Breadth-first search algorithm
def BFS():
    return "zero"
 
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
def runMaze(algorithm):
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
    return func()

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
        while i == x:
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
    startStateX = startStateList[0]
    startStateY = startStateList[1]

    goalStateList = goalState.split()
    goalStateX = goalStateList[0]
    goalStateY = goalStateList[1]

    # Open maze file
    mazeNum = mazeNum.rstrip('\n')
    mazeFileLocation = "a1/mazes/maze_" + mazeNum + ".txt"
    mazeFile = open(mazeFileLocation)

    # Create the maze
    maze = createMaze(mazeSize, mazeFile)
    print(np.matrix(maze))

    # Run the selected algorithm
    print(runMaze(int(algorithm)))