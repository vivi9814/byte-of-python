#-*- coding:utf-8 -*-


shoplist = ['apple', 'mango', 'carrot', 'banana']
name = 'swaroop'

print 'Item 0 is', shoplist[0]
print 'Item 1 is', shoplist[1]
print 'Item 2 is', shoplist[2]
print 'Item 3 is', shoplist[3]
print 'Item -1 is', shoplist[-1]

#shoplist[-1]은 열거형의 마지막 항목
#shoplist[-2]는 열거형의 마지막 항목 바로 뒤의 항목
print 'Item -2 is', shoplist[-2]
print 'Character 0 is', name[0]

#슬라이스연산 시작 위치에 해당하는 항목은 슬라이스에 포함되나 마 지막 위치에 해당하는 항목은 포함되지 않습니다.
print'Item 1 to 3 is', shoplist[1:3]
print 'Item 2 to end is', shoplist[2:]
print 'Item 1 to -1 is', shoplist[1:-1]
print 'Item satart to end is', shoplist[:]

print'Characters 1 to 3 is', name[1:3]
print 'Characters 2 to end is', name[2:]
print 'Characters 1 to -1 is', name[1:-1]
print 'Characters satart to end is', name[0]
