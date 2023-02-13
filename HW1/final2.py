from queue import PriorityQueue

# BFS Functions

def isVisitedBFS(X, Y, visited):
    key = (X, Y)
    if key in visited.keys():
        return True
    return False

def printInFileBFS2(res):
    fp = open("output.txt", 'a')
    fp.write(res.strip() + "\n")

def printInFileBFS(visited, node):
    fp = open("output.txt", 'a')
    res = ""
    stack = []

    while visited[node] != "":
        stack.append(node)
        node = visited[node]

    stack.append(node)

    while stack:
        t = stack.pop()
        fp.write(str(t[1]) + "," + str(t[0]) + " ")
    
    fp.write("\n")
    
def expand(queue, height, width, X, Y, mtrx, stamina, visited):
    if isValid(height, width, X-1, Y, mtrx, stamina, X, Y) and not isVisitedBFS(X-1, Y, visited):    # North
        queue.append(tuple((X-1, Y)))
        visited[((X-1), (Y))] = (X, Y)
    if isValid(height, width, X-1, Y+1, mtrx, stamina, X, Y) and not isVisitedBFS(X-1, Y+1, visited):    # NorthEast
        queue.append(tuple((X-1, Y+1))) 
        visited[((X-1), (Y+1))] = (X, Y)
    if isValid(height, width, X, Y+1, mtrx, stamina, X, Y) and not isVisitedBFS(X, Y+1, visited):    # East
        queue.append(tuple((X, Y+1)))
        visited[((X), (Y+1))] = (X, Y)
    if isValid(height, width, X+1, Y+1, mtrx, stamina, X, Y) and not isVisitedBFS(X+1, Y+1, visited):    # SouthEast
        queue.append(tuple((X+1, Y+1)))
        visited[((X+1), (Y+1))] = (X, Y)
    if isValid(height, width, X+1, Y, mtrx, stamina, X, Y) and not isVisitedBFS(X+1, Y, visited):    # South
        queue.append(tuple((X+1, Y)))
        visited[((X+1), (Y))] = (X, Y)
    if isValid(height, width, X+1, Y-1, mtrx, stamina, X, Y) and not isVisitedBFS(X+1, Y-1, visited):    # SouthWest
        queue.append(tuple((X+1, Y-1))) 
        visited[((X+1), (Y-1))] = (X, Y)
    if isValid(height, width, X, Y-1, mtrx, stamina, X, Y) and not isVisitedBFS(X, Y-1, visited):    # West
        queue.append(tuple((X, Y-1)))
        visited[((X), (Y-1))] = (X, Y)
    if isValid(height, width, X-1, Y-1, mtrx, stamina, X, Y) and not isVisitedBFS(X-1, Y-1, visited):    # NorthWest
        queue.append(tuple((X-1, Y-1)))
        visited[((X-1), (Y-1))] = (X, Y)

def breadthFirstSearch(start_Y, start_X, stamina, lodges_coordinates, mtrx, height, width):
        queue = []
        visited = {}

        queue.append(tuple((start_X, start_Y)))
        visited[(start_X, start_Y)] = ""

        while queue:
            node = queue.pop(0)
            expand(queue, height, width, node[0], node[1], mtrx, stamina, visited)

        for lodge in lodges_coordinates:
            if (lodge[1], lodge[0]) in visited.keys():
                printInFileBFS(visited, (lodge[1], lodge[0]))
            else:
                printInFileBFS2("FAIL")  

# UCS Functions

def printPath(visited, key):
    stack = []

    while visited[key]:
        stack.append(key) 
        key = visited[key]

    stack.append(key)

    fp = open("output.txt", 'a')

    while stack:
        t = stack.pop()
        fp.write(str(t[1]) + "," + str(t[0]) + " ")
    
    fp.write("\n")

def printPath2():
    fp = open("output.txt", 'a')
    fp.write("FAIL" + "\n")

def isVisitedUCS(pQueue, X, Y):
    if pQueue.empty():
        return False
    lt = pQueue.queue

    for ele in lt:
        if ele[1] == X and ele[2] == Y:
           return True
    
    return False

