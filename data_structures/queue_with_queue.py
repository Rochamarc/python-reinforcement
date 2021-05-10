# maxsize – Number of items allowed in the queue.
# empty() – Return True if the queue is empty, False otherwise.
# full() – Return True if there are maxsize items in the queue. If the queue was initialized with maxsize=0 (the default), then full() never returns True.
# get() – Remove and return an item from the queue. If queue is empty, wait until an item is available.
# get_nowait() – Return an item if one is immediately available, else raise QueueEmpty.
# put(item) – Put an item into the queue. If the queue is full, wait until a free slot is available before adding the item.
# put_nowait(item) – Put an item into the queue without blocking. If no free slot is immediately available, raise QueueFull.
# qsize() – Return the number of items in the queue.

from queue import Queue 

# initializing a queue
q = Queue(maxsize = 3)

# qsize() give the maxsize of the queue
print(q.qsize()) # 0

# Add element to queue
q.put('a')
q.put('b')
q.put('c') 

# Return boolean for full
print('Full: ', q.full()) # True

# Removing elements from queue
print('Elements dequeued from queue')
print(q.get())
print(q.get())
print(q.get())

# Return boolean for empty
print('Empty: ', q.empty()) # True

q.put(1)
print('Empty: ', q.empty()) # False
print('Full: ', q.full()) # False


