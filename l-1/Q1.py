# 1. Write a program to count frequency in list preserving first occurrence order (no dictionary). 
# Read N arr. For each distinct element print value and its frequency. 
# Sample: [2,3,2,5,3,2] → 2->3; 3->2; 5->1 
n=input()

x=n.split()

y=[]
for i in x:
    if i not in y:
        y.append(x.count(i))
for i in y:
    print(i,"->",x.count(i))
