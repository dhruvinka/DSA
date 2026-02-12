#prefix Evaluation

from S import Stack

s1=Stack(20)
# s1.display()
ex="+ 9 * 2 3"
tokens=ex.split()[::-1]

for token in tokens:
    if token.isdigit():
        s1.push(int(token))
    else:
        right=s1.pop()
        left=s1.pop()
        if token == '+':
            r=right+left
            s1.push(r)   
        elif token == '-':
            s1.push((right-left))
        elif token == '/':
            s1.push((right-left))
        elif token == '*':
            s1.push((right*left))
        else:
            raise ValueError("Enter uncomman oprater",token)
print(s1.pop())