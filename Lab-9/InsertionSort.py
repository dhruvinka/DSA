arr=[57,23,75,19,10]

# for i in range(len(arr)):
#     key=arr[i]
#     # set j to -1 so it always check  left side of element
#     j=i-1
#     while j >=0 and arr[j] > key:
#         arr[j+1]=arr[j]
#         j-=1
#     # if key is less than then put at j+1 position
#     arr[j+1]=key



for i in range(len(arr)):
    key=arr[i]
    print("key",key)
    j=i-1
    print("j",j)
    while j>=0 and arr[j]>key:
        print("Comparing", arr[j], "and", key,'j',j)
        arr[j+1]=arr[j]
      
      
        print(arr)
        j-=1
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