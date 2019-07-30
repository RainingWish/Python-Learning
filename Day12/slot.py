# first way give properties to variable

class Student(object):
	pass

s=Student()
s.name='Michael'
print(s.name)

# Second way

def set_age(self,age):
	self.age=age

from types import MethodType
s.set_age = MethodType(set_age, s)
s.set_age(25)
print (s.age)

#Third use slot
class Student(object):
	__slots__ = ('name','age')

s=Student()
s.name = 'Michael'
s.age = 25
print(s.name)
print(s.age)
#s.score = 99
#print(s.score) #here we not define score in slots so there will be an error
#also child class cannot receive slots message to follow it rules


