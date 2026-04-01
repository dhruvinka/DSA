from S import *

s1 = Stack(10)
s2 = Stack(10)

n=eval(input('enter the number in [10 , 20 ...] :'))
if len(n) > 0:
    for i in range(len(n)):
        s1.push(n[i])

#pop until stack s1 is not empty
while not s1.isEmpty():
    x = s1.pop()
    # x grater then s2 of peek then and into s1 else into s2
    while not s2.isEmpty() and s2.peek() > x:
        s1.push(s2.pop())
    s2.push(x)

s2.display()
