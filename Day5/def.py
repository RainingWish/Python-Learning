import math
# define a function in python

#define an abslute function

def my_abs(x):
	if not isinstance(x,(int,float)):
		raise TypeError('bad operand type')	
	if x>=0:
		return x
	else:
		return -x

print('input a number and thid function will autp change to it abs value:', my_abs(float(input())))


#enpty function

def nop():
	pass

#pass is do nothing but save a spot for this function
#some function missing pass will output error
#for example if...else.. function


#multi return and math patch

#def a move function
def move(x,y,step,angle=0):
	nx = x + step * math.cos(angle)
	ny = y - step * math.sin(angle)
	return nx,ny

x,y = move(100,100,60,math.pi/6)
print(x,y)

#here will return a tuple
r = move(100,100,60,math.pi/6)
print(r)



#practice:
#give a function ax^2+bx+c=0 find two x value

def quadratic(a,b,c):
	x = (-b + math.sqrt(b*b-4*a*c))/(2*a)
	y = (-b - math.sqrt(b*b-4*a*c))/(2*a)
	return x,y

print ('input a function ax^2+bx+c=0')
a = float(input())
b = float(input())
c = float(input())

x,y = quadratic(a,b,c)

print ('two answer are:',x,y)


