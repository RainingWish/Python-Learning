
#setup and print a list
classmates = ['MIke', 'Bob','Joe']
print ('classmates include: %s with length %d' % (classmates, len(classmates)))

#print one stuff inside the list
print ('''First classmate is %s
Second classmate is %s
Thrid classmate is %s''' %(classmates[0], classmates[1],classmates[2]) )

#print traceback order inside the list
print ('''First classmate is %s
Second classmate is %s
Thrid classmate is %s''' %(classmates[-1], classmates[-2],classmates[-3]) )

#adding string at the end
classmates.append('Adam')
print (classmates)

#adding string at the place u want
classmates.insert(1,'Jack')
print (classmates)

#delet the string at the end of list
a = classmates.pop()
print ('%s is poped out, now classmates are %s' % (a , classmates ))

#delet the string any where u want inside the list
a = classmates.pop(1)
print ('%s is poped out, now classmates are %s' % (a , classmates ))

#change one string in list to other
classmates[1] = 'Sara'
print (classmates)

# different type can both inside a list
L = ['Apple', 123, True]
print (L)

#list can be inside of another list
s = ['a', 'b', ['c', 'd'],'e']
print (s)
print ('lenth s is %d' % len(s))

#practice
#print out Apple, Python and Lisa
L = [ 
	['Apple', 'Google','Microsoft'],
	['Java', 'Python','Ruby','PHP'],
	['Adam','Bart','Lisa']
	]
print(L[0][0],L[1][1],L[2][2])


