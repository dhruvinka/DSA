# 4. Write a program to flatten list-of-lists to a single list (do not use chain/itertools). Read  
# input as a single list from the user. Produce a flattened list. 
# Input: [2, [10 ,20],  [3, 30, 40, 50]]  
# Output: [2, 10, 20, 3, 30, 40, 50] 


def flat(x):
    li=[]
    for i in x:
        if type(i)==list:
                li.extend(flat(i))
        else:
            li.append(i)
    return  li

x=input()
x=eval(x)
print(flat(x))

