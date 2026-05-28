def merge(arr):
    if len(arr) == 1 :
        return arr
    
    mid=len(arr)//2
    left_part=merge(arr[:mid])
    right_part=merge(arr[mid:])

    return merge_sort(left_part,right_part)

def merge_sort(left,right):

    res=[]
    i,j=0,0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i+=1
        else:
            res.append(right[j])
            j+=1
    res.extend(left[i::])
    res.extend(right[j::])
    return res

x=[10,20,5,6,4,2,25,30]
print(merge(x))