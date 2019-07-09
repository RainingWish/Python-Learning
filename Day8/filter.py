
#keep odd remove even
def odd(n):
	return n%2 ==1

print(list(filter(odd,[1,2,4,5,6,9,15,21,22])))

#remove empty
def not_empty(s):
	return s and s.strip()

print(list(filter(not_empty,['A','','B','C',None,'    ','D',''])))

#Find prime numbers

#first find a odd number start with 3

def odd_n():
	n=1
	while True:
		n+=2
		yield n

#fund cannot divible number 
def not_div(n):
	return lambda x:x%n>0

#creat a function keep return next prime number
def primes():
	yield 2
	i = odd_n()
	while True:
		n = next(i)
		yield n
		i = filter(not_div(n),i)

#creat a none infinity loop make it breakable

for n in primes():
	if n < 100:
		print(n)
	else:
		break


#practice: create a function find palindrome number

def pal(n):
	return str(n)==str(n)[::-1]

print(list(filter(pal,range(1,200))))


