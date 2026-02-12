# 2. Write a program to Find longest increasing contiguous subsequence (list). Read N arr. Find 
# maximal-length contiguous subarray with strictly increasing values; print length and 
# start/end indices. 
# Sample: [1,2,3,1,2] → length=3 start=0 end=2

# # x=[1,2,3,1,2]
n=input()
y=n.split()
x=[int(num) for num in y]
index=0
l=0
start=0
li=[]
for i in range(len(x)):
  if i != len(x)-1:
    if x[i+1] > x[i]:
        if x[i+1] - x[i] == 1:
            if l==0:
                s=i
            l=l+1
            index=i
    else:
        if l>0:
            li.append((l+1,s,index))
        l=0
if l>0:
    li.append((l+1,s,index))
       
fin=sorted(li,reverse=True)
print(fin)
print()


# inp = input()
# lis = inp.split(' ')
# lis = [int(num) for num in lis]
# n = len(lis)

# max_len = len = 1
# start = max_start = max_end = 0

# for i in range(1, n):
#     if lis[i] > lis[i - 1]:
#         len += 1
#     else:
#         len = 1
#         start = i

#     if len > max_len:
#         max_len = len
#         max_start = start
#         max_end = i

# print("Length :", max_len, "Start :", max_start, "End :", max_end)