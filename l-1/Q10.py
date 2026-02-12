# 10. Take a deeply nested tuple as input from the user (user single line input) , write code to 
# access the innermost element without hardcoding indices. 

t = eval(input("Enter a list of tuples: "))

# print("You entered:", x)
# p=[]
# t=(1,2,(3,4,(5,6,7)))

def access_innermost(tup):
    for i in tup:
        if type(i) == tuple:
            return access_innermost(i)
    return tup[-1]

print(access_innermost(t))