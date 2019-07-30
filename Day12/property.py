# to protect the score 
#first way define a set score function
class Student(object):

	def get_score(self):
		return self._score
	
	def set_score(self,value):
		if not isinstance(value,int):
			raise ValueError('Score need to be integer')

		if value <0 or value>100:
			raise ValueError('incorrect value')

		self._score = value

s = Student()
s.set_score(60)
print(s.get_score())
#s.set_score(9999) #test error

#Second way use decorator
class Student(object):

	@property
	def score(self):
		return self._score
	
	@score.setter
	def score(self,value):
		if not isinstance(value,int):
			raise ValueError('Score need to be integer')

		if value <0 or value>100:
			raise ValueError('incorrect value')

		self._score = value

s = Student()
s.score = 60
print(s.score)
#s.score = 9999

#read and write property and only read property
#@property + @function.setter = read and write property
#@property + call other function value =  only read property
class Student(object):

	@property
	def birth(self):
		return self._birth

	@birth.setter
	def birth(self,value):
		self._birth = value
	
	@property
	def age(self):
		return 2019-self._birth
#birth is R&W property
#agef is only read property

s = Student()
s.birth = 1995
print(s.birth)
print(s.age)

# practice
#add width and height property to screen class  and add a only read property resolution

 
class Screen(object):

	@property
	def width(self):
		return self._width

	@width.setter
	def width(self,value):
		self._width = value

	@property
	def height(self):
		return self._height

	@height.setter
	def height(self,value):
		self._height = value
	
	@property
	def resolution(self):
		return self._height*self._width

s =  Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)










