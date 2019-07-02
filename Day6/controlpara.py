#define a function that parameter can control

#give a b c d calculate a^2+b^2+c^2+d^2

def calc(numbers):
	sum=0
	for n in numbers:
		sum += n*n
	return sum

print('calculate 1,2,3 squar sum:', calc([1,2,3]))
print('calculate 1,3,5,7 squar sum:', calc([1,3,5,7]))

#change to nun list

def calc(*numbers):
	sum=0
	for n in numbers:
		sum += n*n
	return sum

print('calculate 1,3,5,7 squar sum:', calc(1,3,5,7))
nums = [1,2,3]
print('calculate list nums squar sum:', calc(nums[0],nums[1],nums[2]))
print('calculate list nums squar sum:', calc(*nums))

