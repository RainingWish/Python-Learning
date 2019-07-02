# define a powern function

def power(x,n):
	s=1
	while n>0:
		n-=1
		s*=x
	return s

x = int(input())
n = int(input('power of '))
ans = power(x,n)
print('is:', ans)
