from S import Stack

s1=Stack(20)
s1.display()
ex=" 2 3 - 4 + 5 6 7 * + * "
tokens=ex.split()

for token in tokens:
    if token.isdigit():
        s1.push(int(token))
    else:
        right=s1.pop()
        left=s1.pop()
        if token == '+':
            r=left+right
            s1.push(r)   
        elif token == '-':
            s1.push((left-right))
        elif token == '/':
            s1.push((left/right))
        elif token == '*':
            s1.push((left*right))
        else:
            raise ValueError("Enter uncomman oprater",token)
print(s1.pop())
        

