print ('chinese string')

# ord is use to get a character's number
a = ord('A')
print(a)

# chr is use to change character's number back to character
a = chr(25991)
print(a)

# len() can find there are how many characters inside a string
a = len('ABC')
print ('string ABC have a lenth of', a)

# %d = save a spot for intiger
print ('Hi mike, you have $%d' % 10000)
print ('%2d-%02d' %(3,1))

# %f = save a spot for x digit after dot
print ('5 digit of PI is %.4f' %3.1415926)

# %s = print string and can using in most case
print ('Hi, %s, you have $%s' %('Sam', 11111))

# %% = print % in print function
print ('growth rate: %d %%' %6)

# Joe last year grade is 72, this year grade is 85. Find increasing rate with 1 digit after dot
r = (85/72-1) * 100
print ('Joe grade increasing rate this year is: %.1f%%' % r )



