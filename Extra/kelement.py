from S import Stack

num = "200200"
k = 1

s1 = Stack(20)

for i in range(k, len(num)):
    s1.push(num[i])

result = ""
while not s1.isEmpty():
        result = s1.pop() + result  
x=result.lstrip('0')
print(x)
