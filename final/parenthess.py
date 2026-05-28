from Stack import *
dict1 = {')': '(', '}': '{', ']': '['}

def is_bal(str1):
    s = Stack(10)
    for i in str1:
        if i in dict1.values():
            s.push(i)
        elif i in dict1.keys():
            if s.is_Empty(): 
                return False    
            top = s.pop()
            if top != dict1[i]:
                return False
    return s.is_Empty()
    

print(is_bal("({{}})}"))

    
