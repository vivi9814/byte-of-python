def say_hello():
	print 'hello world'

say_hello()
say_hello()


a = int(raw_input('how many times do you want to repeat?'))

def say_bye(a):
	for i in range (1, a+1):
		print 'bye world'

say_bye(a)