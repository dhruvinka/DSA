# 4. Write a program that checks whether a string of parentheses is balanced or not using 
# stack. [Use Class Implementation] 
# Expected Output: 
# Input an expression in parentheses: {[]) 
# The expression is not balanced. ----------------------------------------- 
# Input an expression in parentheses: ((())) 
# The expression is balanced. ----------------------------------------- 
# Input an expression in parentheses: ()) 
# The expression is not balanced. ----------------------------------------- 
# Input an text of parentheses: ([]){}[[(){}]{}] 
# The expression is balanced. ----------------------------------------- 
# Input an expression in parentheses: [(])) 
# The expression is not balanced. 


from Stack import *
from Q1 import *

# set_size(10)
# init()

# se={')': '(', '}': '{', ']': '['}
# def is_balanced(exp):
#     l=list(exp)
#     f=0
#     for i in l:
#         if i not in se.values():
#             push(i)
#         elif is_empty():  
#                 return False
#             top =pop()
#             if top != se[i]:
#                 return False
#     if f!=-1:
#         return True

# str1="({}})"
# print(display())

# x=is_balanced(str1)
# print(display())
# print(x)

from Q1 import *

# create stack
set_size(50)
init()
s = Stack(50)

pairs = {')': '(', '}': '{', ']': '['}

def is_balanced(exp):
    for ch in exp:
        if ch in pairs.values():
            push(ch)
        elif ch in pairs:
            if is_empty():
                return False
            top = pop()
            if top != pairs[ch]:
                return False
    return is_empty()  

str1="{()}"
print(is_balanced(str1))
