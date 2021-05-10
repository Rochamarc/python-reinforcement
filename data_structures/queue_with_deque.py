from collections import deque 

# initializing a queue
q = deque()

# Add elements to queue
q.append('a')
q.append('b')
q.append('c')

print('Initial queue')
print(q) # deque(['a', 'b', 'c'])

# Removing elements from a queue
print('Elements dequeue from the queue')
print(q.popleft()) # a
print(q.popleft()) # b
print(q.popleft()) # c

print('Queue after removing elements')
print(q) #deque([])
