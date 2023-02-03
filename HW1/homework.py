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

# BFS Functions

def isValid(height, width, X, Y, mtrx, stamina, curr_X, curr_Y):
    if X > -1 and X < height and Y > -1 and Y < width:
        if (mtrx[X][Y] < 0 and mtrx[curr_X][curr_Y] >= mtrx[X][Y]) or (mtrx[curr_X][curr_Y] >= mtrx[X][Y]) or (mtrx[curr_X][curr_Y] < mtrx[X][Y] and (mtrx[X][Y] - mtrx[curr_X][curr_Y]) <= stamina):
            return True
    return False

def isVisitedBFS(X, Y, visited):
    temp = tuple((str(X), str(Y)))
    if temp in visited:
        return True

    visited.append(temp)
    return False

def printInFile(path, node):
    stack = []
    while path[node]:
        stack.append(node)
        node = path[node]
    stack.append(path[stack[len(stack) - 1]])
    
    fp = open('output.txt', 'a')
    while stack:
        node = stack.pop()
        fp.write(str(node[0]) + "," + str(node[1]) + " ")

def expand(queue, height, width, X, Y, mtrx, stamina, visited, path):
    if isValid(height, width, X-1, Y, mtrx, stamina, X, Y) and not isVisitedBFS(X-1, Y, visited):    # North
        queue.append(tuple((X-1, Y)))
        path[tuple((X-1, Y))] = tuple((X,Y))
    if isValid(height, width, X-1, Y+1, mtrx, stamina, X, Y) and not isVisitedBFS(X-1, Y+1, visited):    # NorthEast
        queue.append(tuple((X-1, Y+1))) 
        path[tuple((X-1, Y+1))] = tuple((X,Y))
    if isValid(height, width, X, Y+1, mtrx, stamina, X, Y) and not isVisitedBFS(X, Y+1, visited):    # East
        queue.append(tuple((X, Y+1)))
        path[tuple((X, Y+1))] = tuple((X,Y))
    if isValid(height, width, X+1, Y+1, mtrx, stamina, X, Y) and not isVisitedBFS(X+1, Y+1, visited):    # SouthEast
        queue.append(tuple((X+1, Y+1)))
        path[tuple((X+1, Y+1))] = tuple((X,Y))
    if isValid(height, width, X+1, Y, mtrx, stamina, X, Y) and not isVisitedBFS(X+1, Y, visited):    # South
        queue.append(tuple((X+1, Y)))
        path[tuple((X+1, Y))] = tuple((X,Y))
    if isValid(height, width, X+1, Y-1, mtrx, stamina, X, Y) and not isVisitedBFS(X+1, Y-1, visited):    # SouthWest
        queue.append(tuple((X+1, Y-1))) 
        path[tuple((X+1, Y-1))] = tuple((X,Y))
    if isValid(height, width, X, Y-1, mtrx, stamina, X, Y) and not isVisitedBFS(X, Y-1, visited):    # West
        queue.append(tuple((X, Y-1)))
        path[tuple((X, Y-1))] = tuple((X,Y))
    if isValid(height, width, X-1, Y-1, mtrx, stamina, X, Y) and not isVisitedBFS(X-1, Y-1, visited):    # NorthWest
        queue.append(tuple((X-1, Y-1)))
        path[tuple((X-1, Y-1))] = tuple((X,Y))

def breadthFirstSearch(start_X, start_Y, stamina, lodges_coordinates, mtrx, height, width):
    for lodge in lodges_coordinates:
        queue = []
        visited = []
        path = {}

        path[tuple((start_X, start_Y))] = None
        queue.append(tuple((start_X, start_Y)))
        visited.append(tuple((str(queue[0][0]), str(queue[0][1]))))

        while True:
            if not queue:
                return False
            node = queue.pop(0)
            if lodge == node:
                printInFile(path, lodge)
                break
            expand(queue, height, width, node[0], node[1], mtrx, stamina, visited, path)

# USC Functions

def uniformCostSearch(start_X, start_Y, stamina, lodges_coordinates, mtrx, height, width):
    pass

if __name__ == "__main__":
    main()