
# use partial in functool can more easy define a function

#for example change intiger to base 2 number

def int2(x,base=2):
	return int(x,base)

print(int2('1010101'))

#to use partial to acheive
import functools
int1 = functools.partial(int,base=2)
print(int1('1000000'))

#use partial to sort
sort = functools.partial(sorted,key=abs)
print(sort([1,-3,9,-2,-7]))
