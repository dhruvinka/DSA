
from S import Stack

s1=Stack(200)
s1.display()

pre={'+':1,'-':1,'*':2,'/':2,'^':3}
# ex="( 2 * 5 ) + ( 6 * 3 )"
ex=" k + l - m * n "
tokens=ex.split()
postfix=[]


for token in tokens:
    if token.isalnum():
        postfix.append(token)
    elif token == '(':
        s1.push(token)
    elif token == ')':
        while not s1.isEmpty() and s1.peek() !='(':
            postfix.append(s1.pop())
        s1.pop()
    else:
        while not s1.isEmpty() and s1.peek() != '(' and pre[s1.peek()] >= pre[token]:
            postfix.append(s1.pop())
        s1.push(token)

while not s1.isEmpty():
        postfix.append(s1.pop())
print(' '.join(postfix))