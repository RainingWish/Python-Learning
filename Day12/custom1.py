
# custom a class

#__str__

class Student(object):
	def __init__(self,name):
		self.name=name

print(Student('Michael'))# <__main__.Student object at 0x7f23f2be7780> so augly

#to updated it, creat a __str__() function

class Student(object):
	def __init__(self,name):
		self.name=name
	def __str__(self):
		return 'Student object(name: %s)' %self.name
	__repr__=__str__ #variable use __repr__instead of __str__ in this case, let them same

print(Student('Michael'))
s = Student('Michael')
print(s)

#__iter__

class Fib(object):
	def __init__(self):
		self.a, self.b = 0,1

	def __iter__(self): #return the changing value
		return self

	def __next__(self):
		self.a,self.b = self.b, self.a+self.b
		if self.a > 1000:
			raise StopIteration()
		return self.a

for n in Fib():
	print(n)

# Fib can use for loop but cannot use as list ie: get the fifth data Fib()[5]
# In this case, if we want to use as list need __getitem__
#__getitem__

class Fib(object):
	def __getitem__(self,n):
		a,b = 1,1
		for x in range(n):
			a,b =b, a+b
		return a 

f=Fib()
print(f[0])
print(f[1])
print(f[2])
print(f[3])
print(f[10])
print(f[100])

#however, here we cannot use slice function ie: list(range(100))[5:15]
#hear we can update a eazy slice function into __getitem__

class Fib(object):
	def __getitem__(self,n):
		if isinstance(n,int):		
			a,b = 1,1
			for x in range(n):
				a,b =b, a+b
			return a 
		if isinstance(n,slice):
			start = n.start
			stop = n.stop
			if start is None:
				start = 0
			a,b = 1,1
			L=[]
			for x in range(stop):
				if x>= start:
					L.append(a)
				a,b = b,a+b
			return L

f=Fib()
print(f[0:5])
print(f[:10])
print(f[:10:2]) #Here doea not have step









