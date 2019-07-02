# enroll function

def enroll(name, gender, age=6, city='Wuhan'):
	print('name:', name)
	print('gender:', gender)
	print('age:', age)
	print('city:', city)

enroll('Sarah','F')
enroll('Zac','M',7,'Beijing')

#error in use defult

def add_end(L=[]):
	L.append('End')
	return L

print(add_end([1,2,3]))
print(add_end())
print(add_end())

#here will print 2 end
#to aviod this we need to improve the def add_end function
def add_end(L=None):
	if L is None:
		L=[]	
	L.append('End')
	return L

print(add_end())
print(add_end())


