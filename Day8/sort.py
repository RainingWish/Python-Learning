
# sort a list

print(sorted([36,5,-12,9,-21]))

#sort a list with abs value

print(sorted([36,5,-12,9,-21],key=abs))

#sort string will compare them ASCII number
print(sorted(['bob','about','Zoo','Mike']))

#sort string with lower case
print(sorted(['bob','about','Zoo','Mike'], key=str.lower))

#sort string with lower case then reverse
print(sorted(['bob','about','Zoo','Mike'], key=str.lower, reverse=True))


#practice
L =[('Bob',75),('Adam',92),('Nisha',66),('ROTK',88)]

def by_name(t):
	return t[0]

def by_grade(t):
	return -t[1]

print(sorted(L, key = by_name))
print(sorted(L, key = by_grade))
