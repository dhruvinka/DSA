# 6. Write a program that takes a list of integers and a target and prints all pairs (as tuples) 
# whose sum equals target. Avoid duplicates in your result. 

x=input()
x=x.split()
li=[int(num) for num in x]
target=5
seen=[]
fi=[]
# for i in li:
#     for j in li:
#         if i+j==target and (j,i) not in seen and i!=j:
#             seen.append((i,j))
# for i in seen:
#     for j in seen:
#         if i not in fi and (j,i) not in fi:
#           fi.append(i)

 
for i in li:
    for  j in li:
        if i+j == target:
            seen.append((i,j))

for i in seen:
    if (i[1],i[0]) not in fi:
        fi.append(i)
    
print(seen)
print(fi)