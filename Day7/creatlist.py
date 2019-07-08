#create normal list

L= list(range(1,11))

#creat [1x1,2x2,3x3,4x4,...,10x10] list
#use loop
L=[]
for x in range(1,11):
	L.append(x*x)
#print(L)

#simple way
L=[x*x for x in range(1,11)]
print(L)

#add if after for to find even numbers squart
l=[x*x for x in range(1,11) if x%2==0]
print(l)

#two for loop in a list
L=[m+n for m in'ABC' for n in 'XYZ']
print(L)

#print current folder
import os
print([d for d in os.listdir('.')])

# lower case
L=['Hello','World','IBM','Apple']
print([s.lower()for s in L])

# if list have intiger lower function eill output error
L=['Hello','World',18,'IBM','Apple',None]
print([s.lower()for s in L if isinstance(s,str)==True])





