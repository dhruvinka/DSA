# 7. Write a program to read a list of emails from a text file, it may contain possible duplicates 
# and different logical casing (e.g., User@Example.com vs user@example.com), return a set 
# of unique, normalized (lowercase) emails. 
# Input: ['User@gmail.com', 'user@gmail.com', 'ADMIN@site.org'] 
# Output: {'user@gmail.com', 'admin@site.org'}

# emails = ['User@gmail.com', 'user@gmail.com', 'ADMIN@site.org']
# normalized_set = set()
# for email in emails:
#         normalized_set.add(email.lower())
# print("Unique, normalized emails:", normalized_set)

# modifying an existing element of a tuple 
num = (10, 20, 30, 40, 50)
print(num)
# accept new element and position number
lst= [int(input('Enter a new element: '))]
new = tuple(lst)
pos = int(input('Enter position no: '))
# copy from 0th to pos-2 into another tuple num1
num1 = num[0:pos-1]
# concatenate new element at pos-1 
num1 = num1+new
# concatenate the remaining elements of num from pos till end
num = num1+num[pos:]
print(num)