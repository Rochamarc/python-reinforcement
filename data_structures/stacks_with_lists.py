# demonstrate stack implementation using list
#
#


stack = [] 

# append() func to push
# element in the stack

stack.append('a')
stack.append('b')
stack.append('c')

print("Initial stack")
print(stack) # ['a', 'b', 'c']


# pop() funct to pop
# element from stack in FILO 
# order

print('Elements poped from stack:')
print(stack.pop()) # 'c'
print(stack.pop()) # 'b'
print(stack.pop()) # 'a'

print('Stack after elements are poped: ')
print(stack) # []

# print(stack.pop()) -- index error


