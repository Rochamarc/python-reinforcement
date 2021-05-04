class File:
	def __init__(self, filename, method):
		self.file = open(filename, method)

	def __enter__(self):
		print("Enter")
		return self.file 

	def __exit__(self, type, value, traceback):
		print(f'{type}, {value}, {traceback}')
		print("Exit")
		self.file.close()
		if type == Exception:
			return True # say to python that we handle the exception and we prevent the crash

'''
with File("file.txt", 'w') as f:
	print("Midlle")
	f.write("Hello!")
	# raise FileExistsError()
'''

### Second part

from contextlib import contextmanager

@contextmanager
def file(filename, method):
	print('enter')
	file = open(filename, method) # enter
	yield file 
	file.close() # exit
	print('exit')


with file('text.txt', 'w') as f:
	print('middle')
	f.write('hello')