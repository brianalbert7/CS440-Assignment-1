# A Maze Searching program for CS440
# Authors: Brian Albert and Mohamed Moussa

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
 
# Bi-Directional search algorithm
def BDS(startStateList, goalStateList, maze, size):
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
    i = 3
    j = 3
    solutionFound = False
    solutions = []

    closed1.append(startStateList.copy())
    closed2.append(goalStateList.copy())

    # Loop until a solution is found or a fail
    while len(frontier1) != 0 and len(frontier2) != 0:
        # If frontier1 is not empty
        if len(frontier1) != 0:
            # Set node1 as the first value of frontier1
            node1 = frontier1.pop(0)

            # If node1 is the goal or if frontier2 contains node1 we have found the target
            if node1 == goalStateList or node1 in frontier2:
                solutionFound = True

            i = maze[node1[0]][node1[1]] + 1

            # Check neighbors
            # Check left
            if node1[0] != size and node1[1]-1 != size and node1[0] != -1 and node1[1]-1 != -1 and not solutionFound:
                expandArray.append(node1[0])
                expandArray.append(node1[1]-1)
                if maze[node1[0]][node1[1]-1] == 0:
                    candidates1.append(expandArray.copy())
                    maze[expandArray[0]][expandArray[1]] = i

                elif maze[node1[0]][node1[1]-1] > 1 and node1 in closed2:
                    if expandArray in closed2:
                        solutions.append(expandArray.copy())
                        solutionFound = True

                expandArray.clear() 

            # Check right
            if node1[0] != size and node1[1]+1 != size and node1[0] != -1 and node1[1]+1 != -1 and not solutionFound:
                expandArray.append(node1[0])
                expandArray.append(node1[1]+1)
                if maze[node1[0]][node1[1]+1] == 0:
                    candidates1.append(expandArray.copy())
                    maze[expandArray[0]][expandArray[1]] = i

                elif maze[node1[0]][node1[1]+1] > 1:
                    if expandArray in closed2:
                        solutions.append(expandArray.copy())
                        solutionFound = True

                expandArray.clear()

            # Check up
            if node1[0]-1 != size and node1[1] != size and node1[0]-1 != -1 and node1[1] != -1 and not solutionFound:
                expandArray.append(node1[0]-1)
                expandArray.append(node1[1])
                if maze[node1[0]-1][node1[1]] == 0:
                    candidates1.append(expandArray.copy())
                    maze[expandArray[0]][expandArray[1]] = i
                    
                elif maze[node1[0]-1][node1[1]] > 1:
                    if expandArray in closed2:
                        solutions.append(expandArray.copy())
                        solutionFound = True

                expandArray.clear()

            # Check down
            if node1[0]+1 != size and node1[1] != size and node1[0]+1 != -1 and node1[1] != -1 and not solutionFound:
                expandArray.append(node1[0]+1)
                expandArray.append(node1[1])
                if maze[node1[0]+1][node1[1]] == 0:
                    candidates1.append(expandArray.copy())
                    maze[expandArray[0]][expandArray[1]] = i
                    
                elif maze[node1[0]+1][node1[1]] > 1:
                    if expandArray in closed2:
                        solutions.append(expandArray.copy())
                        solutionFound = True

                expandArray.clear()

            # For all neighbors check if they have already been visited and if they are already in the queue
            for c in candidates1:
                if c not in closed1 and c not in frontier1:
                    # If neighbor is good add it to visited and place it in the queue
                    closed1.append(c.copy())
                    frontier1.append(c.copy())
                    
            candidates1.clear()

            
        # If frontier2 is not empty
        if len(frontier2) != 0:
            # Set node2 as the first value of frontier2
            node2 = frontier2.pop(0)

            # If node2 is the goal or if frontier1 contains node2 we have found the target
            if node2 == startStateList or node2 in frontier1:
                solutionFound = True

            j = maze[node2[0]][node2[1]] + 1

            # Check neighbors
            # Check left
            if node2[0] != size and node2[1]-1 != size and node2[0] != -1 and node2[1]-1 != -1 and not solutionFound:
                expandArray.append(node2[0])
                expandArray.append(node2[1]-1)
                if maze[node2[0]][node2[1]-1] == 0:
                    candidates2.append(expandArray.copy())
                    maze[expandArray[0]][expandArray[1]] = j

                elif maze[node2[0]][node2[1]-1] > 1:
                    if expandArray in closed1:
                        solutions.append(expandArray.copy())
                        solutionFound = True

                expandArray.clear() 

            # Check right
            if node2[0] != size and node2[1]+1 != size and node2[0] != -1 and node2[1]+1 != -1 and not solutionFound:
                expandArray.append(node2[0])
                expandArray.append(node2[1]+1)
                if maze[node2[0]][node2[1]+1] == 0:
                    candidates2.append(expandArray.copy())
                    maze[expandArray[0]][expandArray[1]] = j
                    
                elif maze[node2[0]][node2[1]+1] > 1:
                    if expandArray in closed1:
                        solutions.append(expandArray.copy())
                        solutionFound = True

                expandArray.clear()

            # Check up
            if node2[0]-1 != size and node2[1] != size and node2[0]-1 != -1 and node2[1] != -1 and not solutionFound:
                expandArray.append(node2[0]-1)
                expandArray.append(node2[1])
                if maze[node2[0]-1][node2[1]] == 0:
                    candidates2.append(expandArray.copy())
                    maze[expandArray[0]][expandArray[1]] = j
                    
                elif maze[node2[0]-1][node2[1]] > 1:
                    if expandArray in closed1:
                        solutions.append(expandArray.copy())
                        solutionFound = True

                expandArray.clear()

            # Check down
            if node2[0]+1 != size and node2[1] != size and node2[0]+1 != -1 and node2[1] != -1 and not solutionFound:
                expandArray.append(node2[0]+1)
                expandArray.append(node2[1])
                if maze[node2[0]+1][node2[1]] == 0:
                    candidates2.append(expandArray.copy())
                    maze[expandArray[0]][expandArray[1]] = j
                    
                elif maze[node2[0]+1][node2[1]] > 1:
                    if expandArray in closed1:
                        solutions.append(expandArray.copy())
                        solutionFound = True

                expandArray.clear()


            # For all neighbors check if they have already been visited and if they are already in the queue
            for c in candidates2:
                if c not in closed2 and c not in frontier2:
                    # If neighbor is good add it to visited and place it in the queue
                    closed2.append(c.copy())
                    frontier2.append(c.copy())

            candidates2.clear()

            # When the target is reached
            if solutionFound:

                # Check to see if neighbors of the solution are the same as the solution
                solutionX = solutions[0][0]
                solutionY = solutions[0][1]

                intersection = maze[solutionX][solutionY]

                # Check left
                if solutionX != size and solutionY-1 != size and solutionX != -1 and solutionY-1 != -1:
                    if maze[solutionX][solutionY-1] == intersection:
                        expandArray.append(solutionX)
                        expandArray.append(solutionY-1)
                        if (expandArray in closed1 and solutions[0] in closed2) or (expandArray in closed2 and solutions[0] in closed1):
                            solutions.append(expandArray.copy())
                        expandArray.clear()

                # Check right
                if solutionX != size and solutionY+1 != size and solutionX != -1 and solutionY+1 != -1:
                    if maze[solutionX][solutionY+1] == intersection:
                        expandArray.append(solutionX)
                        expandArray.append(solutionY+1)
                        if (expandArray in closed1 and solutions[0] in closed2) or (expandArray in closed2 and solutions[0] in closed1):
                            solutions.append(expandArray.copy())
                        expandArray.clear()

                # Check up
                if solutionX-1 != size and solutionY != size and solutionX-1 != -1 and solutionY != -1:
                    if maze[solutionX-1][solutionY] == intersection:
                        expandArray.append(solutionX-1)
                        expandArray.append(solutionY)
                        if (expandArray in closed1 and solutions[0] in closed2) or (expandArray in closed2 and solutions[0] in closed1):
                            solutions.append(expandArray.copy())
                        expandArray.clear()

                # Check down
                if solutionX+1 != size and solutionY != size and solutionX+1 != -1 and solutionY != -1:
                    if maze[solutionX+1][solutionY] == intersection:
                        expandArray.append(solutionX+1)
                        expandArray.append(solutionY)
                        if (expandArray in closed1 and solutions[0] in closed2) or (expandArray in closed2 and solutions[0] in closed1):
                            solutions.append(expandArray.copy())
                        expandArray.clear()

                # Make sure there are at most two solution points
                solutionIn1 = False
                solutionIn2 = False
                for s in solutions:
                    if s in closed1:
                        if solutionIn1:
                            solutions.remove(s)
                        else:
                            solutionIn1 = True
                    if s in closed2:
                        if solutionIn2:
                            solutions.remove(s)
                        else:
                            solutionIn2 = True

                # Initialize variables
                pathList = []
                path = []
                cost = 0
                path1 = []
                cost1 = 0
                path2 = []
                cost2 = 0
                solution = []

                i = intersection

                # If there are two values in solutions
                if (len(solutions) > 1):
                    if solutions[0] in closed1:
                        x = solutions[0][0]
                        y = solutions[0][1]

                        pathList.append(x)
                        pathList.append(y)
                        path1.append(pathList.copy())
                        pathList.clear()

                        while maze[x][y] != 2:
                            added = False

                            # Check if path goes left
                            if x != size and y-1 != size and x != -1 and y-1 != -1:
                                if maze[x][y-1] == i-1:
                                    pathList.append(x)
                                    pathList.append(y-1)
                                    if not added and pathList in closed1:
                                        path1.append(pathList.copy())
                                        cost1 += 1
                                        y -= 1
                                        added = True
                                    pathList.clear()

                            # Check if path goes right
                            if x != size and y+1 != size and x != -1 and y+1 != -1:
                                if maze[x][y+1] == i-1:
                                    pathList.append(x)
                                    pathList.append(y+1)
                                    if not added and pathList in closed1:
                                        path1.append(pathList.copy())
                                        cost1 += 1
                                        y += 1
                                        added = True
                                    pathList.clear()
                                    
                            # Check if path goes up
                            if x-1 != size and y != size and x-1 != -1 and y != -1:
                                if maze[x-1][y] == i-1:
                                    pathList.append(x-1)
                                    pathList.append(y)
                                    if not added and pathList in closed1:
                                        path1.append(pathList.copy())
                                        cost1 += 2
                                        x -= 1
                                        added = True
                                    pathList.clear()

                            # Check if path goes down
                            if x+1 != size and y != size and x+1 != -1 and y != -1:
                                if maze[x+1][y] == i-1:
                                    pathList.append(x+1)
                                    pathList.append(y)
                                    if not added and pathList in closed1:
                                        path1.append(pathList.copy())
                                        cost1 += 2
                                        x += 1
                                        added = True
                                    pathList.clear()

                            i -= 1

                    if solutions[0] in closed2:
                        x = solutions[0][0]
                        y = solutions[0][1]

                        pathList.append(x)
                        pathList.append(y)
                        path2.append(pathList.copy())
                        pathList.clear()

                        while maze[x][y] != 2:
                            added = False

                            # Check if path goes left
                            if x != size and y-1 != size and x != -1 and y-1 != -1:
                                if maze[x][y-1] == i-1:
                                    pathList.append(x)
                                    pathList.append(y-1)
                                    if not added and pathList in closed2:
                                        path2.append(pathList.copy())
                                        cost2 += 1
                                        y -= 1
                                        added = True
                                    pathList.clear()

                            # Check if path goes right
                            if x != size and y+1 != size and x != -1 and y+1 != -1:
                                if maze[x][y+1] == i-1:
                                    pathList.append(x)
                                    pathList.append(y+1)
                                    if not added and pathList in closed2:
                                        path2.append(pathList.copy())
                                        cost2 += 1
                                        y += 1
                                        added = True
                                    pathList.clear()
                                    
                            # Check if path goes up
                            if x-1 != size and y != size and x-1 != -1 and y != -1:
                                if maze[x-1][y] == i-1:
                                    pathList.append(x-1)
                                    pathList.append(y)
                                    if not added and pathList in closed2:
                                        path2.append(pathList.copy())
                                        cost2 += 2
                                        x -= 1
                                        added = True
                                    pathList.clear()

                            # Check if path goes down
                            if x+1 != size and y != size and x+1 != -1 and y != -1:
                                if maze[x+1][y] == i-1:
                                    pathList.append(x+1)
                                    pathList.append(y)
                                    if not added and pathList in closed2:
                                        path2.append(pathList.copy())
                                        cost2 += 2
                                        x += 1
                                        added = True
                                    pathList.clear()

                            i -= 1

                    i = intersection

                    if solutions[1] in closed1:
                        x = solutions[1][0]
                        y = solutions[1][1]

                        pathList.append(x)
                        pathList.append(y)
                        path1.append(pathList.copy())
                        pathList.clear()

                        while maze[x][y] != 2:
                            added = False

                            # Check if path goes left
                            if x != size and y-1 != size and x != -1 and y-1 != -1:
                                if maze[x][y-1] == i-1:
                                    pathList.append(x)
                                    pathList.append(y-1)
                                    if not added and pathList in closed1:
                                        path1.append(pathList.copy())
                                        cost1 += 1
                                        y -= 1
                                        added = True
                                    pathList.clear()

                            # Check if path goes right
                            if x != size and y+1 != size and x != -1 and y+1 != -1:
                                if maze[x][y+1] == i-1:
                                    pathList.append(x)
                                    pathList.append(y+1)
                                    if not added and pathList in closed1:
                                        path1.append(pathList.copy())
                                        cost1 += 1
                                        y += 1
                                        added = True
                                    pathList.clear()
                                    
                            # Check if path goes up
                            if x-1 != size and y != size and x-1 != -1 and y != -1:
                                if maze[x-1][y] == i-1:
                                    pathList.append(x-1)
                                    pathList.append(y)
                                    if not added and pathList in closed1:
                                        path1.append(pathList.copy())
                                        cost1 += 2
                                        x -= 1
                                        added = True
                                    pathList.clear()

                            # Check if path goes down
                            if x+1 != size and y != size and x+1 != -1 and y != -1:
                                if maze[x+1][y] == i-1:
                                    pathList.append(x+1)
                                    pathList.append(y)
                                    if not added and pathList in closed1:
                                        path1.append(pathList.copy())
                                        cost1 += 2
                                        x += 1
                                        added = True
                                    pathList.clear()

                            i -= 1

                    if solutions[1] in closed2:
                        x = solutions[1][0]
                        y = solutions[1][1]

                        pathList.append(x)
                        pathList.append(y)
                        path2.append(pathList.copy())
                        pathList.clear()

                        while maze[x][y] != 2:
                            added = False

                            # Check if path goes left
                            if x != size and y-1 != size and x != -1 and y-1 != -1:
                                if maze[x][y-1] == i-1:
                                    pathList.append(x)
                                    pathList.append(y-1)
                                    if not added and pathList in closed2:
                                        path2.append(pathList.copy())
                                        cost2 += 1
                                        y -= 1
                                        added = True
                                    pathList.clear()

                            # Check if path goes right
                            if x != size and y+1 != size and x != -1 and y+1 != -1:
                                if maze[x][y+1] == i-1:
                                    pathList.append(x)
                                    pathList.append(y+1)
                                    if not added and pathList in closed2:
                                        path2.append(pathList.copy())
                                        cost2 += 1
                                        y += 1
                                        added = True
                                    pathList.clear()
                                    
                            # Check if path goes up
                            if x-1 != size and y != size and x-1 != -1 and y != -1:
                                if maze[x-1][y] == i-1:
                                    pathList.append(x-1)
                                    pathList.append(y)
                                    if not added and pathList in closed2:
                                        path2.append(pathList.copy())
                                        cost2 += 2
                                        x -= 1
                                        added = True
                                    pathList.clear()

                            # Check if path goes down
                            if x+1 != size and y != size and x+1 != -1 and y != -1:
                                if maze[x+1][y] == i-1:
                                    pathList.append(x+1)
                                    pathList.append(y)
                                    if not added and pathList in closed2:
                                        path2.append(pathList.copy())
                                        cost2 += 2
                                        x += 1
                                        added = True
                                    pathList.clear()

                            i -= 1
                        
                    # Join paths and costs
                    path1.reverse()
                    path = path1 + path2
                    cost = cost1 + cost2

                    solution.append(path)
                    solution.append(cost)

                    return solution

                if len(solutions) == 1:
                    x = solutions[0][0]
                    y = solutions[0][1]

                    pathList.append(x)
                    pathList.append(y)
                    path1.append(pathList.copy())
                    pathList.clear()

                    while maze[x][y] != 2:
                        added = False

                        # Check if path goes left
                        if x != size and y-1 != size and x != -1 and y-1 != -1:
                            if maze[x][y-1] == i-1:
                                pathList.append(x)
                                pathList.append(y-1)
                                if not added and pathList in closed1:
                                    path1.append(pathList.copy())
                                    cost1 += 1
                                    y -= 1
                                    added = True
                                pathList.clear()

                        # Check if path goes right
                        if x != size and y+1 != size and x != -1 and y+1 != -1:
                            if maze[x][y+1] == i-1:
                                pathList.append(x)
                                pathList.append(y+1)
                                if not added and pathList in closed1:
                                    path1.append(pathList.copy())
                                    cost1 += 1
                                    y += 1
                                    added = True
                                pathList.clear()
                                
                        # Check if path goes up
                        if x-1 != size and y != size and x-1 != -1 and y != -1:
                            if maze[x-1][y] == i-1:
                                pathList.append(x-1)
                                pathList.append(y)
                                if not added and pathList in closed1:
                                    path1.append(pathList.copy())
                                    cost1 += 2
                                    x -= 1
                                    added = True
                                pathList.clear()

                        # Check if path goes down
                        if x+1 != size and y != size and x+1 != -1 and y != -1:
                            if maze[x+1][y] == i-1:
                                pathList.append(x+1)
                                pathList.append(y)
                                if not added and pathList in closed1:
                                    path1.append(pathList.copy())
                                    cost1 += 2
                                    x += 1
                                    added = True
                                pathList.clear()

                        i -= 1

                    x = solutions[0][0]
                    y = solutions[0][1]
                    
                    i = intersection

                    while maze[x][y] != 2:
                        added = False

                        # Check if path goes left
                        if x != size and y-1 != size and x != -1 and y-1 != -1:
                            if maze[x][y-1] == i-1:
                                pathList.append(x)
                                pathList.append(y-1)
                                if not added and pathList in closed2:
                                    path2.append(pathList.copy())
                                    cost2 += 1
                                    y -= 1
                                    added = True
                                pathList.clear()

                        # Check if path goes right
                        if x != size and y+1 != size and x != -1 and y+1 != -1:
                            if maze[x][y+1] == i-1:
                                pathList.append(x)
                                pathList.append(y+1)
                                if not added and pathList in closed2:
                                    path2.append(pathList.copy())
                                    cost2 += 1
                                    y += 1
                                    added = True
                                pathList.clear()
                                
                        # Check if path goes up
                        if x-1 != size and y != size and x-1 != -1 and y != -1:
                            if maze[x-1][y] == i-1:
                                pathList.append(x-1)
                                pathList.append(y)
                                if not added and pathList in closed2:
                                    path2.append(pathList.copy())
                                    cost2 += 2
                                    x -= 1
                                    added = True
                                pathList.clear()

                        # Check if path goes down
                        if x+1 != size and y != size and x+1 != -1 and y != -1:
                            if maze[x+1][y] == i-1:
                                pathList.append(x+1)
                                pathList.append(y)
                                if not added and pathList in closed2:
                                    path2.append(pathList.copy())
                                    cost2 += 2
                                    x += 1
                                    added = True
                                pathList.clear()

                        i -= 1

                # Join paths and costs
                path1.reverse()
                path = path1 + path2
                cost = cost1 + cost2

                solution.append(path)
                solution.append(cost)

                return solution

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
        1: BDS,
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
