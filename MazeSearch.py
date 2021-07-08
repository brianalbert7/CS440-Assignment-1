# A Maze Searching program for CS440
# Authors: Brian Albert

# Import libraries
import numpy as np
from PriorityQueue import PriorityQueue
import math
# Breadth-first search algorithm
def BFS(startStateList, goalStateList, maze, size):
    # Check if start or goal is a wall
    if maze[startStateList[0]][startStateList[1]] == 1 or maze[goalStateList[0]][goalStateList[1]] == 1:
        return -1

    # Initialize the frontier and set it equal to the start state
    frontier = []
    frontier.append(startStateList)

    # Represent the start point as 2 on the maze
    maze[startStateList[0]][startStateList[1]] = 2

    # Initialize other variables
    closed = []
    candidates = []
    expandArray = []
    node = []
    i = 0

    # Loop until a solution is found or a fail
    while len(frontier) != 0:
        node = frontier.pop(0)
        
        # When a solution is found
        if node == goalStateList:
            solution = []
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

            solution.append(path)
            solution.append(cost)

            return solution
        
        closed.append(node.copy())

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

        candidates.clear()

    return -1
 
# Depth-limited search algorithm
def DLS(startStateList, goalStateList, maze, size):
    # Check if start or goal is a wall
    if maze[startStateList[0]][startStateList[1]] == 1 or maze[goalStateList[0]][goalStateList[1]]:
        return -1

    # Initialize the frontier and set it equal to the start state
    frontier1 = []
    frontier1.append(startStateList)
    frontier2 = []
    frontier2.append(goalStateList)

    # Represent the start point as 2 on the maze
    maze[startStateList[0]][startStateList[1]] = 2
    maze[goalStateList[0]][goalStateList[1]] = 2

    # Initialize other variables
    closed1 = []
    closed2 = []
    candidates1 = []
    candidates2 = []
    expandArray = []
    node1 = []
    node2 = []
    prevMaze = []
    i = 0
    j = 0
    solutionFound = False

    # Loop until a solution is found or a fail
    while len(frontier1) != 0 and len(frontier2) != 0:
        print(np.matrix(maze))
        node1 = frontier1.pop(0)
        node2 = frontier2.pop(0)
        
        closed1.append(node1.copy())
        closed2.append(node2.copy())

        i = maze[node1[0]][node1[1]] + 1
        j = maze[node2[0]][node2[1]] + 1

        # Expand the current node1
        # Check left
        if node1[0] != size and node1[1]-1 != size and node1[0] != -1 and node1[1]-1 != -1:
            expandArray.append(node1[0])
            expandArray.append(node1[1]-1)
            if maze[node1[0]][node1[1]-1] == 0:
                candidates1.append(expandArray.copy())
                maze[expandArray[0]][expandArray[1]] = i

            elif maze[node1[0]][node1[1]-1] > 1 and node1 in closed2:
                if expandArray in closed2:
                    solutionFound = True

            expandArray.clear() 

        # Check right
        if node1[0] != size and node1[1]+1 != size and node1[0] != -1 and node1[1]+1 != -1:
            expandArray.append(node1[0])
            expandArray.append(node1[1]+1)
            if maze[node1[0]][node1[1]+1] == 0:
                candidates1.append(expandArray.copy())
                maze[expandArray[0]][expandArray[1]] = i

            elif maze[node1[0]][node1[1]+1] > 1:
                if expandArray in closed2:
                    solutionFound = True

            expandArray.clear()

        # Check up
        if node1[0]-1 != size and node1[1] != size and node1[0]-1 != -1 and node1[1] != -1:
            expandArray.append(node1[0]-1)
            expandArray.append(node1[1])
            if maze[node1[0]-1][node1[1]] == 0:
                candidates1.append(expandArray.copy())
                maze[expandArray[0]][expandArray[1]] = i
                
            elif maze[node1[0]-1][node1[1]] > 1:
                if expandArray in closed2:
                    solutionFound = True

            expandArray.clear()

        # Check down
        if node1[0]+1 != size and node1[1] != size and node1[0]+1 != -1 and node1[1] != -1:
            expandArray.append(node1[0]+1)
            expandArray.append(node1[1])
            if maze[node1[0]+1][node1[1]] == 0:
                candidates1.append(expandArray.copy())
                maze[expandArray[0]][expandArray[1]] = i
                
            elif maze[node1[0]+1][node1[1]] > 1:
                if expandArray in closed2:
                    solutionFound = True

            expandArray.clear()

        # Expand the current node2
        # Check left
        if node2[0] != size and node2[1]-1 != size and node2[0] != -1 and node2[1]-1 != -1:
            expandArray.append(node2[0])
            expandArray.append(node2[1]-1)
            if maze[node2[0]][node2[1]-1] == 0:
                candidates2.append(expandArray.copy())
                maze[expandArray[0]][expandArray[1]] = j

            elif maze[node2[0]][node2[1]-1] > 1:
                if expandArray in closed1:
                    solutionFound = True

            expandArray.clear() 

        # Check right
        if node2[0] != size and node2[1]+1 != size and node2[0] != -1 and node2[1]+1 != -1:
            expandArray.append(node2[0])
            expandArray.append(node2[1]+1)
            if maze[node2[0]][node2[1]+1] == 0:
                candidates2.append(expandArray.copy())
                maze[expandArray[0]][expandArray[1]] = j
                
            elif maze[node2[0]][node2[1]+1] > 1:
                if expandArray in closed1:
                    solutionFound = True

            expandArray.clear()

        # Check up
        if node2[0]-1 != size and node2[1] != size and node2[0]-1 != -1 and node2[1] != -1:
            expandArray.append(node2[0]-1)
            expandArray.append(node2[1])
            if maze[node2[0]-1][node2[1]] == 0:
                candidates2.append(expandArray.copy())
                maze[expandArray[0]][expandArray[1]] = j
                
            elif maze[node2[0]-1][node2[1]] > 1:
                if expandArray in closed1:
                    solutionFound = True

            expandArray.clear()

        # Check down
        if node2[0]+1 != size and node2[1] != size and node2[0]+1 != -1 and node2[1] != -1:
            expandArray.append(node2[0]+1)
            expandArray.append(node2[1])
            if maze[node2[0]+1][node2[1]] == 0:
                candidates2.append(expandArray.copy())
                maze[expandArray[0]][expandArray[1]] = j
                
            elif maze[node2[0]+1][node2[1]] > 1:
                if expandArray in closed1:
                    solutionFound = True

            expandArray.clear()

        print(np.matrix(maze))

        # When the searches intersect, a solution is given, so return the solution
        if solutionFound:
            solution = []
            x = goalStateList[0]
            y = goalStateList[1]
            path = []
            pathList = []
            cost = 0

            pathList.append(x)
            pathList.append(y)
            path.append(pathList.copy())
            pathList.clear()

        for c in candidates1:
            if c not in closed1 and c not in frontier1:
                frontier1.append(c.copy())

        for c in candidates2:
            if c not in closed2 and c not in frontier2:
                frontier2.append(c.copy())

        candidates1.clear()
        candidates2.clear()
        prevMaze = [x[:] for x in maze]

    print(np.matrix(maze))
    return -1
 

