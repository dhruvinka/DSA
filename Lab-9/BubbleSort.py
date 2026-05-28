# arr=[50,60,10,203,30,50]

# with open('input.txt','r') as f:
#     arr=list(map(int,f.read().split(",")))

arr=[37,54,21,85,68,12,9,57,3]
for i in range(len(arr)):
    for j in range(0,len(arr)-i-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
    print(arr)

# print(arr)
# with open('input.txt','w') as f:
#     for i in arr:
#         f.write(str(i)+",")