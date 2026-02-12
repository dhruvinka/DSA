# x=[(1,3),(4,2),(3,1)]
# sorted_x=sorted(x,key=lambda x:x[1])
# print(sorted_x)

x = eval(input("Enter a list of tuples: "))

print("You entered:", x)
for i in range(len(x)):
    for j in range(len(x)-1):
        if x[j][1] > x[j+1][1]:
            temp=x[j]
            x[j]=x[j+1]
            x[j+1]=temp

print(x)


