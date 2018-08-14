#-*- coding:utf-8 -*-


print 'Simple Assignment'
shoplist = ['apple', 'mango', 'carrot', 'banana']
#my list is another name that pointing to the same object

print 'before I purchase', shoplist
mylist = shoplist

del shoplist[0]

print 'shoplist is', shoplist
print 'mylist is', mylist
#shoplist0만 지웠는데 mylist도 없어짐

print 'Copy by making a full slice'

mylist = shoplist[:]

print 'mylist', mylist
print 'shoplist', shoplist

del mylist[0]

print 'shoplist is', shoplist
print 'mylist is', mylist

#복사본을 생성하고 싶을 때에는, 슬라이스 연산자를 이용하여 복사본을 생성해야함
#단순히 한 변수를 다른 변수에 할당하게 되면 두 변수는 같은 객체를 '참조'하게 되며
#실제 복사본이 생성되지 않음.