def isValid(height, width, X, Y, mtrx, stamina, curr_X, curr_Y):
    if X > -1 and X < height and Y > -1 and Y < width:
        if (mtrx[X][Y] < 0 and abs(mtrx[curr_X][curr_Y]) >= abs(mtrx[X][Y])) or (abs(mtrx[curr_X][curr_Y]) >= abs(mtrx[X][Y])) or (abs(mtrx[curr_X][curr_Y]) < abs(mtrx[X][Y]) and (abs(mtrx[X][Y]) - abs(mtrx[curr_X][curr_Y])) <= stamina):
            return True
    return False

def expandUCS(children, parentCost, X, Y, close, height, width, mtrx, stamina):
    extraCost = 10
    if isValid(height, width, X-1, Y, mtrx, stamina, X, Y) and not isVisitedUCS(close, X-1, Y):
        children.put((parentCost + extraCost, X-1, Y))
    if isValid(height, width, X, Y+1, mtrx, stamina, X, Y) and not isVisitedUCS(close, X, Y+1):
        children.put((parentCost + extraCost, X, Y+1))    
    if isValid(height, width, X+1, Y, mtrx, stamina, X, Y) and not isVisitedUCS(close, X+1, Y):
        children.put((parentCost + extraCost, X+1, Y))
    if isValid(height, width, X, Y+1, mtrx, stamina, X, Y) and not isVisitedUCS(close, X, Y+1):
        children.put((parentCost + extraCost, X, Y+1))
    
    extraCost = 14
    if isValid(height, width, X-1, Y+1, mtrx, stamina, X, Y) and not isVisitedUCS(close, X-1, Y+1):
        children.put((parentCost + extraCost, X-1, Y+1))
    if isValid(height, width, X+1, Y+1, mtrx, stamina, X, Y) and not isVisitedUCS(close, X+1, Y+1):
        children.put((parentCost + extraCost, X+1, Y+1))
    if isValid(height, width, X+1, Y-1, mtrx, stamina, X, Y) and not isVisitedUCS(close, X+1, Y-1):
        children.put((parentCost + extraCost, X+1, Y-1))
    if isValid(height, width, X-1, Y-1, mtrx, stamina, X, Y) and not isVisitedUCS(close, X-1, Y-1):
        children.put((parentCost + extraCost, X-1, Y-1))

def ifExists(pQueue, X, Y):

    if pQueue.empty():
        return False

    for ele in pQueue.queue:
        if ele[1] == X and ele[2] == Y:
            return ele
    return False

def uniformCostSearch(start_Y, start_X, stamina, lodges_coordinates, mtrx, height, width):
    for lodge in lodges_coordinates:
        open_q = PriorityQueue()
        close = PriorityQueue()
        flag = 1
        visited = {}

        open_q.put((0, start_X, start_Y))
        visited[(start_X, start_Y)] = ""

        while not open_q.empty():
            currNode = open_q.get()

            if tuple((currNode[1], currNode[2])) == (lodge[1], lodge[0]):
                printPath(visited, (currNode[1], currNode[2]))
                flag = 0
                break

            children = PriorityQueue()
            expandUCS(children, currNode[0], currNode[1], currNode[2], close, height, width, mtrx, stamina)
            
            while not children.empty():
                child = children.get()
                checkOpen = ifExists(open_q, child[1], child[2])
                checkClosed = ifExists(close, child[1], child[2])

                if not checkOpen and not checkClosed:
                    open_q.put(child)
                    visited[(child[1], child[2])] = (currNode[1], currNode[2])
                elif checkOpen != False:
                    if child[0] < checkOpen[0]:
                        open_q.queue.remove(checkOpen)
                        open_q.put(child)
                        visited[(child[1], child[2])] = (currNode[1], currNode[2])
                elif checkClosed != False:
                    if child[0] < checkClosed[0]:
                        close.queue.remove(checkClosed)
                        open_q.put(child)               
            
            close.put(currNode)
        if flag == 1:
            printPath2()

