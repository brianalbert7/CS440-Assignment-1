# A Maze Searching program for CS440
# Authors: Brian Albert and Mohamed Moussa

# Import libraries
import numpy as np
from PriorityQueue import PriorityQueue
import math
import matplotlib.pyplot as plt
from datetime import datetime
start=datetime.now()

# Breadth-first search algorithm
def BFS(startStateList, goalStateList, maze, size):
    # Check if start or goal is a wall
    if maze[startStateList[0]][startStateList[1]] == 1 or maze[goalStateList[0]][goalStateList[1]] == 1:
        print("Starts or ends on a 1")
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
        i = maze[node[0]][node[1]] + 1
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
            solution.append(closed)


            return solution
        
        closed.append(node.copy())

        
    
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
 
# IDDFS algorithm
def IDDFS(startStateList, goalStateList, maze, size):
    # Check if start or goal is a wall
    if maze[startStateList[0]][startStateList[1]] == 1 or maze[goalStateList[0]][goalStateList[1]] == 1:
        print("Starts or ends on a 1")
        return -1

    mazeCopy = [x[:] for x in maze]
    # Initialize the frontier and set it equal to the start state
    for depth in range(1000):
        maze = [x[:] for x in mazeCopy]
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
        j = 0

        # Loop until a solution is found or a fail
        while len(frontier) != 0 and depth != j:
            j += 1
            node = frontier.pop()
        
            # When a solution is found
            i = maze[node[0]][node[1]] + 1
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
                solution.append(closed)


                return solution
            
            closed.append(node.copy())

            
        
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

#
def h4(p1,p2):
    pass

def personalHeuristic(p1,p2):
    return max(computeEuclideanDistance(p1,p2),computeManhattanDistance(p1,p2))
    
# A* algorithm using Euclidean Distance
def A1(startStateList,goalStateList, maze,size):
    #Check if start or goal is a wall
    if maze[startStateList[0]][startStateList[1]] == 1 or maze[goalStateList[0]][goalStateList[1]] == 1:
        return -1

    #Initialize the frontier and set it equal to the start state
    frontier = PriorityQueue()
    startCoordinate = []
    startCoordinate.append(startStateList[0])
    startCoordinate.append(startStateList[1])
    startCoordinate.append(computeEuclideanDistance(startStateList,goalStateList))
    startCoordinate.append(0)
    frontier.insert(startCoordinate)

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
        i = maze[node[0]][node[1]] + 1
        #When a solution is found
        if coordinate == goalStateList:
            
         
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
                #print("[" + str(x) + "," + str(y) + "]")
                #print(i)
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
            solution.append(closed)

            return solution
        closed.append(node.copy())
        
        #Expand the current node
        #Check left
        if node[0] != size and node[1]-1 != size and node[0] != -1 and node[1]-1 != -1:
            if maze[node[0]][node[1]-1] == 0:
                expandArray.append(node[0])
                expandArray.append(node[1] -1)
                expandArray.append(computeEuclideanDistance([node[0],node[1] -1],goalStateList))
                expandArray.append(1 + node[3])
                candidates.append(expandArray.copy())
                maze[expandArray[0]][expandArray[1]] = i
                expandArray.clear()

        # Check right
        if node[0] != size and node[1]+1 != size and node[0] != -1 and node[1]+1 != -1:
            if maze[node[0]][node[1]+1] == 0:
                expandArray.append(node[0])
                expandArray.append(node[1]+1)
                expandArray.append(computeEuclideanDistance([node[0],node[1] +1],goalStateList))
                expandArray.append(1 + node[3])
                candidates.append(expandArray.copy())
                maze[expandArray[0]][expandArray[1]] = i
                expandArray.clear()

        # Check up
        if node[0]-1 != size and node[1] != size and node[0]-1 != -1 and node[1] != -1:
            if maze[node[0]-1][node[1]] == 0:
                expandArray.append(node[0]-1)
                expandArray.append(node[1])
                expandArray.append(computeEuclideanDistance([node[0] -1,node[1]],goalStateList))
                expandArray.append(2 + node[3])
                candidates.append(expandArray.copy())
                maze[expandArray[0]][expandArray[1]] = i
                expandArray.clear()

        # Check down
        if node[0]+1 != size and node[1] != size and node[0]+1 != -1 and node[1] != -1:
            if maze[node[0]+1][node[1]] == 0:
                expandArray.append(node[0]+1)
                expandArray.append(node[1])
                expandArray.append(computeEuclideanDistance([node[0] +1,node[1]],goalStateList))
                expandArray.append(2 + node[3])
                candidates.append(expandArray.copy())
                maze[expandArray[0]][expandArray[1]] = i
                expandArray.clear()

        
        for c in candidates:
            if c not in closed and c not in frontier.queue:
                frontier.insert(c.copy())

        candidates.clear()
    print("no solution found")
    return -1

