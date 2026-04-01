
stack=[]
top=-1

def is_empty():
    global top
    return top == -1

def push(x):
    global top,stack
    stack.append(x)
    top+=1

def pop():
    global top,stack
    if is_empty():
        return None
    top-=1
    return stack.pop()

def add_bottem(x):
    global top,stack
    if is_empty():
        push(x)
        return
    tem=pop()
    add_bottem(x)
    push(tem)

def rev_stack():
   if is_empty():
       return
   tem=pop()
   rev_stack()
   add_bottem(tem)
   

n=int(input('enter the number of element you want to add :'))
if n > 0:
    for i in range(n):
        x=int(input("enter the element"))
        push(x)


print("After adding into stack")
print(stack)

rev_stack()

print("After reverse into stack")
print(stack)