# A* Functions

def calcPathCost(Enext, Ecurr, M):
    if Enext - Ecurr <= M:
        return 0
    else:
        return max(0, Enext - Ecurr - M)

def ifExistsAS(pQueue, X, Y):
    if pQueue.empty():
        return False

    for ele in pQueue.queue:
        if ele[1] == X and ele[2] == Y:
            return ele
    return False

def isVisited(pQueue, X, Y):
    key = (X, Y)

    if key in pQueue.keys():
        return True
    return False

def calcMomemtum(prev_X, prev_Y, curr_X, curr_Y, mtrx):
    return max(0, (abs(mtrx[int(prev_X)][int(prev_Y)]) - abs(mtrx[curr_X][curr_Y])))

def allowedMoves(Momentum, curr_X, curr_Y, next_X, next_Y, mtrx, stamina, height, width):
    if next_X < 0 or next_X >= height or next_Y < 0 or next_Y >= width:
        return False

    if (mtrx[next_X][next_Y]) < 0 and abs(mtrx[next_X][next_Y]) > abs(mtrx[curr_X][curr_Y]):
        return False

    elev_next = abs(mtrx[next_X][next_Y])

    if (elev_next < abs(mtrx[curr_X][curr_Y])) or (elev_next <= abs(mtrx[curr_X][curr_Y]) + stamina + Momentum):
        return True
    return False 

def heuristic(curr_X, curr_Y, lodge_X, lodge_Y):
    return (pow(curr_X - lodge_X, 2) + pow(curr_Y - lodge_Y, 2))

def removeFromopen_queue(open_queue, X, Y):
    temp = []
    while not open_queue.empty():
        node = open_queue.get()
        if node[2][0] == X and node[2][1] == Y:
            break
        temp.append(node)

    while temp:
        open_queue.put(temp.pop())

