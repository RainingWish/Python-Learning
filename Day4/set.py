#set is also a bunch of key, but cant store value.
#due to key cannot repeat, in this case, key cannot repeat in set


#creat a set
s = set([1,2,3])
print(s)

#delet the repeat
r = set([1,1,2,2,3,3])
print(r)

#add(key): add a key to a set
s.add(4)
print(s)

#remove(key): delet a key in set
s.remove(1)
print(s)

#use set to do math logic
s1 = set([1,2,3])
s2 = set([2,3,4])
a = s1 & s2
print (a)
o = s1 | s2
print(o)

# list can be change, string cannot been change
a = [3, 2, 1]
a.sort()
print(a)

a = 'abc'
print(a.replace('a','A'))
print(a)


