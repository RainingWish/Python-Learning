
# for ... in loop: getting out every character inside a list/tuple
#print all name in a name list
#warning: for... in ... : dont forget the':'
names = ['mike','Bob','Joe']
for name in names:
	print(name)

#range(int): given all number greater than 0 and lower than int
#create a 0 to 5 list
L=list(range(6))
print(L)
# sum 0 to 100
s = 0
for x in range(101):
	s = s+x
print (s)

# while loop: if the condition after while is true, keep the loop
# if the condition after while is false, end the loop
#warning: while ... : dont forget the':'
# sum all odd number below 100
s = 0
n=99
while n>0:
	s=s+n
	n-=2
print(s)

#break can end the loop anywhere
#print 0 to 5 
n=1
while n<=10:
	if n>5:
		break
	print(n)
	n+=1
print('END')

#continue can skip the function after him and go to next loop
#print all odd number inside 10
n=0
while n<10:
	n+=1
	if n%2 == 0:
		continue
	print(n)
print('END')
