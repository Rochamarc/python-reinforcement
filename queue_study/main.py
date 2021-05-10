from queue import Queue 
from random import randint 

'''
q = Queue(10)

for i in range(10):
	q.put(randint(1,10))

print(q.queue) # get the full queue
'''


# ultrapassar o maximo
q = Queue(10)

for i in range(10):
	q.put(i)

q.get()
q.get()

print(q.queue)