from queue import PriorityQueue

# BFS Functions

def isVisitedBFS(X, Y, visited):
    key = (X, Y)
    if key in visited.keys():
        return True
    return False

def printInFile2(res):
    fp = open("output.txt", 'a')
    fp.write(res.strip() + "\n")

def printInFile(visited, node):
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
                printInFile(visited, (lodge[1], lodge[0]))
            else:
                printInFile2("FAIL")  
# USC Functions

def deleteNode(open_queue, X, Y):
    temp = PriorityQueue()

    while not open_queue.empty():
        t = open_queue.get()
        if t[1] == X and t[2] == Y:
            while not temp.empty():
                open_queue.put(temp.get())
            return
        temp.put(t)

def isPresent(ky, mp):
    if ky in mp.keys():
        return True; 

def isVisited(visited, X, Y):
    key = str(X) + str(Y)
    if key in visited.keys():
        return True
    return False

def expandUCS(children, cost, X, Y, visited, height, width, mtrx, stamina, children_map, parent):
    extraCost = 10
    if isValid(height, width, X-1, Y, mtrx, stamina, X, Y) and not isVisited(visited, X-1, Y): # North
        children.put((cost + extraCost, X-1, Y))
        children_map[(str(X-1) + str(Y))] = cost + extraCost
    if isValid(height, width, X, Y+1, mtrx, stamina, X, Y) and not isVisited(visited, X-1, Y): # East
        children.put((cost + extraCost, X, Y+1))
        children_map[(str(X) + str(Y+1))] = cost + extraCost
    if isValid(height, width, X+1, Y, mtrx, stamina, X, Y) and not isVisited(visited, X-1, Y): # South
        children.put((cost + extraCost, X+1, Y))
        children_map[(str(X+1) + str(Y))] = cost + extraCost
    if isValid(height, width, X, Y+1, mtrx, stamina, X, Y) and not isVisited(visited, X-1, Y): # West
        children.put((cost + extraCost, X, Y+1))
        children_map[(str(X) + str(Y+1))] = cost + extraCost

    extraCost = 14
    if isValid(height, width, X-1, Y+1, mtrx, stamina, X, Y) and not (str(X-1) + str(Y+1)) in visited.keys(): # NorthEast
        children.put((cost + extraCost, X-1, Y+1))
        children_map[(str(X-1) + str(Y+1))] = cost + extraCost
    if isValid(height, width, X+1, Y+1, mtrx, stamina, X, Y) and not (str(X+1) + str(Y+1)) in visited.keys(): # SouthEast
        children.put((cost + extraCost, X+1, Y+1))
        children_map[(str(X+1) + str(Y+1))] = cost + extraCost
    if isValid(height, width, X+1, Y-1, mtrx, stamina, X, Y) and not (str(X+1) + str(Y-1)) in visited.keys(): # SouthWest
        children.put((cost + extraCost, X+1, Y-1))
        children_map[(str(X+1) + str(Y-1))] = cost + extraCost
    if isValid(height, width, X-1, Y-1, mtrx, stamina, X, Y) and not (str(X-1) + str(Y-1)) in visited.keys(): # NorthWest
        children.put((cost + extraCost, X-1, Y-1))
        children_map[(str(X-1) + str(Y-1))] = cost + extraCost

def uniformCostSearch(start_Y, start_X, stamina, lodges_coordinates, mtrx, height, width):
    print(start_X, start_Y)
    for lodge in lodges_coordinates:
        open_queue = PriorityQueue()
        close = PriorityQueue()
        visited = {}
        open_queue_map = {}
        closed_map = {}
        children_map = {}
        parent = {}
        parent[(str(start_X) + str(start_Y))] = ""
        open_queue.put((0, start_X, start_Y))
        open_queue_map[str(start_X) + str(start_Y)] = 0
        visited[str(start_X) + str(start_Y)] = 0

        while not open_queue.empty():
            currNode = open_queue.get()
            del open_queue_map[(str(currNode[1]) + str(currNode[2]))]

            if tuple((currNode[1], currNode[2])) == lodge:
                printInFileUCS(parent, str(currNode[1]) + str(currNode[2]))
                break

            children = PriorityQueue()
            expandUCS(children, currNode[0], currNode[1], currNode[2], visited, height, width, mtrx, stamina, children_map, parent)

            
            while not children.empty():
                child = children.get()
                
                if (str(child[1]) + str(child[2])) in children_map.keys():
                    del children_map[(str(child[1]) + str(child[2]))]
            
                if not isPresent((str(child[1]) + str(child[2])), open_queue_map) and not isPresent((str(child[1]) + str(child[2])), closed_map):
                    open_queue.put((child[0], child[1], child[2]))
                    open_queue_map[str(child[1]) + str(child[2])] = child[0]
                    parent[str(child[1]) + str(child[2])] = str(currNode[1]) + str(currNode[2])
                elif isPresent((str(child[1]) + str(child[2])), open_queue_map):
                    if open_queue_map[str(child[1]) + str(child[2])] > child[0]:
                        deleteNode(open_queue, child[1], child[2])
                        open_queue.put(child)
                        open_queue_map[str(child[1]) + str(child[2])] = child[0]
                        parent[str(child[1]) + str(child[2])] = str(currNode[1]) + str(currNode[2])
                elif isPresent((str(child[1]) + str(child[2])), closed_map):
                    if closed_map[str(child[1]) + str(child[2])] > child[0]:
                        deleteNode(close, child[1], child[2])
                        open_queue.put(child)
                        open_queue_map[str(child[1]) + str(child[2])] = child[0]
                        parent[str(child[1]) + str(child[2])] = str(currNode[1]) + str(currNode[2])
            
            close.put(currNode)
            closed_map[str(currNode[1]) + str(currNode[2])] = currNode[0]
        fp = open("output.txt", 'a')
        fp.write("FAIL\n")

def printInFileUCS(parent, key):

    stack = []
    stack.append(key)
    while len(parent[key]):
        stack.append(parent[key])
        key = parent[key]

    fp = open("output.txt", "a")
    pth = ""
    while(stack):
        temp = stack.pop()
        pth = pth + temp[1] + "," + temp[0] + " "
    
    fp.write(pth.strip() + "\n")

# Common Functions

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

def isValid(height, width, X, Y, mtrx, stamina, curr_X, curr_Y):
    if X > -1 and X < height and Y > -1 and Y < width:
        if (mtrx[X][Y] < 0 and abs(mtrx[curr_X][curr_Y]) >= abs(mtrx[X][Y])) or (abs(mtrx[curr_X][curr_Y]) >= abs(mtrx[X][Y])) or (abs(mtrx[curr_X][curr_Y]) < abs(mtrx[X][Y]) and (abs(mtrx[X][Y]) - abs(mtrx[curr_X][curr_Y])) <= stamina):
            return True
    return False

if __name__ == "__main__":
    main()
