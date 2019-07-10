
# get a function name use __name__

def now():
	print('2019-7-10')

f = now
print(f())
print(now.__name__)
print(f.__name__)

#create a decorator can use in any function to print the time for it work
import functools
import time

def metric(fn):
	@functools.wraps(fn)
	def wrapper(*args,**kw):
		#start time
		start = time.time()
		result = fn (*args,**kw)
		end = time.time()
		print('%s executed in %s ms' % (fn.__name__, int(round((end-start)*1000))))
		return result
	return wrapper

@metric
def fast(x,y):
	time.sleep(0.0012)
	return x+y;

@metric
def slow(x,y,z):
	time.sleep(0.1234)
	return x*y*z;

f = fast(11,22)
s = slow(11,22,33)
print (f)
print (s)






