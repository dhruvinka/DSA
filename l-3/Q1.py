# 1. Create a file named “modular_stack.py” and implement the following functions to provide 
# basic stack operations. Also write a file test_modular_stack.py to test the working of your 
# implementation. 
# a. Declare a variable “Stack” which can hold values for stack size and top position 
# respectively, set its value to None. 
# b. Implement a ms_set_size function which takes integer as an argument for stack 
# size. 
# c. Implement an ms_init_stack function to initialize the stack. 
# d. Implement ms_is_empty and ms_is_full functions which return boolean value. 
# e. Implement ms_push function to perform insertion onto stack. 
# f. 
# Implement ms_pop function to perform deletion on stack. 
# g. Implement ms_peak to return the top element from the stack. 
# h. Implement ms_display to display content stack. 
# i. 
# Implement ms_destroy to remove stack and its content.

stack=None
size=0
top=-1

def set_size(s):
    global size
    size=s
    return size

def init():
    global stack, top
    stack=[]
    top=-1

def is_empty():
    global top
    if top==-1:
        return True
    return False

def is_full():
    global top, size
    if top==size-1:
        return True
    return False

def push(value):
    global stack, top
    if is_full():
        return "Stack Overflow"
    top+=1
    stack.append(value)
    return stack


def pop():
    global stack, top
    if is_empty():
        return "Stack Underflow"
    top-=1
    return stack.pop()

def peak():
    global stack, top
    if is_empty():
        return "Stack is Empty"
    return stack[top]

def display():
    global stack
    return [stack,top,size]
   