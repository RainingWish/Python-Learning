# __xxx__ is special variable
# _xxx is private variable

def _private_1(name):
	return 'Hello,%s' %name

def _private_2(name):
	return 'Hi,%s' %name

def greeting(name):
	if len(name)>3:
		return _private_1(name)
	else:
		return _private_2(name)

print(greeting('Ado'))
print(greeting('Luwan'))
