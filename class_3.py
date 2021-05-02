# Metaclasses 
#
#

"""
class Test:
	pass

def func():
	pass 


print(type(Test)) # class 'type'
"""


### other way to make a class
class Foo:
	def show(self):
		print("Hi")


def add_attribute(self):
	self.z = 9

# type(ClassName=String, Inherit=(inherit), Attributes={"x": 5})
Test = type('Test', (Foo,), {"x":5, "add_attribute": add_attribute})
t = Test()
t.add_attribute()
t.show()
print(t.z)
# print(t.x)