def computeEuclideanDistance(p1, p2):
    xDiff = p2[0] - p1[0]
    yDiff = p2[1] - p1[1]
    xDiff = abs(xDiff)
    yDiff = abs(yDiff)
    return math.sqrt((xDiff**2) + (yDiff**2))

def computeManhattanDistance(p1,p2):
    xDiff =p2[0] - p1[0]
    yDiff = p2[1] - p1[1]
    xDiff = abs(xDiff)
    yDiff = abs(yDiff)
    return xDiff + yDiff

#min of Manhattan Distance and Euclidean Distance
def h3(p1,p2):
    return min(computeEuclideanDistance(p1,p2),computeManhattanDistance(p1,p2))

def personalHeuristic(p1,p2):
    pass
    
# A* algorithm using h
def A1(startStateList,goalStateList, maze,size):
    #Check if start or goal is a wall
    if maze[startStateList[0]][startStateList[1]] == 1 or maze[goalStateList[0]][goalStateList[1]] == 1:
        return -1

    #Initialize the frontier and set it equal to the start state
    frontier = PriorityQueue()
    frontier.queue.append(startStateList)

    #Represent the start point as 2 on the maze
    maze[startStateList[0]][startStateList[1]] = 2


    # Initialize other variables
    closed = []
    candidates = []
    expandArray = []
    node = []
    i = 0

        #Loop until a solution is found or a fail
    while len(frontier.queue) != 0:
        node = frontier.pop()
        coordinate = []
        coordinate.append(node[0])
        coordinate.append(node[1])
        #When a solution is found
        if coordinate == goalStateList:
            print("match")
            solution = []
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

            solution.append(path)
            solution.append(cost)

            return solution
        closed.append(node.copy())

        i = maze[node[0]][node[1]] + 1

        #Expand the current node
        #Check down
        if node[0] != size and node[1]-1 != size and node[0] != -1 and node[1]-1 != -1:
            if maze[node[0]][node[1]-1] == 0:
                expandArray.append(node[0])
                expandArray.append(node[1] -1)
                expandArray.append(h3([node[0],node[1] -1],goalStateList))
                maze[expandArray[0]][expandArray[1]] = i
                expandArray.clear()

        # Check up
        if node[0] != size and node[1]+1 != size and node[0] != -1 and node[1]+1 != -1:
            if maze[node[0]][node[1]+1] == 0:
                expandArray.append(node[0])
                expandArray.append(node[1]+1)
                expandArray.append(h3([node[0],node[1] +1],goalStateList))
                candidates.append(expandArray.copy())
                maze[expandArray[0]][expandArray[1]] = i
                expandArray.clear()

        # Check left
        if node[0]-1 != size and node[1] != size and node[0]-1 != -1 and node[1] != -1:
            if maze[node[0]-1][node[1]] == 0:
                expandArray.append(node[0]-1)
                expandArray.append(node[1])
                expandArray.append(h3([node[0] -1,node[1]],goalStateList))
                candidates.append(expandArray.copy())
                maze[expandArray[0]][expandArray[1]] = i
                expandArray.clear()

        # Check right
        if node[0]+1 != size and node[1] != size and node[0]+1 != -1 and node[1] != -1:
            if maze[node[0]+1][node[1]] == 0:
                expandArray.append(node[0]+1)
                expandArray.append(node[1])
                expandArray.append(h3([node[0] +1,node[1]],goalStateList))
                candidates.append(expandArray.copy())
                maze[expandArray[0]][expandArray[1]] = i
                expandArray.clear()

        for c in candidates:
            if c not in closed and c not in frontier.queue:
                frontier.insert(c.copy())

        candidates.clear()
    print("no solution found")
    return -1

