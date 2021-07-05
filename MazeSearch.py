# A Maze Searching program for CS440
# Authors: Brian Albert

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

# Driver Method
if __name__ == "__main__":
    # Open problem.txt and save information
    problemFile = open("a1/problem.txt", "r")

    mazeSize = problemFile.readline()
    startState = problemFile.readline()
    goalState = problemFile.readline()
    algorithm = problemFile.readline()
    maze = problemFile.readline()

    startStateList = startState.split()
    startStateX = startStateList[0]
    startStateY = startStateList[1]

    goalStateList = goalState.split()
    goalStateX = goalStateList[0]
    goalStateY = goalStateList[1]

    # Open maze file
    maze = maze.rstrip('\n')
    mazeFileLocation = "a1/mazes/maze_" + maze + ".txt"
    mazeFile = open(mazeFileLocation)

    # Run the selected algorithm
    print(runMaze(int(algorithm)))