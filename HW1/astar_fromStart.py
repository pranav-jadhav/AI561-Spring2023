from queue import PriorityQueue

def ifExists(pQueue, X, Y):
    if pQueue.empty():
        return False

    for ele in pQueue.queue:
        if ele[1] == X and ele[2] == Y:
            return ele
    return False

def printInFileAS(visited, key):
    pass

def heuristic(curr_X, curr_Y, lodge_X, lodge_Y):
    return (pow(curr_X - lodge_X, 2) + pow(curr_Y - lodge_Y, 2))

def calcPathCost(Enext, Ecurr, M, HMC):
    if Enext - Ecurr <= M:
        return HMC
    else:
        return max(0, Enext - Ecurr - M) + HMC

def expandAS(children, curr_X, curr_Y, mtrx, height, width, stamina, visited, parent_cost, lodge_X, lodge_Y):

    pass

def aStarSearch(start_Y, start_X, stamina, lodge_coordinates, mtrx, height, width):
    for lodge in lodge_coordinates:
        flag = 1
        open_queue = PriorityQueue()
        close = PriorityQueue()
        visited = {}

        open_queue.put((0 + heuristic(start_X, start_Y, lodge[1], lodge[0]), 0, (start_X, start_Y)))
    
        while not open_queue.empty():
            currNode = open_queue.get()
                
            children = PriorityQueue()
            expandAS(children, currNode[2][0], currNode[2][1], mtrx, height, width, stamina, visited, currNode[1], lodge[1], lodge[0])

            while not children.empty():
                child = children.get()

                if child[2][0] == lodge[1] and child[2][1] == lodge[0]:
                    printInFileAS(visited, currNode[2])
                    flag = 0
                    print("YAAAAAYYYYYYYYYYY")
                    break

                checkOpen = ifExists(open_queue, child[2][0], child[2][1])
                checkClosed = ifExists(close, child[2][0], child[2][1])

                if checkOpen != False:
                    pass
                    

                


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

    fp = open('output.txt', 'w')

    if algorithm == "A*":
        aStarSearch(start_X, start_Y, stamina, lodges_coordinates, mtrx, height, width)

if __name__ == "__main__":
    main()