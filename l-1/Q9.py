# 9. Write a program to take two lists, zip them into a list of tuples. Then unzip back into two 
# lists. Verify correctness.  

# list1=[1,2,3,4]
# list2=['a','b','c','d']
# zipped=list(zip(list1,list2))
# print("Zipped:",zipped)
# unzipped1, unzipped2=zip(*zipped)   
# print("Unzipped List 1:",list(unzipped1))


list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']

zip = []
for i in range(len(list1)):
    zip.append((list1[i], list2[i]))

print("Zipped List of Tuples:", zip)

unzip = []
unzip = []
for pair in zip:
    unzip.append(pair[0])
    unzip.append(pair[1])

print("Unzipped List 1:", unzip[::2])
print("Unzipped List 2:", unzip[1::2])


print("Correctness Verified:", unzip[::2] == list1 and unzip[1::2] == list2)