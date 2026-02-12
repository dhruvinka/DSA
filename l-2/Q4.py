# 4. Write a program to invert a dictionary. Given a dictionary of {Student: Grade}. Create a 
# new dictionary mapping grades to students so that we can identify students getting a 
# particular grade. 
# Input: {'Stud-A': 'A', 'Stud-B': 'B', 'Stud-C': 'A'} 
# Output: {'A': ['Stud-A', 'Stud-C'], 'B': ['Stud-B']}

x={'Stud-A': 'A', 'Stud-B': 'B', 'Stud-C': 'A'}
z=x.copy()
y={}

for keys,values in z.items():
    if values not in y:
        x={values:[]}
        y.update(x)
for keys,values in y.items():
    x=[]
    for k,v in z.items():
        if keys == v:
            x.append(k)
            y[keys]=x

print(y)    
print(z)    
