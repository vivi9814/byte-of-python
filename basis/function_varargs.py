#-*- coding:utf-8 -*-

#함수에 임의의 개수의 매개 변수를 지정

def total(initial=5, *numbers, **keywords):
	count = initial
	for number in numbers:
		count += number
	for key in keywords:
		count += keywords[key]
	return count

print total(10, 1, 2, 3, vegetables=50, fruits=100)


#별 기호를 이용하여 임의의 개수의 인수를 표현 ex. *numbers, **keywords

