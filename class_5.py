# Generator
#
#

"""
x = [ i**2 for i in range(10000000000000) ]

for el in x:
	print(el)
"""

class Gen:
	def __init__(self, n):
		self.n = n
		self.last = 0

	def __next__(self):
		return self.next()

	def next(self):
		if self.last == self.n:
			raise StopIteration()

		rv = self.last ** 2
		self.last += 1
		return rv


# pythonist way to write this 
def gen(n):
	for i in range(n):
		# pauses the function until hit it again
		yield i ** 2

g = gen(10000000000)

print(next(g))
print(next(g))
print(next(g))
print(next(g))
'''
for i in g:
	print(i)
'''


"""
g = Gen(100)

while True:
	try:
		print(next(g))
	except StopIteration:
		break
"""


