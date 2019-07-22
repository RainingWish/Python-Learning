#easy subclass

class Animal(object):
	def run(self):
		print('Animal is running')

class Dog(Animal):
	pass

class Cat(Animal):
	pass

dog=Dog()
dog.run()

cat=Cat()
cat.run()

#less-easy subclass

class Animal(object):
	def run(self):
		print('Animal is running')

class Dog(Animal):
	def run(self):
		print('Dog is running')
	def eat(self):
		print('Eating meat')

class Cat(Animal):
	def run(self):
		print('Cat is running')

dog=Dog()
dog.run()
dog.eat()

cat=Cat()
cat.run()

#check class type

a=list()
b=Animal()
c=Dog()

print(isinstance(a,list)) #a is a list
print(isinstance(b,Animal)) # b is animal
print(isinstance(c,Dog)) #c is dog
print(isinstance(c,Animal)) #c also an animal
print(isinstance(b,Dog)) # b is animal but not dog





