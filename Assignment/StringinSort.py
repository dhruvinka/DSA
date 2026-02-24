# . Write a program to print the characters of the string in sorted order using stack.  
# Input: str = "hello3569world12478" 
# Output: 123456789dehllloorw 

from S import *

s1 = Stack(50)
s2 = Stack(50)
s3=Stack(40)

s1.push('hello3569world12478')

for i in s1.s[0]:
    if  i.isalnum():
         if i.isdigit():
            s3.push(int(i))
         else:
             s2.push(i)

s2.display()
s3.display()

tmp=Stack(40)

while not s3.isEmpty():
    x = s3.pop()
    while (not tmp.isEmpty()) and (tmp.peek()) > x:
        s3.push(tmp.pop())
    tmp.push(x)

tmp2=Stack(40)
while not s2.isEmpty():
    x = s2.pop()
    while (not tmp2.isEmpty()) and (tmp2.peek()) > x:
        s2.push(tmp2.pop())
    tmp2.push(x)
res=""
while not tmp.isEmpty():
    res+=str(tmp.pop())

res = res[::-1]

res2=""
while not tmp2.isEmpty():
    res2+=str(tmp2.pop())
res2=res2[::-1]
print(res+res2)