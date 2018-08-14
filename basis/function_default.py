#-*- coding:utf-8 -*-

def say(message, times=1):
	print message * times

say('Hello')
say('Word', 5)

#매개 변수 목록에서 마지막에 있는 매개 변수들에만 기본 인수값을 지정해 줄 수 있다.