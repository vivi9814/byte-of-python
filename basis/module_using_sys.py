import sys
import os

print('The command line arguments are: ')
for i in sys.argv:
	print i

print '\n\nThe PYTHON ATM is', sys.path, '\n'

print os.getcwd() 

print sys.argv