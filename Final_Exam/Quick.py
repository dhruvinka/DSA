
# def partion(arr,low,high):
#     pi=arr[low]
#     i=low+1
#     j=high

#     while True:
#         while i <=j and arr[i] <= pi:
#             i+=1
#         while i <=j and arr[i] >= pi:
#             j-=1
#         if i<j:
#             arr[i],arr[j]=arr[j],arr[i]
#         else:
#             break
#     arr[low],arr[j]=arr[j],arr[low]
#     return j

# def Quick(arr,low,high):
#     if low < high:
#         p=partion(arr,low,high)
#         Quick(arr,low,p-1)
#         Quick(arr,p+1,high)



def partion(arr,low,high):
    pivot=arr[low]
    i=low+1
    j=high

    while True:
        while i <= j and arr[i] <= pivot:
            i+=1
        while i <= j and arr[j] >= pivot:
            j-=1
        if i<j:
            arr[i],arr[j]=arr[j],arr[i]
        else:
            break
    arr[low],arr[j]=arr[j],arr[low]
       
    return j

def quick_sort(arr,low,high):
    if low < high:
        pi=partion(arr,low,high)
        quick_sort(arr,low,pi-1)
        quick_sort(arr,pi+1,high)

arr=[10,80,30,90,40,50,30]
print(quick_sort(arr,0,len(arr)-1))

print(arr)