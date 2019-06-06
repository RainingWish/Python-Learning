#input a birth year decide u are a adult, teenager or a kid

#let user input theire birth year
birth = input('Your birth year is:')
#input function will save the number in string
#in this case, we need change the string to intiger for comparing
birth = int(birth)
#calculate your age
age = 2019-birth
print ('your age is', age)

#start comparing
#elif = else if
# warning: dont forget ':'
if age >= 18:
	print('adult')
elif age >= 6:
	print('teenager')
else:
	print('kid')


#practice, given hight and weight find BMI and give the health statement
height = input('Your height in meter:')
weight = input('Your weight in kg:')

height = float(height)
weight = float(weight)
BMI = weight/(height*height)
print ('your BMI is', BMI)

if BMI >= 32:
	print('really fat')
elif BMI >= 28:
	print('fat')
elif BMI >= 25:
	print('over weight')
elif BMI >= 18.5:
	print('normal')
else:
	print('too light')
