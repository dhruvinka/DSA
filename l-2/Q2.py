# 2. Demonstrate and explain the usage of the following methods - Set.    
# a. difference() {-}  
# b. difference_update() {-=}  
# c. discard()    
# d. intersection() {&}  
# e. intersection_update() 
# f. isdisjoint()    
# g. issubset() 
# {<=}  
# {&=}  
# h.  {<} 
# i. issuperset() {>=}  
# j.  {>}     
# k. symmetric_difference() {^}  
# l. symmetric_difference_update() {^=}  
# m. union() |  
# n. update() {|=}  


a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
# print("Set a:", a)
print("Set b:", b)
# print()

# print("Set difference (a - b):", a.difference(b)) 
# print("Set difference second method (a - b):", a-b)  
# print()

# a.difference_update(b)  # a = a - b
# print("Set after difference_update:", a)
# a -= b
# print("Set after difference_update second method:", a)
# print()

a = {1, 2, 3, 4, 5}
a.discard(3)  
print("Set after discard(3):", a)
print()

#common element
print("Set intersection (a & b):", a.intersection(b))  
print("Set intersection second method (a & b):", a & b)
#inplace intersection
a.intersection_update(b)  # a = a & b
print("Set after intersection_update :", a)
print()

a={1,2,3}
b={4,5,6}
#return True or False
#True when all element is diff form 'a' to 'b' else False
print("isdisjoint",a.isdisjoint(b))
print()


a={1,2,3,4,5}
b={1,2,3}
#subset -> A set A is called a subset of set B if all elements of A are also elements of B.
print("issubset:",a.issubset(b))
print("second method",(a<=b))
print()

#superset (if b's all element is present in a then a is superset of b)
print('superset',a.issuperset(b))
print('superset second way',(a>=b))
print()

#union
print('Union',a.union(b))
print('Union second way',a|b)
print()

#update
a.update(b)  # a = a | b
print("Set after update():", a)
a |= b
print("Set after update second way:", a)
print()

#symmetric difference
a={1,2,3,4,5}
b={4,5,6,7,8}

#return new set with removing common element
print("symmetric_difference:",a.symmetric_difference(b))
print("symmetric_difference second way:",a^b)
print()

#symmetric difference update
#inplace operation
a.symmetric_difference_update(b)  # a = a ^ b
print("Set after symmetric_difference_update():", a)
a ^= b
print("Set after symmetric_difference_update second way:", a)

