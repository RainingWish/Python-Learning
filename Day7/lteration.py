# for loop in python
for i,value in enumerate(['A','B','C']):
	print(i,value)

#give list find max and min
def find(L):
	if L == []:
		return (None,None)
	else:
		minl=L[0]
		maxl=L[0]
		for i in L:
			if i>maxl:
				maxl=i
			elif i<minl:
				minl=i
		return (minl,maxl)

print(find([]))
print(find([0,-3,-2,1,6,11,-8]))
