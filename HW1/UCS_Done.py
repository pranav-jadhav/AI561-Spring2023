from queue import PriorityQueue

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

    if algorithm == "UCS":
        uniformCostSearch(start_X, start_Y, stamina, lodges_coordinates, mtrx, height, width)

if __name__ == "__main__":
    main()



