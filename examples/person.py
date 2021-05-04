def check_social_security(cls):
	def wrapper(*args):
		if len(args[-1]) == 11:
			p = cls(*args)
			return p
		return None
	return wrapper


@check_social_security
class Person:
	def __init__(self, name, age, social_security):
		self.__name = name 
		self.age = age 
		self.__social_security = social_security

	@property
	def social_security(self):
		return self.__social_security

	@property 
	def name(self):
		return self.__name 

	def get_info(self):
		return f'Name: {self.__name}\nAge: {self.age}\nSocial social_security: {self.__social_security}'

	def __repr__(self):
		return "<class 'Person'>"

p = Person('Marcos', 24, '16119718715')
print(p) # <class 'Person'>
print(p.name)
print(p.social_security)
print(p.age)

p2 = Person('Malu', 22, '1541451252')
print(p2) # None