# define a function could add key parameter

def person(name, age, **kw):
	print('name:',name, 'age:', age,'other:', kw)

person('Mick',28)
person('Bob',35,city = 'Beijing')
person('Calven', 50, gender = 'M', job = 'Engineer')

extra = {'City':'Beijing','job':'Engineer'}
person('Jack',23,**extra)

#practice
def product(*numbers):
	if len(numbers) == 0:
		#raise TypeError('Empty')	
		return 0
	sum=1
	for n in numbers:
		sum*=n
	return sum

print('product(5,6,7)=', product(5,6,7))
print('product(5,6)=', product(5,6))
print('product(0)=', product(0))
print('product()=', product())
print('product(5,6,7,9)=', product(5,6,7,9))

