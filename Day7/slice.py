# slice is use to get some specific things in a list or tuple

L = ['Mick','Sam','Tracy','Bob','Jack']

print (L[:3])
print(L[1:3])
print(L[-2:])
print(L[-2:-1])

l = list(range(100))
#print(l)
print (l[:10])
print(l[-10:])
print(l[:10:2]) # 0 to 10 skip 1 each
print(l[::5]) # every 5 pick 1
#print(l[:]) #print a same list

# tuple
print((0,1,2,3,4,5)[:3]) #output also tuple

#remove all empty from a string

def trim(s):
	i=len(s)
	while i>1:
		if s[0]==' ':
			s = s[1:]
		elif s[-1] == ' ':
			s = s[:-1]
		i-=1
	return s

A = '  hello '
print(A)
print(trim(A))

B = '       EMMMMMM     '
print(B)
print(trim(B))







