import sys

arr=[]
# for i in sys.argv:
#     arr.append(int(i))

for i in range(1,len(sys.argv)):
    arr.append(int(sys.argv[i]))


for i in range(len(arr)-1):
    for j in range(0,len(arr)-i-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]

print(arr)

with open("output.txt",'w')as f:
    for i in arr:
        f.write(str(i))