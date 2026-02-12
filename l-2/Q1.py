# 1. Demonstrate and explain the usage of the following methods - Dictionary. 
# a. items()  
# b. get()  
# c. pop()  
# d. popitem()  
# e. update()  
# f. fromkeys()  
# g. keys()  
# h. values()  
# i. setdefault() 


x={'a':1,'b':2,'c':3,'d':4,'e':5}

print("Dictionary items():",x.items())
print()
print("Dictionary get():",x.get('b'))  
print()
print("Dictionary pop():",x.pop('c')) 
print("Dictionary after pop():",x)
print()
print("Dictionary popitem():",x.popitem())  # removes lastpair
print("Dictionary after popitem():",x)
print()
y={'f':6,'g':7}
x.update(y)  # updates dictionary x with key-value pairs from y
print("Dictionary after update():",x)
print()
z = dict.fromkeys(['h', 'i'], 0)  # creates a new
print("Dictionary fromkeys():",z)

print("Dictionary keys():",x.keys())  # returns a view of keys in the dictionary
print("Dictionary values():",x.values())  # returns a view of values in the dictionary
print("Dictionary setdefault():",x.setdefault('j', 10))  # sets '
print("Dictionary after setdefault():",x)