def expandAS(X, Y, mtrx, height, width, stamina, open_queue, parent_cost, lodge, parent, close):
    
    if allowedMoves(calcMomemtum(parent[(X, Y)][0], parent[(X, Y)][1], X, Y, mtrx), X, Y, X-1, Y, mtrx, stamina, height, width):   # North
        if not isVisited(parent, X-1, Y):
            Mmtm = calcMomemtum(parent[(X, Y)][0], parent[(X, Y)][1], X, Y, mtrx)
            h = 10
            g = calcPathCost(abs(mtrx[X-1][Y]), abs(mtrx[X][Y]), Mmtm)
            heur = heuristic(X-1, Y, lodge[1], lodge[0])
            open_queue.put((parent_cost + heur + h + g, parent_cost + h + g, (X-1, Y), Mmtm))
            parent[(X-1, Y)] = (X, Y)

        ele = ifExistsAS(open_queue, X-1, Y)
        if ele != False and ele[1] > parent_cost + 10 + calcPathCost(abs(mtrx[X-1][Y]), abs(mtrx[X][Y]), Mmtm):
            open_queue.queue.remove(ele)
            Mmtm = calcMomemtum(parent[(X, Y)][0], parent[(X, Y)][1], X, Y, mtrx)
            h = 10
            g = calcPathCost(abs(mtrx[X-1][Y]), abs(mtrx[X][Y]), Mmtm)
            heur = heuristic(X-1, Y, lodge[1], lodge[0])
            open_queue.put((parent_cost + heur + h + g, parent_cost + h + g, (X-1, Y), Mmtm))
            parent[((X-1, Y))] = (X, Y)

        ele = ifExistsAS(close, X-1, Y)
        if ele != False and ele[1] > parent_cost + 10 + calcPathCost(abs(mtrx[X-1][Y]), abs(mtrx[X][Y]), Mmtm):
            close.queue.remove(ele)
            Mmtm = calcMomemtum(parent[(X, Y)][0], parent[(X, Y)][1], X, Y, mtrx)
            if ele[3] < Mmtm:
                h = 10
                g = calcPathCost(abs(mtrx[X-1][Y]), abs(mtrx[X][Y]), Mmtm)
                heur = heuristic(X-1, Y, lodge[1], lodge[0])
                open_queue.put((parent_cost + heur + h + g, parent_cost + h + g, (X-1, Y), Mmtm))
                parent[((X-1, Y))] = (X, Y)

    if allowedMoves(calcMomemtum(parent[(X, Y)][0], parent[(X, Y)][1], X, Y, mtrx), X, Y, X, Y+1, mtrx, stamina, height, width):   # East
        if not isVisited(parent, X, Y+1):
            Mmtm = calcMomemtum(parent[(X, Y)][0], parent[(X, Y)][1], X, Y, mtrx)
            h = 10
            g = calcPathCost(abs(mtrx[X][Y+1]), abs(mtrx[X][Y]), Mmtm)
            heur = heuristic(X, Y+1, lodge[1], lodge[0])
            open_queue.put((parent_cost + heur + h + g, parent_cost + h + g, (X, Y+1), Mmtm))
            parent[(X,Y+1)] = (X, Y)
        
        ele = ifExistsAS(open_queue, X, Y+1)
        if ele != False and ele[1] > parent_cost + 10 + calcPathCost(abs(mtrx[X][Y+1]), abs(mtrx[X][Y]), Mmtm):
            open_queue.queue.remove(ele)
            Mmtm = calcMomemtum(parent[(X, Y)][0], parent[(X, Y)][1], X, Y, mtrx)
            h = 10
            g = calcPathCost(abs(mtrx[X][Y+1]), abs(mtrx[X][Y]), Mmtm)
            heur = heuristic(X, Y+1, lodge[1], lodge[0])
            open_queue.put((parent_cost + heur + h + g, parent_cost + h + g, (X, Y+1), Mmtm))
            parent[((X, Y+1))] = (X, Y)

        ele = ifExistsAS(close, X, Y+1)
        if ele != False and ele[1] > parent_cost + 10 + calcPathCost(abs(mtrx[X][Y+1]), abs(mtrx[X][Y]), Mmtm):
            close.queue.remove(ele)
            Mmtm = calcMomemtum(parent[(X, Y)][0], parent[(X, Y)][1], X, Y, mtrx)
            if ele[3] < Mmtm:
                h = 10
                g = calcPathCost(abs(mtrx[X][Y+1]), abs(mtrx[X][Y]), Mmtm)
                heur = heuristic(X, Y+1, lodge[1], lodge[0])
                open_queue.put((parent_cost + heur + h + g, parent_cost + h + g, (X, Y+1), Mmtm))
                parent[((X, Y+1))] = (X, Y)

    if allowedMoves(calcMomemtum(parent[(X, Y)][0], parent[(X, Y)][1], X, Y, mtrx), X, Y, X+1, Y, mtrx, stamina, height, width):   # South
        if not isVisited(parent, X+1, Y):
            Mmtm = calcMomemtum(parent[(X, Y)][0], parent[(X, Y)][1], X, Y, mtrx)
            h = 10
            g = calcPathCost(abs(mtrx[X+1][Y]), abs(mtrx[X][Y]), Mmtm)
            heur = heuristic(X+1, Y, lodge[1], lodge[0])
            open_queue.put((parent_cost + heur + h + g, parent_cost + h + g, (X+1, Y), Mmtm))
            parent[(X+1,Y)] = (X, Y)
        ele = ifExistsAS(open_queue, X+1, Y)
        if ele != False and ele[1] > parent_cost + 10 + calcPathCost(abs(mtrx[X+1][Y]), abs(mtrx[X][Y]), Mmtm):
            open_queue.queue.remove(ele)
            Mmtm = calcMomemtum(parent[(X, Y)][0], parent[(X, Y)][1], X, Y, mtrx)
            h = 10
            g = calcPathCost(abs(mtrx[X+1][Y]), abs(mtrx[X][Y]), Mmtm)
            heur = heuristic(X+1, Y, lodge[1], lodge[0])
            open_queue.put((parent_cost + heur + h + g, parent_cost + h + g, (X+1, Y), Mmtm))
            parent[((X+1, Y))] = (X, Y)
        
        ele = ifExistsAS(close, X+1, Y)
        if ele != False and ele[1] > parent_cost + 10 + calcPathCost(abs(mtrx[X+1][Y]), abs(mtrx[X][Y]), Mmtm):
            close.queue.remove(ele)
            Mmtm = calcMomemtum(parent[(X, Y)][0], parent[(X, Y)][1], X, Y, mtrx)
            if ele[3] < Mmtm:
                h = 10
                g = calcPathCost(abs(mtrx[X+1][Y]), abs(mtrx[X][Y]), Mmtm)
                heur = heuristic(X+1, Y, lodge[1], lodge[0])
                open_queue.put((parent_cost + heur + h + g, parent_cost + h + g, (X+1, Y), Mmtm))
                parent[((X+1, Y))] = (X, Y)

    if allowedMoves(calcMomemtum(parent[(X, Y)][0], parent[(X, Y)][1], X, Y, mtrx), X, Y, X, Y-1, mtrx, stamina, height, width):   # West
        if not isVisited(parent, X, Y-1):
            Mmtm = calcMomemtum(parent[(X, Y)][0], parent[(X, Y)][1], X, Y, mtrx)
            h = 10
            g = calcPathCost(abs(mtrx[X][Y-1]), abs(mtrx[X][Y]), Mmtm)
            heur = heuristic(X, Y-1, lodge[1], lodge[0])
            open_queue.put((parent_cost + heur + h + g, parent_cost + h + g, (X, Y-1), Mmtm))
            parent[(X, Y-1)] = (X, Y)
        ele = ifExistsAS(open_queue, X, Y-1)
        if ele != False and ele[1] > parent_cost + 10 + calcPathCost(abs(mtrx[X][Y-1]), abs(mtrx[X][Y]), Mmtm):
            open_queue.queue.remove(ele)
            Mmtm = calcMomemtum(parent[(X, Y)][0], parent[(X, Y)][1], X, Y, mtrx)
            h = 10
            g = calcPathCost(abs(mtrx[X][Y-1]), abs(mtrx[X][Y]), Mmtm)
            heur = heuristic(X, Y-1, lodge[1], lodge[0])
            open_queue.put((parent_cost + heur + h + g, parent_cost + h + g, (X, Y-1), Mmtm))
            parent[((X, Y-1))] = (X, Y)
        
        ele = ifExistsAS(close, X, Y-1)
        if ele != False and ele[1] > parent_cost + 10 + calcPathCost(abs(mtrx[X][Y-1]), abs(mtrx[X][Y]), Mmtm):
            close.queue.remove(ele)
            Mmtm = calcMomemtum(parent[(X, Y)][0], parent[(X, Y)][1], X, Y, mtrx)
            if ele[3] < Mmtm:
                h = 10
                g = calcPathCost(abs(mtrx[X][Y-1]), abs(mtrx[X][Y]), Mmtm)
                heur = heuristic(X, Y-1, lodge[1], lodge[0])
                open_queue.put((parent_cost + heur + h + g, parent_cost + h + g, (X, Y-1), Mmtm))
                parent[((X, Y-1))] = (X, Y)


    if allowedMoves(calcMomemtum(parent[(X, Y)][0], parent[(X, Y)][1], X, Y, mtrx), X, Y, X-1, Y+1, mtrx, stamina, height, width):   # NorthEast
        if not isVisited(parent, X-1, Y+1):
            Mmtm = calcMomemtum(parent[(X, Y)][0], parent[(X, Y)][1], X, Y, mtrx)
            h = 14
            g = calcPathCost(abs(mtrx[X-1][Y+1]), abs(mtrx[X][Y]), Mmtm)
            heur = heuristic(X-1, Y+1, lodge[1], lodge[0])
            open_queue.put((parent_cost + heur + h + g, parent_cost + h + g, (X-1, Y+1), Mmtm))
            parent[(X-1,Y+1)] = (X, Y)
        ele = ifExistsAS(open_queue, X-1, Y+1)
        if ele != False and ele[1] > parent_cost + 14 + calcPathCost(abs(mtrx[X-1][Y+1]), abs(mtrx[X][Y]), Mmtm):
            open_queue.queue.remove(ele)
            Mmtm = calcMomemtum(parent[(X, Y)][0], parent[(X, Y)][1], X, Y, mtrx)
            h = 14
            g = calcPathCost(abs(mtrx[X-1][Y+1]), abs(mtrx[X][Y]), Mmtm)
            heur = heuristic(X-1, Y+1, lodge[1], lodge[0])
            open_queue.put((parent_cost + heur + h + g, parent_cost + h + g, (X-1, Y+1), Mmtm))
            parent[((X-1, Y+1))] = (X, Y)
        ele = ifExistsAS(close, X-1, Y+1)
        if ele != False and ele[1] > parent_cost + 10 + calcPathCost(abs(mtrx[X-1][Y+1]), abs(mtrx[X][Y]), Mmtm):
            close.queue.remove(ele)
            Mmtm = calcMomemtum(parent[(X, Y)][0], parent[(X, Y)][1], X, Y, mtrx)
            if ele[3] < Mmtm:
                h = 10
                g = calcPathCost(abs(mtrx[X-1][Y+1]), abs(mtrx[X][Y]), Mmtm)
                heur = heuristic(X-1, Y+1, lodge[1], lodge[0])
                open_queue.put((parent_cost + heur + h + g, parent_cost + h + g, (X-1, Y+1), Mmtm))
                parent[((X-1, Y+1))] = (X, Y)



    if allowedMoves(calcMomemtum(parent[(X, Y)][0], parent[(X, Y)][1], X, Y, mtrx), X, Y, X+1, Y+1, mtrx, stamina, height, width):   # SouthEast
        if not isVisited(parent, X+1, Y+1):
            Mmtm = calcMomemtum(parent[(X, Y)][0], parent[(X, Y)][1], X, Y, mtrx)
            h = 14
            g = calcPathCost(abs(mtrx[X+1][Y+1]), abs(mtrx[X][Y]), Mmtm)
            heur = heuristic(X+1, Y+1, lodge[1], lodge[0])
            open_queue.put((parent_cost + heur + h + g, parent_cost + h + g, (X+1, Y+1), Mmtm))
            parent[(X+1,Y+1)] = (X, Y)
        
        ele = ifExistsAS(open_queue, X+1, Y+1)
        if ele != False and ele[1] > parent_cost + 14 + calcPathCost(abs(mtrx[X+1][Y+1]), abs(mtrx[X][Y]), Mmtm):
            open_queue.queue.remove(ele)
            Mmtm = calcMomemtum(parent[(X, Y)][0], parent[(X, Y)][1], X, Y, mtrx)
            h = 14
            g = calcPathCost(abs(mtrx[X+1][Y+1]), abs(mtrx[X][Y]), Mmtm)
            heur = heuristic(X+1, Y+1, lodge[1], lodge[0])
            open_queue.put((parent_cost + heur + h + g, parent_cost + h + g, (X+1, Y+1), Mmtm))
            parent[((X+1, Y+1))] = (X, Y)

        ele = ifExistsAS(close, X+1, Y+1)
        if ele != False and ele[1] > parent_cost + 10 + calcPathCost(abs(mtrx[X+1][Y+1]), abs(mtrx[X][Y]), Mmtm):
            close.queue.remove(ele)
            Mmtm = calcMomemtum(parent[(X, Y)][0], parent[(X, Y)][1], X, Y, mtrx)
            if ele[3] < Mmtm:
                h = 10
                g = calcPathCost(abs(mtrx[X+1][Y+1]), abs(mtrx[X][Y]), Mmtm)
                heur = heuristic(X+1, Y+1, lodge[1], lodge[0])
                open_queue.put((parent_cost + heur + h + g, parent_cost + h + g, (X+1, Y+1), Mmtm))
                parent[((X+1, Y+1))] = (X, Y)

    if allowedMoves(calcMomemtum(parent[(X, Y)][0], parent[(X, Y)][1], X, Y, mtrx), X, Y, X+1, Y-1, mtrx, stamina, height, width):   # SouthWest
        if not isVisited(parent, X+1, Y-1):
            Mmtm = calcMomemtum(parent[(X, Y)][0], parent[(X, Y)][1], X, Y, mtrx)
            h = 14
            g = calcPathCost(abs(mtrx[X+1][Y-1]), abs(mtrx[X][Y]), Mmtm)
            heur = heuristic(X+1, Y-1, lodge[1], lodge[0])
            open_queue.put((parent_cost + heur + h + g, parent_cost + h + g, (X+1, Y-1), Mmtm))
            parent[(X+1,Y-1)] = (X, Y)
        
        ele = ifExistsAS(open_queue, X+1, Y-1)
        if ele != False and ele[1] > parent_cost + 14 + calcPathCost(abs(mtrx[X+1][Y-1]), abs(mtrx[X][Y]), Mmtm):
            open_queue.queue.remove(ele)
            Mmtm = calcMomemtum(parent[(X, Y)][0], parent[(X, Y)][1], X, Y, mtrx)
            h = 14
            g = calcPathCost(abs(mtrx[X+1][Y-1]), abs(mtrx[X][Y]), Mmtm)
            heur = heuristic(X+1, Y-1, lodge[1], lodge[0])
            open_queue.put((parent_cost + heur + h + g, parent_cost + h + g, (X+1, Y-1), Mmtm))
            parent[((X+1, Y-1))] = (X, Y)

        ele = ifExistsAS(close, X+1, Y-1)
        if ele != False and ele[1] > parent_cost + 10 + calcPathCost(abs(mtrx[X+1][Y-1]), abs(mtrx[X][Y]), Mmtm):
            close.queue.remove(ele)
            Mmtm = calcMomemtum(parent[(X, Y)][0], parent[(X, Y)][1], X, Y, mtrx)
            if ele[3] < Mmtm:
                h = 10
                g = calcPathCost(abs(mtrx[X+1][Y-1]), abs(mtrx[X][Y]), Mmtm)
                heur = heuristic(X+1, Y-1, lodge[1], lodge[0])
                open_queue.put((parent_cost + heur + h + g, parent_cost + h + g, (X+1, Y-1), Mmtm))
                parent[((X+1, Y-1))] = (X, Y)

    if allowedMoves(calcMomemtum(parent[(X, Y)][0], parent[(X, Y)][1], X, Y, mtrx), X, Y, X-1, Y-1, mtrx, stamina, height, width):   # NorthWest
        if not isVisited(parent, X-1, Y-1):
            Mmtm = calcMomemtum(parent[(X, Y)][0], parent[(X, Y)][1], X, Y, mtrx)
            h = 14
            g = calcPathCost(abs(mtrx[X-1][Y-1]), abs(mtrx[X][Y]), Mmtm)
            heur = heuristic(X-1, Y-1, lodge[1], lodge[0])
            open_queue.put((parent_cost + heur + h + g, parent_cost + h + g, (X-1, Y-1), Mmtm))
            parent[(X-1,Y-1)] = (X, Y)
        ele = ifExistsAS(open_queue, X-1, Y-1)
        if ele != False and ele[1] > parent_cost + 14 + calcPathCost(abs(mtrx[X-1][Y-1]), abs(mtrx[X][Y]), Mmtm):
            open_queue.queue.remove(ele)
            Mmtm = calcMomemtum(parent[(X, Y)][0], parent[(X, Y)][1], X, Y, mtrx)
            h = 14
            g = calcPathCost(abs(mtrx[X-1][Y-1]), abs(mtrx[X][Y]), Mmtm)
            heur = heuristic(X-1, Y-1, lodge[1], lodge[0])
            open_queue.put((parent_cost + heur + h + g, parent_cost + h + g, (X-1, Y-1), Mmtm))
            parent[((X-1, Y-1))] = (X, Y)
        
        ele = ifExistsAS(close, X-1, Y-1)
        if ele != False and ele[1] > parent_cost + 10 + calcPathCost(abs(mtrx[X-1][Y-1]), abs(mtrx[X][Y]), Mmtm):
            close.queue.remove(ele)
            Mmtm = calcMomemtum(parent[(X, Y)][0], parent[(X, Y)][1], X, Y, mtrx)
            if ele[3] < Mmtm:
                h = 10
                g = calcPathCost(abs(mtrx[X-1][Y-1]), abs(mtrx[X][Y]), Mmtm)
                heur = heuristic(X-1, Y-1, lodge[1], lodge[0])
                open_queue.put((parent_cost + heur + h + g, parent_cost + h + g, (X-1, Y-1), Mmtm))
                parent[((X-1, Y-1))] = (X, Y)

