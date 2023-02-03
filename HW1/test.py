from queue import PriorityQueue

q = PriorityQueue()

q.put(10)
q.put(50)
q.put(30)
q.put(25)

while not q.empty():
    print(q.get())

q.put(10)
q.put(50)
q.put(30)
q.put(25)

q.get(30)
print("--------------------------")
while not q.empty():
    print(q.get())