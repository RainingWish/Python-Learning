class Student(object):
	pass

bart = Student()

print(bart) # print bart memory place

print(Student) # print student is a class belong to main

bart.name='Bart Simpson' # give bart a name attribute

print(bart.name)

#use __init__ give some attribute to student

class Student(object):
	def __init__(self,name,score): # __init__ first variable must be self
		self.name = name
		self.score = score

bart = Student('Bart Simpson',59)
print(bart.name)
print(bart.score)

# Data encapsulation

#use normal function
def print_score(std):
	print('%s: %s' % (std.name,std.score))

print_score(bart)

#use data encapsulation
class Student(object):

	def __init__(self,name,score): # __init__ first variable must be self
		self.name = name
		self.score = score

	def print_score(self):
		print('%s: %s' % (self.name,self.score))

	def get_grade(self):
		if self.score >= 80:
			return 'A'
		elif self.score >=60:
			return 'B'
		else:
			return 'C'

lisa = Student('Lisa',99)
bob = Student('Bob',70)
bart = Student('Bart Simpson',59)

print(lisa.print_score(),lisa.get_grade()) #here input both name and score to get grade so have a none

print(lisa.name,lisa.get_grade())
print(bob.name,bob.get_grade())
print(bart.name,bart.get_grade())

#change variable to private

class Student(object):
	
	def __init__(self,name,score): # __init__ first variable must be self
		self.__name = name
		self.__score = score

	def get_name(self):
		return self.__name #__variable is private
	
	def get_score(self):
		return self.__score
	
	def set_score(self,score):
		if 0<= score <=100:			
			self.__score = score
		else:
			raise ValueError('error score input')

bart = Student('Bart Simpson',59)
print(bart.get_name())

#practice change gender variable to private

class Student(object):
	
	def __init__(self,name,score,gender): # __init__ first variable must be self
		self.name = name
		self.__score = score
		self.__gender = gender

	def get_gender(self):
		return self.__gender
	
	def set_gender(self,gender):
		if gender == 'female' or gender == 'male':
			self.__gender = gender
		else:
			raise ValueError('error gender input')

bart = Student('Bart Simpson',59,'male')

print (bart.get_gender())

bart.set_gender('female')

print (bart.get_gender())

