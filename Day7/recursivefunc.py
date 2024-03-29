
# calculate n! = 1x2x3x...xn
# use fact(n)

def fact(n):
	if n==1:
		return 1
	return n * fact(n-1)

print(fact(5))

# better function

def fact(n):
	return fact_iter(n,1)

def fact_iter(num, product):
	if num == 1:
		return product
	return fact_iter(num - 1, num* product)

# Hanoi Tower

def move (n,a,b,c):
	if n == 1:
		print(a,'-->',c)
	else:
		move(n-1,a,c,b)
		move(1,a,b,c)
		move(n-1,b,a,c)

move(2,'A','B','C')
print('new')
move(3,'A','B','C')

