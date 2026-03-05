# 9. Implement a linked list to create and manage a set of elements. Set of elements 
# contains integer values i.e. S = {4,5,6}. No Elements are repeated in a Set. Also 
# implement a method which shows all possible subsets of the created set by user 
# i.e. {{4}, {5}, {6}, {4,5}, {4,6}, {5,6}, {4,5,6}, {Ø}}.

s={4,5,6}

def subsets(s):
    l1=list(s)
    n=len(l1)
    result=[]
    for i in range(2**n):
        subset=[]
        for j in range(n):
            if i & (1 << j):
                subset.append(l1[j])
        result.append(subset)
    return result

print(subsets(s))