def printInFileAS(visited, node):
    print(node)
    print(visited)
    fp = open("output.txt", 'a')
    res = ""
    stack = []

    while not (visited[node][0] == node[0] and visited[node][1] == node[1]):
        stack.append(node)
        node = visited[node]
    stack.append(node)

    while stack:
        t = stack.pop()
        fp.write(str(t[1]) + "," + str(t[0]) + " ")
    
    fp.write("\n")

def printInFile2AS():
    fp = open("output.txt", 'a')
    fp.write("FAIL\n")

def aStarSearch(start_X, start_Y, stamina, lodge_coordinates, mtrx, height, width):
    for lodge in lodge_coordinates:
        flag = 1
        parent = {}

        open_queue = PriorityQueue()
        close = PriorityQueue()

        open_queue.put((0 + heuristic(start_X, start_Y, lodge[1], lodge[0]), 0, (start_Y, start_X), 0))
        
        parent[(start_Y, start_X)] = (start_Y, start_X)

        while not open_queue.empty():
            currNode = open_queue.get()
            
            if (currNode[2][0] == lodge[1]) and currNode[2][1] == lodge[0]:
                printInFileAS(parent, (lodge[1], lodge[0]))
                flag = 0
                break

            expandAS(currNode[2][0], currNode[2][1], mtrx, height, width, stamina, open_queue, currNode[1], lodge, parent, close)
            close.put(currNode) 

        if flag == 1:
            printInFile2AS()


