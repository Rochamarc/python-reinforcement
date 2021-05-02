class Meta(type):
	def __new__(self, class_name, bases, attrs):
		""" this method is called before __init__ """

		a = {}
		for name, value in attrs.items():
			if name.startswith("__"):
				a[name] = value
			else:
				a[name.upper()] = value	

		return type(class_name, bases, a)

class Dog(metaclass=Meta):
	x = 5
	y = 8

	def hello(self):
		print("Hi")

d = Dog()
print(d.HELLO())