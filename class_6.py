# Context manager
#
#

''' This is wrong way '''
file = open('file.txt', 'w')
file.write('hello') # an error here, would leave the file open
file.close()


file = open('file.txt','r')

''' This is righ way '''
try:
	file.write('hello')
finally:
	file.close() 

''' this is the better way '''
with open('file.txt', 'r') as file:
	''' do the same as the code below, but in python way '''
	file.write('hello')

