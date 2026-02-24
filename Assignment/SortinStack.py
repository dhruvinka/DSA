from S import *

s1 = Stack(10)
s2 = Stack(10)

# 3, 5, 6, 9, 1, 2, 4, 7, 8

s1.push(3)
s1.push(5)
s1.push(6)
s1.push(9)
s1.push(1)
s1.push(2)
s1.push(4)
s1.push(7)

while not s1.isEmpty():
    x = s1.pop()
    while not s2.isEmpty() and s2.peek() > x:
        s1.push(s2.pop())
    s2.push(x)

s2.display()
