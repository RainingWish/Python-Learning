# instance properties and class properties

class Student(object):
	name = 'Student'

s=Student()
print(s.name)
print(Student.name)
s.name='Michael'
print(s.name)
print(Student.name)
del s.name
print(s.name)

# add a count system for Student
# every time call __init__ function, count+=1

class Student(object):
	count = 0
	
	def __init__(self,name):
		self.name = name
		Student.count+=1

print(Student.count)
bart = Student('Bart')
print(Student.count)
lisa = Student('Bart')
print('Student:',Student.count)

