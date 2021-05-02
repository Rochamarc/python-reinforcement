# Decorators
#
#

def func(f):
	def wrapper(*args, **kwargs):
		print("Started")
		rv = f(*args, **kwargs)
		print("Ended")
		return rv 
		
	return wrapper

@func
def func2(x, y):
	print(x)
	return y


@func
def func3():
	print("i am func3")

"""
x = func(func3)
print(x)
x()
"""

# @func subs this -> func3 = func(func3) # same shit in the previous lines
# func2 = func(func2)

func3()
x = func2(10, 6)
print(x)