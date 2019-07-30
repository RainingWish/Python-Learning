
#__getattr__

#most use in rest API, use getattr to change SDK when API is changed

class Chain(object):
	def __init__(self,path=''):
		self._path = path

	def __getattr__(self,path):
		return Chain('%s/%s' % (self._path,path))
		
	def __str__(self):
		return self._path

	__repr__ = __str__

print(Chain().status.user.timeline.list)

#__call__

class Student(object):
	def __init__(self,name):
		self.name = name

	def __call__(self):
		print('My name is %s' %self.name)

s=Student('Mick')
s()

print(callable(Student('Mick')))
print(callable(max))
print(callable(None))
print(callable([1,2,3]))
