def introduce(func):
	def wrapper(*args):
		print("Hi, i am a function!")
		rv = func(*args)
		return rv
	return wrapper 

@introduce
def say_hi():
	print('Hi!')

@introduce
def greetings(name):
	return f'Hello {name}'

s = say_hi()
print(s) # None
g = greetings('Marcos')
print(g) # Hello Marcos
