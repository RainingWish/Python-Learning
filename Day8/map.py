

#map a function
def f(x):
	return x*x

r = map(f, [1,2,3,4,5,6,7,8,9]) # r is a Iterator

print(list(r))
print(r)

#use map change intiger inside list trans to string

print(list(map(str,[1,2,3,4,5,6,7,8,9])))

# reduce function
# reduce(f,[x1,x2,x3,x4]) = f(f(f(x1,x2),x3),x4)

#use reduce trans [1,3,5,7,9] to 13579

from functools import reduce

def fnc(x,y):
	return x*10+y

print(reduce(fnc,[1,3,5,7,9]))

#trans string to int

def c2n(s):
	digits = {'0': 0,'1': 1,'2': 2,'3': 3,'4': 4,'5': 5,'6': 6,'7': 7,'8': 8,'9': 9,}
	return digits[s]

print(reduce(fnc,map(c2n,'33679')))		

# practice: change a string first to capital other are small

def norm(name):
	L=name[0].upper()
	for x in name [1:]:
		L=L+x.lower()
	return L

L1 = ['adam','LISA','bOB']
print(list(map(norm,L1)))

#use reduce to calculate all number inside list times togeter

def prod(L):
	
	def time(x,y):
		return x*y
	
	return reduce(time,L)

print(prod([3,5,7,9]))

#change a string to float

def s2f(s):
	
	def c2n(s):
		digits = {'0': 0,'1': 1,'2': 2,'3': 3,'4': 4,'5': 5,'6': 6,'7': 7,'8': 8,'9': 9,}
		return digits[s]
	
	def fn(x,y):
		return x*10+y

	s1,s2 = s.split('.')
	s1 = reduce(fn,map(c2n,s1))
	s2 = reduce(fn,map(c2n,s2))/(pow(10,len(s2)))	
	return s1+s2

print(s2f('123.456'))
print(s2f('321.017'))






