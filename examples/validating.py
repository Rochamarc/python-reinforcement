# One way to use decorators to validates something
#
#

class Person:
	def __init__(self, name, age):
		self.name = name 
		self.age = age

	def __repr__(self):
		return f'Person({self.name})'

def validates_name(funct):
	""" This will validates the length and the age values and
		return a person object if the validation is True
	"""
	def wrapper(*args):
		if len(args[0]) >= 2:
			if args[-1] > 1:
				mk = funct(*args)
				return mk 
		return None
	return wrapper

@validates_name
def make_person(name, age):
	p = Person(name, age) 
	return p 

@validates_name
def greetings(name, age):
	return f"Hello, my name is {name} and i'm {age} years old!"

m = make_person('Marcos', 24)
print(m) # Person(Marcos)
m2 = make_person('Bo', 1)
print(m2) # None
m3 = make_person('Bo', 2)
print(m3) # Person(Bo)


### grretings method
g = greetings('Marcos', 24)
print(g)
g2 = greetings('Malu', 0)
print(g2)