# Main Function

def main():
    input_file = open("input.txt", "r")
    lines = input_file.readlines()
    data = [line.strip() for line in lines]

    algorithm = data[0] #algortihm to be used
    data[1] = data[1].split(" ")
    width, height = int(data[1][0]), int(data[1][1]) #get height and width of mtrx3

    data[2] = data[2].split(" ")
    start_X, start_Y = int(data[2][0]), int(data[2][1]) #get starting coordinates

    stamina = int(data[3])

    no_of_lodges = int(data[4])

    lodges_coordinates = []

    for i in range(0, no_of_lodges):
        data[4+1+i] = data[4+1+i].split(" ")
        temp = (int(data[4+1+i][0]), int(data[4+1+i][1]))
        lodges_coordinates.append(temp)
        i = i+1

    mtrx = []

    for i in range(0, height):
        idx = 4 + no_of_lodges + i + 1
        data[idx] = data[idx].split(" ")
        res = [eval(i) for i in data[idx]]
        mtrx.append(res)
        i = i + 1

    output_file = fp = open('output.txt', 'w')

    if algorithm == "BFS":
        breadthFirstSearch(start_X, start_Y, stamina, lodges_coordinates, mtrx, height, width)
    elif algorithm == "UCS":
        uniformCostSearch(start_X, start_Y, stamina, lodges_coordinates, mtrx, height, width)
    else:
        aStarSearch(start_X, start_Y, stamina, lodges_coordinates, mtrx, height, width)

if __name__ == "__main__":
    main()