x=[10,20,30]
y=(60,70,80,x)
print(y)
print(id(y[3]))
x.append(40)
print(y)
print(id(y[3]))
