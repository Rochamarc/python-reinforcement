from random import randint 
class Person:
	def __init__(self, name):
		self.__name = name

	@property	
	def name(self):
		""" Use the Object.name method as a property but its still a method """ 
		return self.__name


p = Person('Marcos')
print(p.name)
''' p.name = 'Lucas' # Return an error ... unlesss '''

class Person2:
	people = 0

	def __init__(self, name):
		self.__name = name
		Person2.add_social_security()

	@property	
	def name(self):
		""" Use the Object.name method as a property but its still a method """ 
		return self.__name

	@name.setter
	def name(self, n_name):
		""" Change the __name using a method as a property """
		self.__name = n_name 

	@classmethod
	def add_social_security(cls):
		cls.people += 1

a = Person2('Smeagol')
print(a.name) # Smeagol
a.name = 'Gollum' 
print(a.name) # Gollum
print(a.people) # 1

a2 = Person2('Malu')
print(a2.name) # Malu
print(a2.people) # 2 even if i ask for a.identity again


