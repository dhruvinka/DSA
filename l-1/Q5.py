# 5. Write a program that safely accesses the nth element of a list. If the index is out of range, 
# print “Invalid index”. 


try:
    x=[10,20,30,40,50,60]
    si=7
    print(x[si])
except IndexError:
    print("Invalid index")
    