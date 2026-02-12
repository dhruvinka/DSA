from Q1 import *

def reverse_words(s):
    init()
    set_size(50)
    result = ""

    for ch in s:
        if ch != " ":
            push(ch)          
        else:
            while not is_empty():
                result += pop()  
            result += " " 
                  # add space
    while not is_empty():
        result += pop()

    return result


str1 = "Hello World from DDU"
print(reverse_words(str1))
