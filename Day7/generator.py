#use generator instead of list to save memory
L= [x*x for x in range(10)]
print(L)

g=(x*x for x in range(10))
print(g)

for n in g:
	print(n)

# Fibonacci, the third number is the adding number of first two
def fib(number):
	i,a,b = 0,0,1
	while i<number:
		print(b)
		a , b = b, a+b
		i+=1
	return 'done'

fib(7)
#to change fib function to generater : use yield
def fib(number):
	i,a,b = 0,0,1
	while i<number:
		yield b
		a , b = b, a+b
		i+=1
	return 'done'

f=fib(7)
print(f)

for n in fib(7):
	print(n)

# Pascal's Triangle

def tri():
	L = [1]
	while True:
		yield L
		L=[1]+[L[x]+L[x+1] for x in range(len(L)-1)]+[1]

# test
n = 0
for t in tri():
	print(t)
	n+=1
	if n ==10:
		break








