top=None
size=None
stack=None

def init(s):
    global top,stack,size
    top=-1
    size=s
    stack=[]

def is_empty():
    global top
    if top==-1:
        return True
    return False    

def is_Full():
    global top,size
    if top==size-1:
        return True
    return False  

def push(val):
    global top,size,stack
    if is_Full():
        print("Stack is full")
    top+=1
    stack.append(val)

def pop():
    global top,size,stack
    if is_empty():
        print("Stack is Empty")
    top-=1
    return stack.pop()

def peek():
    global top,size,stack
    if is_empty():
        print("Stack is Empty")
    return stack[top]

def display():
    global top,size,stack
    print(top)
    print(size)
    print(stack)


if __name__=="__main__":
    init(10)
    push(1)
    push(2)
    push(3)
    print(peek())
    print(pop())
    print(display())




  