# A* algorithm using h4
def A2(startStateList,goalStateList,maze,size):
    #Check if start or goal is a wall
    if maze[startStateList[0]][startStateList[1]] == 1 or maze[goalStateList[0]][goalStateList[1]] == 1:
        return -1

    #Initialize the frontier and set it equal to the start state
    frontier = PriorityQueue()
    startCoordinate = []
    startCoordinate.append(startStateList[0])
    startCoordinate.append(startStateList[1])
    startCoordinate.append(h3(startStateList,goalStateList))
    startCoordinate.append(0)
    frontier.insert(startCoordinate)

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
        i = maze[node[0]][node[1]] + 1
        #When a solution is found
        if coordinate == goalStateList:
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
            solution.append(closed)

            return solution
        closed.append(node.copy())

       

        #Expand the current node
        #Check left
        if node[0] != size and node[1]-1 != size and node[0] != -1 and node[1]-1 != -1:
            if maze[node[0]][node[1]-1] == 0:
                expandArray.append(node[0])
                expandArray.append(node[1] -1)
                expandArray.append(h3([node[0],node[1] -1],goalStateList))
                expandArray.append(1 + node[3])
                candidates.append(expandArray.copy())
                maze[expandArray[0]][expandArray[1]] = i
                expandArray.clear()

        # Check right
        if node[0] != size and node[1]+1 != size and node[0] != -1 and node[1]+1 != -1:
            if maze[node[0]][node[1]+1] == 0:
                expandArray.append(node[0])
                expandArray.append(node[1]+1)
                expandArray.append(h3([node[0],node[1] +1],goalStateList))
                expandArray.append(1 + node[3])
                candidates.append(expandArray.copy())
                maze[expandArray[0]][expandArray[1]] = i
                expandArray.clear()

        # Check up
        if node[0]-1 != size and node[1] != size and node[0]-1 != -1 and node[1] != -1:
            if maze[node[0]-1][node[1]] == 0:
                expandArray.append(node[0]-1)
                expandArray.append(node[1])
                expandArray.append(h3([node[0] -1,node[1]],goalStateList))
                expandArray.append(2 + node[3])
                candidates.append(expandArray.copy())
                maze[expandArray[0]][expandArray[1]] = i
                expandArray.clear()

        # Check down
        if node[0]+1 != size and node[1] != size and node[0]+1 != -1 and node[1] != -1:
            if maze[node[0]+1][node[1]] == 0:
                expandArray.append(node[0]+1)
                expandArray.append(node[1])
                expandArray.append(h3([node[0] +1,node[1]],goalStateList))
                expandArray.append(2 + node[3])
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
def A3(startStateList,goalStateList,maze,size):
     #Check if start or goal is a wall
    if maze[startStateList[0]][startStateList[1]] == 1 or maze[goalStateList[0]][goalStateList[1]] == 1:
        return -1

    #Initialize the frontier and set it equal to the start state
    frontier = PriorityQueue()
    startCoordinate = []
    startCoordinate.append(startStateList[0])
    startCoordinate.append(startStateList[1])
    startCoordinate.append(h3(startStateList,goalStateList))
    startCoordinate.append(0)
    frontier.insert(startCoordinate)

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
        i = maze[node[0]][node[1]] + 1
        #When a solution is found
        if coordinate == goalStateList:
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
            solution.append(closed)

            return solution
        closed.append(node.copy())

       

        #Expand the current node
        #Check left
        if node[0] != size and node[1]-1 != size and node[0] != -1 and node[1]-1 != -1:
            if maze[node[0]][node[1]-1] == 0:
                expandArray.append(node[0])
                expandArray.append(node[1] -1)
                expandArray.append(personalHeuristic([node[0],node[1] -1],goalStateList))
                expandArray.append(1 + node[3])
                candidates.append(expandArray.copy())
                maze[expandArray[0]][expandArray[1]] = i
                expandArray.clear()

        # Check right
        if node[0] != size and node[1]+1 != size and node[0] != -1 and node[1]+1 != -1:
            if maze[node[0]][node[1]+1] == 0:
                expandArray.append(node[0])
                expandArray.append(node[1]+1)
                expandArray.append(personalHeuristic([node[0],node[1] +1],goalStateList))
                expandArray.append(1 + node[3])
                candidates.append(expandArray.copy())
                maze[expandArray[0]][expandArray[1]] = i
                expandArray.clear()

        # Check up
        if node[0]-1 != size and node[1] != size and node[0]-1 != -1 and node[1] != -1:
            if maze[node[0]-1][node[1]] == 0:
                expandArray.append(node[0]-1)
                expandArray.append(node[1])
                expandArray.append(personalHeuristic([node[0] -1,node[1]],goalStateList))
                expandArray.append(2 + node[3])
                candidates.append(expandArray.copy())
                maze[expandArray[0]][expandArray[1]] = i
                expandArray.clear()

        # Check down
        if node[0]+1 != size and node[1] != size and node[0]+1 != -1 and node[1] != -1:
            if maze[node[0]+1][node[1]] == 0:
                expandArray.append(node[0]+1)
                expandArray.append(node[1])
                expandArray.append(personalHeuristic([node[0] +1,node[1]],goalStateList))
                expandArray.append(2 + node[3])
                candidates.append(expandArray.copy())
                maze[expandArray[0]][expandArray[1]] = i
                expandArray.clear()
       
        for c in candidates:
            if c not in closed and c not in frontier.queue:
                frontier.insert(c.copy())

        candidates.clear()
    print("no solution found")
    return -1

 
# Method to run the correct algorithm
def runMaze(algorithm, ssl, gsl, maze, size):
    switcher = {
        0: BFS,
        1: IDDFS,
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

        while len(solution[2]) != 0:
            mazeCopy[solution[2][0][0]][solution[2][0][1]] = [161, 161, 161]
            solution[2].pop(0)

        pathCopy = path
        while len(pathCopy) != 0:
            mazeCopy[pathCopy[0][0]][pathCopy[0][1]] = 2
            pathCopy.pop(0)

        for i in range(mazeSize):
            for j in range(mazeSize):
                if mazeCopy[i][j] == 1:
                    mazeCopy[i][j] = [0, 0, 0]
                if mazeCopy[i][j] == 0:
                    mazeCopy[i][j] = [255, 255, 255]
                if mazeCopy[i][j] == 2:
                    mazeCopy[i][j] = [0, 255, 230]
        mazeCopy[startStateList[0]][startStateList[1]] = [0, 255, 0]
        mazeCopy[goalStateList[0]][goalStateList[1]] = [255, 0, 0]
        
        plt.axis('off')
        plt.imshow(mazeCopy)
        plt.show()
    print(datetime.now()-start)
