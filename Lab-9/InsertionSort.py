arr=[50,60,10,203,30,90]

for i in range(len(arr)):
    key=arr[i]
    # set j to -1 so it always check  left side of element
    j=i-1
    while j >=0 and arr[j] > key:
        arr[j+1]=arr[j]
        j-=1
    # if key is lase then then put at j+1 positionl
    arr[j+1]=key

print(arr)
















# arr=[50,60,10,203,30,90]

# for i in range(len(arr)):
#     key=arr[i]
#     j=i-1
#     while j>=0 and arr[j]>key:
#         arr[j+1]=arr[j]
#         j-=1
#     arr[j+1]=key

# print(arr)