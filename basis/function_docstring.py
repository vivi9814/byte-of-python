def print_max(x, y):
	'''Prints the maximum of two numbers.

	The two values must be integers.'''

	x = int(x)
	y = int(y)

	if x>y:
		print x, 'is maximum'
	else:
		print y, 'is maximum'

print_max(3, 5)
print print_max.__doc__

#DocString은 일반적으로 첫째줄의 첫문자는 대문자로, 마지막 문자는 마침표로 끝나도록 작성합니다.
#그리고 두번째 줄은 비워 두고, 세번째 줄부터는 이것이 어떤 기능을 하는지에 대해 상세하게 작성합니다.

