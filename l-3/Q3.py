# 3. Create a file named “Stack.py” and implement the following behaviours to provide basic 
# stack operations in the Stack Class.  
# a. Instance of “Stack” which can hold values as per defined size  
# b. It should maintain a top position  
# c. Users can set size at time of object creation. 
# d. Implement is_empty and is_full functions which return boolean values. 
# e. Implement basic operations on stack.


from Stack import *


s1=Stack(10)
s1.init()

def is_empty():
   if( s1.top==-1):
      return True
   return False

def is_full():
   if ( s1.top == s1.size-1):
      return True
   return False

def push(val):
   if (is_full()):
      print("Stack is full")
   s1.top+=1
   s1.stack.append(val)
   

def pop():
   if is_empty():
      print("Stack is empty")
   s1.top-=1
   return s1.stack.pop()

def peek():
    if is_empty():
          print("Stack is empty")
    return s1.stack[s1.top]


push(30)
s1.dis()
print("Peek:",peek())
s1.dis()
print(pop())