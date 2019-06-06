
#dict = dictionaty also = map in other language

#use dict setup grade to classmates
d = {'Mike':95,'Bob':75,'Lucy':85}
print ('Mike grade is:', d['Mike'])
d['Adam']=99
print ('Adam grade is:', d['Adam'])

#use in to check key created or not
a = 'Thomas' in d
print(a)

#get() also can check character, if the key is not created, will return none
a = d.get('Thomas')
print(a)

#pop(key): delet a key inside the dict
a = d.pop('Bob')
print('Bob been kick out which grade is:'a)
print(d) 

#dict compare with list
#advantage of dict: check and add spead is realy quick. doesn't come slower when the number of key increase
#disadvantage of dict: need lot of memory wast a lot of memory
#dict is use memory to trade speed
