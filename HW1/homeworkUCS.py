from queue import PriorityQueue

def main():
    input_file = open("input.txt", "r")
    lines = input_file.readlines()
    data = [line.strip() for line in lines]

    algorithm = data[0] #algortihm to be used

    data[1] = data[1].split(" ")
    width, height = int(data[1][0]), int(data[1][1]) #get height and width of mtrx3

    data[2] = data[2].split(" ")
    start_Y, start_X = int(data[2][0]), int(data[2][1]) #get starting coordinates

    stamina = int(data[3])

    no_of_lodges = int(data[4])

    lodges_coordinates = []

    for i in range(0, no_of_lodges):
        data[4+1+i] = data[4+1+i].split(" ")
        temp = (int(data[4+1+i][1]), int(data[4+1+i][0]))
        lodges_coordinates.append(temp)

    print("Lodges: ", lodges_coordinates)
    print("****************************")

    mtrx = []

    for i in range(0, height):
        idx = 4 + no_of_lodges + i + 1
        data[idx] = data[idx].split(" ")
        res = [eval(i) for i in data[idx]]
        mtrx.append(res)
    
    print("Matrix: ", mtrx)
    print("****************************")

    output_file = fp = open('output.txt', 'w')

    if algorithm == "UCS":
        uniformCostSearch(start_X, start_Y, stamina, lodges_coordinates, mtrx, height, width)

# USC Functions

def deleteNode(open, X, Y):
    temp = PriorityQueue()

    while not open.empty():
        t = open.get()
        if t[1] == X and t[2] == Y:
            while not temp.empty():
                open.put(temp.get())
            return
        temp.put(t)

def isPresent(ky, mp):
    if ky in mp.keys():
        return True; 

def isValid(height, width, X, Y, mtrx, stamina, curr_X, curr_Y):
    if X > -1 and X < height and Y > -1 and Y < width:
        if (mtrx[X][Y] < 0 and mtrx[curr_X][curr_Y] >= mtrx[X][Y]) or (mtrx[curr_X][curr_Y] >= mtrx[X][Y]) or (mtrx[curr_X][curr_Y] < mtrx[X][Y] and (mtrx[X][Y] - mtrx[curr_X][curr_Y]) <= stamina):
            return True
    return False

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

def uniformCostSearch(start_X, start_Y, stamina, lodges_coordinates, mtrx, height, width):
    for lodge in lodges_coordinates:
        open = PriorityQueue()
        close = PriorityQueue()
        visited = {}
        open_map = {}
        closed_map = {}
        children_map = {}
        parent = {}
        parent[(str(start_X) + str(start_Y))] = ""
        open.put((0, start_X, start_Y))
        open_map[str(start_X) + str(start_Y)] = 0
        visited[str(start_X) + str(start_Y)] = 0

        print("Initially: ")
        print("Open: ", open_map)
        print("Close: ", closed_map)
        print("-----------------------------------------------------------")
        while not open.empty():
            currNode = open.get()
            del open_map[(str(currNode[1]) + str(currNode[2]))]

            print("currNode: ", currNode)

            print("Check:", (currNode[1], currNode[2]), mtrx[currNode[1]][currNode[2]], lodge, mtrx[lodge[0]][lodge[1]])

            if tuple((currNode[1], currNode[2])) == lodge:
                print(currNode)
                print("YAAAAAAAAAAAAAAYYYYYYYYYYYYYYYYYYYYYYYYYYY")
                print(str(currNode[1]), str(currNode[2]), "565656565656656565")
                printInFileUCS(parent, str(currNode[1]) + str(currNode[2]))
                break

            children = PriorityQueue()
            expandUCS(children, currNode[0], currNode[1], currNode[2], visited, height, width, mtrx, stamina, children_map, parent)
            print("children_map: ", children_map)
            
            while not children.empty():
                child = children.get()
                
                if (str(child[1]) + str(child[2])) in children_map.keys():
                    del children_map[(str(child[1]) + str(child[2]))]
            
                if not isPresent((str(child[1]) + str(child[2])), open_map) and not isPresent((str(child[1]) + str(child[2])), closed_map):
                    open.put((child[0], child[1], child[2]))
                    open_map[str(child[1]) + str(child[2])] = child[0]
                    parent[str(child[1]) + str(child[2])] = str(currNode[1]) + str(currNode[2])
                elif isPresent((str(child[1]) + str(child[2])), open_map):
                    if open_map[str(child[1]) + str(child[2])] > child[0]:
                        deleteNode(open, child[1], child[2])
                        open.put(child)
                        open_map[str(child[1]) + str(child[2])] = child[0]
                        parent[str(child[1]) + str(child[2])] = str(currNode[1]) + str(currNode[2])
                elif isPresent((str(child[1]) + str(child[2])), closed_map):
                    if closed_map[str(child[1]) + str(child[2])] > child[0]:
                        deleteNode(close, child[1], child[2])
                        del closed_map[str(child[1]) + str(child[2])]
                        open.put(child)
                        open_map[str(child[1]) + str(child[2])] = child[0]
                        parent[str(child[1]) + str(child[2])] = str(currNode[1]) + str(currNode[2])
            
            close.put(currNode)
            closed_map[str(currNode[1]) + str(currNode[2])] = currNode[0]
            print("After while: open_map: ", open_map)
            print("After while: closed_map: ", closed_map)
            print("After while: childred_map: ", children_map)
            print("-------------------------------------------------------------")
            print("-------------------------------------------------------------")
        print(parent)

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
    print(stack)

if __name__ == "__main__":
    main()