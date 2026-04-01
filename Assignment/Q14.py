def subarray(arr):

    sub=[]
    for i in range(len(arr)):
        for j in range(i+1,len(arr)+1):
            sub.append(arr[i:j])

    sum=0
    for i in range(len(sub)-1):
        x=min(sub[i])
        y=max(sub[i])
        result=y-x
        sum+=result
    
    print(sub)
    print(sum)


size=int(input("Enter the size of an arr : "))
x=[]
for i in range(1,size+1):
    val=int(input("Enter the values of an element : "))
    x.append(val)
subarray(x)

        