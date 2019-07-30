# define a bunch of sub, sub-sub class for a class

#main
class Animal(object):
	pass

#sub class
class Mammal(Animal):
	pass

class Bird(Animal):
	pass

#sub-sub class

class Dog(Mammal):
	pass

class Bat(Mammal):
	pass

class Parrot(Bird):
	pass

class Ostrich(Bird):
	pass

#now add runnable and flyable function

class Runnable(object):
	def run(self):
		print('Running...')

class Flyable(object):
	def fly(self):
		print('Flying...')

#now we want dog both inheritance Mammal and Runnable
class Dog(Mammal,Rinnable):
	pass

#now we want bat both inheritance Mammal and Flyable
class Bat(Mammal,Flyable):
	pass

#Mixin
#to better see sub class inheritance relasionship
#we better change Runnable to RunnableMixIn and Flyable to FlyableMinIn
# to seperate them from main class

class MyTCPServer(TCPServer, ForkingMixIn):
	pass


class MyUDPServer(UDPServer, ThreadingMixIn):
	pass

#JAVA cannot use MixIn!!!!!



