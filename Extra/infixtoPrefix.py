from S import Stack

s1=Stack(200)
s1.display()

pre={'+':1,'-':1,'*':2,'/':2,'^':3}
# pre={'+':3,'-':3,'*':2,'/':2,'^':1}
# ex="k + l - m * n + ( o ^ p ) * w / u / v * t + q "
# ex=" 2 * 3 / ( 2 - 1 ) + 5 * ( 4 - 1 )"
ex=" k + l * m - n "
token=ex.split()[::-1]
swapped=[]

for tok in token:
    if tok == '(':
        swapped.append(')')
    elif tok == ')':
        swapped.append('(')
    else:
        swapped.append(tok)

postfix=[]

for token in swapped:
    if token.isalnum():
        postfix.append(token)
    elif token == '(':
        s1.push(token)
    elif token == ')':
        while not s1.isEmpty() and s1.peek() !='(':
            postfix.append(s1.pop())
        s1.pop()
    else:
        while not s1.isEmpty() and s1.peek() !='(' and pre[s1.peek()] > pre[token]:
            postfix.append(s1.pop())
        s1.push(token)

while not s1.isEmpty():
    postfix.append(s1.pop())

prefix=postfix[::-1]
print(prefix)
print(' '.join(prefix))

    

