queue = []

# Add to queue
queue.append('a')
queue.append('b')
queue.append('c')

print("Initial queue")
print(queue) # ['a', 'b', 'c']

# Removind from queue
print("Elements dequeued from queue")
print(queue.pop(0)) # a
print(queue.pop(0)) # b 
print(queue.pop(0)) # c

print('Queue after removing elemnts')
print(queue) 


