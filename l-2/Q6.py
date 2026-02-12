# 6. Write a program to identify anagrams. Given a list of words, group them into a dictionary 
# where the key is the sorted character tuple (or string) and the value is the list of anagrams. 
# Input: ['eat', 'tea', 'tan', 'ate', 'nat', 'ant'] 
# Output: {('a','e','t'): ['eat', 'tea', 'ate'],  
# ('a','n','t'): ['tan', 'nat', 'ant']} 

x=['eat', 'tea', 'tan', 'ate', 'nat', 'ant'] 
y={}
# for word in x:
#     sorted_word=tuple(sorted(word))
#     if sorted_word not in y:
#         y[sorted_word]=[]
#     y[sorted_word].append(word)
# print("Anagrams grouped in dictionary:", y)

for word in x:
    words=tuple(sorted(word))
    if words not in y:
        y[words]=[]
    y[words].append(word)
print(y)