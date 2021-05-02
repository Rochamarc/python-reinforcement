import inspect 
from queue import Queue 

def make_class(x):
	class Dog:
		def __init__(self,name):
			self.name = name 

		def print_value(self):
			print(x)

	return Dog 

"""
cls = make_class(10)
d = cls("Tim") # this is a class
print(d.name) 
d.print_value() # this is acessing the method make_class attr
"""

for i in range(10):
	def show():
		print(i*2)
	# show()	
# show() # doesn't make sense, but it works fine

def func(x):
	if x  == 1:
		def rv():
			print("X is equal to 1")
	else:
		def rv():
			print("X is not 1")

	return rv

new_func = func(2)
# new_func()
print(inspect.getsource(Queue))
 