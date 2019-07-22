#use type

print(type(123))
print(type('str'))
print(type(None))
print(type(abs))

print(type(123)==type(456))
print(type(123)==int)
print(type('abc')==type('123'))
print(type('abc')==str)
print(type('abc')==type(456))

#use type to decide is a finction or not

import types

def fn():
	pass

print(type(fn)==types.FunctionType)
print(type(abs)==types.BuiltinFunctionType)
print(type(lambda x:x)==types.LambdaType)
print(type((x for x in range(10)))==types.GeneratorType)

#use dir()

print(dir('ABC'))
print(len('ABC'))
print('ABC'.__len__())

class MyDog(object):
	def __len__(self):
		return 100

dog = MyDog()
print(len(dog))

print('ABC'.lower())
print('abc'.upper())