# A* algorithm using h
def A2(startStateList,goalStateList,maze,size):
    #Check if start or goal is a wall
    if maze[startStateList[0]][startStateList[1]] == 1 or maze[goalStateList[0]][goalStateList[1]] == 1:
        return -1

    #Initialize the frontier and set it equal to the start state
    frontier = PriorityQueue()
    frontier.queue.append(startStateList)

    #Represent the start point as 2 on the maze
    maze[startStateList[0]][startStateList[1]] = 2


    # Initialize other variables
    closed = []
    candidates = []
    expandArray = []
    node = []
    i = 0

        #Loop until a solution is found or a fail
    while len(frontier.queue) != 0:
        node = frontier.pop()
        coordinate = []
        coordinate.append(node[0])
        coordinate.append(node[1])
        #When a solution is found
        if coordinate == goalStateList:
            print("match")
            solution = []
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

            solution.append(path)
            solution.append(cost)

            return solution
        closed.append(node.copy())

        i = maze[node[0]][node[1]] + 1

        #Expand the current node
        #Check down
        if node[0] != size and node[1]-1 != size and node[0] != -1 and node[1]-1 != -1:
            if maze[node[0]][node[1]-1] == 0:
                expandArray.append(node[0])
                expandArray.append(node[1] -1)
                expandArray.append(computeEuclideanDistance([node[0],node[1] -1],goalStateList))
                maze[expandArray[0]][expandArray[1]] = i
                expandArray.clear()

        # Check up
        if node[0] != size and node[1]+1 != size and node[0] != -1 and node[1]+1 != -1:
            if maze[node[0]][node[1]+1] == 0:
                expandArray.append(node[0])
                expandArray.append(node[1]+1)
                expandArray.append(computeEuclideanDistance([node[0],node[1] +1],goalStateList))
                candidates.append(expandArray.copy())
                maze[expandArray[0]][expandArray[1]] = i
                expandArray.clear()

        # Check left
        if node[0]-1 != size and node[1] != size and node[0]-1 != -1 and node[1] != -1:
            if maze[node[0]-1][node[1]] == 0:
                expandArray.append(node[0]-1)
                expandArray.append(node[1])
                expandArray.append(computeEuclideanDistance([node[0] -1,node[1]],goalStateList))
                candidates.append(expandArray.copy())
                maze[expandArray[0]][expandArray[1]] = i
                expandArray.clear()

        # Check right
        if node[0]+1 != size and node[1] != size and node[0]+1 != -1 and node[1] != -1:
            if maze[node[0]+1][node[1]] == 0:
                expandArray.append(node[0]+1)
                expandArray.append(node[1])
                expandArray.append(computeEuclideanDistance([node[0] +1,node[1]],goalStateList))
                candidates.append(expandArray.copy())
                maze[expandArray[0]][expandArray[1]] = i
                expandArray.clear()

        for c in candidates:
            if c not in closed and c not in frontier.queue:
                frontier.insert(c.copy())

        candidates.clear()
    print("no solution found")
    return -1

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
    mazeCopy = [x[:] for x in maze]

    # Run the selected algorithm
    solution = runMaze(int(algorithm), startStateList, goalStateList, maze, mazeSize)
    
    if solution == -1:
        print("No valid solution")
    else:
        # Save the found path and cost
        path = solution[0]
        cost = solution[1]

        print("Path:")
        print(path)

        print("Cost:")
        print(cost)

        print("Resulting maze and path: ")

        pathCopy = path
        while len(pathCopy) != 0:
            mazeCopy[pathCopy[0][0]][pathCopy[0][1]] = 2
            pathCopy.pop(0)

        print(np.matrix(mazeCopy))
