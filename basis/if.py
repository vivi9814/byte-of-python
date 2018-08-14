#if statement

number = 23
guess = int(raw_input('Enger an integer :'))

if guess == number :
	# New block starts here
	print 'Congratulations, you guessed it.'
	print '(But you do not win any prizes!)'
	# New block ends here
elif guess < number:
	# Another block
	print 'No, it is a little higher than that'
elif guess > number:
	print 'No, it is a little lower than that'
else:
	print 'Done'
