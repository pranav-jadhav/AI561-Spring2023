from queue import PriorityQueue

# Common Functions



# BFS Functions




##UCS Functions

def getIndex(X, Y, open):
    for i in range(0, len(open)):
        if open[i][1][0] == X and open[i][1][1] == Y:
            return i

def isVisitedUCS(X, Y, visited):
    pass

def expandUCS(children, X, Y, height, width, mtrx, stamina, visited, cost):
    extraCost = 10
    if isValid(height, width, X-1, Y, mtrx, stamina, X, Y) and not isVisitedUCS(X-1, Y, visited):    # North
        children.put((cost + extraCost, tuple((X-1, Y))))
        # path[tuple((X-1, Y))] = tuple((X,Y))
    if isValid(height, width, X, Y+1, mtrx, stamina, X, Y) and not isVisitedUCS(X, Y+1, visited):    # East
        children.put((cost + extraCost, tuple((X, Y+1))))
        # path[tuple((X, Y+1))] = tuple((X,Y))
    if isValid(height, width, X+1, Y, mtrx, stamina, X, Y) and not isVisitedUCS(X+1, Y, visited):    # South
        children.put((cost + extraCost, tuple((X+1, Y))))
        # path[tuple((X+1, Y))] = tuple((X,Y))
    if isValid(height, width, X, Y-1, mtrx, stamina, X, Y) and not isVisitedUCS(X, Y-1, visited):    # West
        children.put((cost + extraCost, tuple((X, Y-1))))
        # path[tuple((X, Y-1))] = tuple((X,Y))
    
    cost = 14
    if isValid(height, width, X-1, Y+1, mtrx, stamina, X, Y) and not isVisitedUCS(X-1, Y+1, visited):    # NorthEast
        children.put((cost + extraCost, tuple((X-1, Y+1))))
        # path[tuple((X-1, Y+1))] = tuple((X,Y))
    if isValid(height, width, X+1, Y+1, mtrx, stamina, X, Y) and not isVisitedUCS(X+1, Y+1, visited):    # SouthEast
        children.put((cost + extraCost, tuple((X+1, Y+1))))
        # path[tuple((X+1, Y+1))] = tuple((X,Y))
    if isValid(height, width, X+1, Y-1, mtrx, stamina, X, Y) and not isVisitedUCS(X+1, Y-1, visited):    # SouthWest
        children.put((cost + extraCost, tuple((X+1, Y-1))))
        # path[tuple((X+1, Y-1))] = tuple((X,Y))
    if isValid(height, width, X-1, Y-1, mtrx, stamina, X, Y) and not isVisitedUCS(X-1, Y-1, visited):    # NorthWest
        children.put((cost + extraCost, tuple((X-1, Y-1))))
        # path[tuple((X-1, Y-1))] = tuple((X,Y))

def uniformCostSearch(start_X, start_Y, stamina, lodges_coordinates, mtrx, height, width):
    print("UCS")
    
    for lodge in lodges_coordinates:
        open = PriorityQueue()
        openList = []
        close = PriorityQueue()
        closeList = []
        visited = []

        open.put((0, tuple((start_X, start_Y))))

        while not open.empty():
            currNode = open.get()
            openList.remove(tuple((str(currNode[1][0]), str(currNode[1][1]))))
            if currNode == lodge:
                print(currNode)
                break
            children = PriorityQueue()
            expandUCS(children, currNode[1][0], currNode[1][1], height, width, mtrx, stamina, visited, currNode[0])
            while children:
                child = children.get()
                if tuple((str(child[1][0]), str(child[1][1]))) not in visited:
                    open.put(child)
                    openList.append(tuple((str(child[1][0]), str(child[1][1]))))
                elif tuple((str(child[1][0]), str(child[1][1]))) in openList:
                    nodeIdx = getIndex(child[1][0], child[1][0], open)
                    if child[0] < open[nodeIdx][0]:
                        open.



            close.put((currNode[0], tuple((currNode[1][0], currNode[1][1]))))
            closeList.append(tuple((str(currNode[1][0]), str(currNode[1][1]))))
            visited.append(tuple((str(currNode[1][0]), str(currNode[1][1]))))
