size=5
stack=[None]*size
top=-1

def is_full():
    global top,size
    return top==size-1

def is_empty():
    global top
    return top==-1

def push(data):
    global top,stack
    if is_full():
        print("full")
    else:
        top+=1
        stack[top]=data
    
def pop():
    global top,stack
    if is_empty():
        print("empty")
    else:
        data=stack[top]
        stack[top]=None
        top-=1
        return data
    
def peek():
    global top,stack
    if is_empty():
        print("empty")
    else:
        data=stack[top]
        return data
    
if __name__ == "__main__":
    push(10)
    push(2)   
    push(3)
    push(45)
    push(50)
    print(stack)
    print(peek())
    print(pop())
    print(pop())
    print(stack)
