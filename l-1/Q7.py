# User enters: [(1,3), (4,2), (3,1)]
x = eval(input("Enter a list of tuples: "))

print("You entered:", x)
p=[]

for i in range(len(x)):
        if (x[i][0] + x[i][1]) % 2 == 0:
            p.append((x[i][0],x[i][1]))

print(p)
            


