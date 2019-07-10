
#normal case  return a sum

def calc_sum(*args):
	ax=0
	for n in args:
		ax+=n
	return ax

#However, if we don't need sum imidiatly and pending on later code

def lazy_sum(*args):
	def sum():
		ax=0
		for n in args:
			ax+=n
		return ax
	return sum

#when we use lazy_sum() return is not the sum value is the sum function

f = lazy_sum(1,3,5,7,9)

print(f) #print where we store the function

print(f()) #after we call the function, it return number

#every function is indipendent even the number inside is same
f1 = lazy_sum(1,3,5,7,9)
f2 = lazy_sum(1,3,5,7,9)
print(f1==f2)

# closur

def count():
	fs = []
	for i in range(1,4):
		def f():
			return i*i
		fs.append(f)
	return fs

f1,f2,f3 = count()

print(f1(),f2(),f3()) # it print  9 9 9 istead of 1 4 9 this call closur

# change to none closur

def count():
	def f(j):
		def g():
			return j*j
		return g
	fs = []
	for i in range (1,4):
		fs.append(f(i)) #f(i) run imidiantly so i value trans to f()
	return fs

f1,f2,f3 = count()

print(f1(),f2(),f3())

#use closur return a increase number function

#use ninlocal
def createCounter():
	count = 0	
	def counter():
		nonlocal count
		count+=1		
		return count
	return counter

counterA = createCounter()
print(counterA(),counterA(),counterA(),counterA())
counterB = createCounter()
L=[counterB(),counterB(),counterB(),counterB()]
print(L)




#use list
def createCounter():
	count = [0]	
	def counter():
		count[0]+=1		
		return count[0]
	return counter

counterA = createCounter()
print(counterA(),counterA(),counterA(),counterA())
counterB = createCounter()
L=[counterB(),counterB(),counterB(),counterB()]
print(L)






